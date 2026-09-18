"""
forecast_trend.py

Single reusable forecasting script for Data, Worn Thin.

Handles two kinds of input, since both are ultimately the same problem
(one time series, project it forward):
  - Google Trends search interest, via trendspy
  - FRED macro/economic series (e.g. apparel CPI, minimum wage)

Forecasting method: Holt-Winters exponential smoothing
(statsmodels.tsa.holtwinters.ExponentialSmoothing). Chosen over a plain
moving average because it captures trend AND seasonality (Google Trends
data especially tends to repeat yearly, e.g. "coats" spiking every
winter), and over ARIMA because it needs no manual order tuning while
still being a real, citable statistical model rather than a guess.

Usage examples:
    py -3.14 forecast_trend.py --source trends --query "linen pants" --periods 12
    py -3.14 forecast_trend.py --source fred --query CPIAPPSL --periods 12 --seasonal-periods 12

Output:
    A CSV of historical + forecast values, and a branded PNG chart,
    written to --output-dir (default: current folder). Route these into
    data/processed/cycle N/issue-XX/ per the repo convention before
    committing.
"""

import argparse
import json
import os
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from statsmodels.tsa.holtwinters import ExponentialSmoothing

load_dotenv()


# ---------------------------------------------------------------------------
# 1. Fetching: one function per source, both return the same shape
#    (a pandas Series named "value", indexed by date, ascending)
# ---------------------------------------------------------------------------

def fetch_google_trends(keyword: str, timeframe: str = "today 5-y") -> pd.Series:
    """Pull Google Trends search-interest-over-time for one keyword.

    trendspy replaces the archived pytrends (which now returns 429s).
    Interest is a 0-100 index, not an absolute volume.
    """
    from trendspy import Trends

    tr = Trends()
    df = tr.interest_over_time(keyword, timeframe=timeframe)

    # trendspy returns the keyword itself as the value column name
    series = df[keyword].rename("value")
    series.index = pd.to_datetime(series.index)
    return series.sort_index()


def fetch_fred_series(series_id: str, api_key: str | None = None) -> pd.Series:
    """Pull one FRED series (e.g. CPIAPPSL, FEDMINNFRWG) as a plain series.

    FRED returns a JSON error object (not an HTTP error) on a bad series
    ID or bad key, so we check for "observations" explicitly and surface
    FRED's own error message rather than letting a bare KeyError happen.
    """
    api_key = api_key or os.getenv("FRED_API_KEY")
    if not api_key:
        raise RuntimeError(
            "No FRED_API_KEY found. Add it to a gitignored .env file "
            "(never hardcode it, a past key leak required rotation)."
        )

    url = "https://api.stlouisfed.org/fred/series/observations"
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
    }
    resp = requests.get(url, params=params, timeout=30)
    payload = resp.json()

    if "observations" not in payload:
        raise RuntimeError(f"FRED error for series '{series_id}': {payload}")

    df = pd.DataFrame(payload["observations"])
    df = df[df["value"] != "."]  # FRED uses "." for missing observations
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = df["value"].astype(float)

    series = df.set_index("date")["value"]
    return series.sort_index()


# ---------------------------------------------------------------------------
# 2. Forecasting: one shared core for either kind of series
# ---------------------------------------------------------------------------

def forecast_series(
    series: pd.Series,
    periods: int,
    seasonal_periods: int | None = None,
    interval_repetitions: int = 300,
) -> pd.DataFrame:
    """Fit Holt-Winters and forecast `periods` steps ahead.

    Returns a DataFrame with columns: value, forecast, lower, upper.
    `value` and `forecast` are mutually exclusive (one is NaN wherever
    the other is set), so the two can be plotted as one continuous line
    with a visible handoff point.

    seasonal_periods is the number of observations in one full seasonal
    cycle, e.g. 12 for monthly data with yearly seasonality, 52 for
    weekly Google Trends data with yearly seasonality. Pass None to fit
    a trend-only model (no seasonality) if the series is too short for
    a seasonal fit or doesn't show a clear cycle.
    """
    seasonal = "add" if seasonal_periods else None

    model = ExponentialSmoothing(
        series,
        trend="add",
        seasonal=seasonal,
        seasonal_periods=seasonal_periods,
        initialization_method="estimated",
    )
    fit = model.fit()

    point_forecast = fit.forecast(periods)

    # Simulated paths give a simple, honest uncertainty band instead of
    # presenting a single forecast line as if it were certain.
    sim_paths = pd.concat(
        [
            fit.simulate(nsimulations=periods, anchor="end", error="add")
            for _ in range(interval_repetitions)
        ],
        axis=1,
    )
    lower = sim_paths.quantile(0.1, axis=1)
    upper = sim_paths.quantile(0.9, axis=1)

    # np.nan (not pd.NA) so matplotlib can plot these columns directly
    history = pd.DataFrame(
        {"value": series, "forecast": float("nan"), "lower": float("nan"), "upper": float("nan")}
    )
    future = pd.DataFrame(
        {
            "value": float("nan"),
            "forecast": point_forecast,
            "lower": lower.values,
            "upper": upper.values,
        },
        index=point_forecast.index,
    )
    result = pd.concat([history, future])
    return result.astype(
        {"value": "float64", "forecast": "float64", "lower": "float64", "upper": "float64"}
    )


# ---------------------------------------------------------------------------
# 3. Plotting: exploratory + branded versions, per repo chart conventions
# ---------------------------------------------------------------------------

def load_palette(palette_path: str) -> dict:
    with open(palette_path) as f:
        return json.load(f)


def plot_forecast(result: pd.DataFrame, title: str, palette_path: str, output_dir: Path):
    # Exploratory version: plain matplotlib, for checking the shape works
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(result.index, result["value"], label="Actual")
    ax.plot(result.index, result["forecast"], label="Forecast")
    ax.fill_between(result.index, result["lower"], result["upper"], alpha=0.2)
    ax.set_title(f"{title} (exploratory)")
    ax.legend()
    fig.savefig(output_dir / "forecast_exploratory.png", dpi=150)

    # Branded version: palette-styled, per repo convention
    palette = load_palette(palette_path)
    with plt.rc_context({"font.family": "serif"}):  # avoids font-not-found warnings
        fig2, ax2 = plt.subplots(figsize=(9, 5))
        ax2.plot(result.index, result["value"], color=palette["Cocoa"], linewidth=2, label="Actual")
        ax2.plot(result.index, result["forecast"], color=palette["Dusty"], linewidth=2, linestyle="--", label="Forecast")
        ax2.fill_between(result.index, result["lower"], result["upper"], color=palette["Sage"], alpha=0.3)
        ax2.set_title(title)
        ax2.spines["top"].set_visible(False)
        ax2.spines["right"].set_visible(False)
        ax2.legend(frameon=False)
        ax2.xaxis.set_major_locator(MaxNLocator(8))
        fig2.autofmt_xdate()
        fig2.savefig(output_dir / "forecast_branded.png", dpi=150)


# ---------------------------------------------------------------------------
# 4. CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Forecast a Google Trends or FRED series.")
    parser.add_argument("--source", choices=["trends", "fred"], required=True)
    parser.add_argument("--query", required=True, help="Keyword (trends) or series ID (fred)")
    parser.add_argument("--periods", type=int, default=12, help="Steps to forecast ahead")
    parser.add_argument("--seasonal-periods", type=int, default=None, help="e.g. 12 monthly, 52 weekly")
    parser.add_argument("--timeframe", default="today 5-y", help="trendspy timeframe string (trends only)")
    parser.add_argument("--palette", default="brand/palette.json")
    parser.add_argument("--output-dir", default=".")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.source == "trends":
        series = fetch_google_trends(args.query, timeframe=args.timeframe)
    else:
        series = fetch_fred_series(args.query)

    result = forecast_series(series, args.periods, args.seasonal_periods)
    result.to_csv(output_dir / "forecast_output.csv")

    plot_forecast(result, title=args.query, palette_path=args.palette, output_dir=output_dir)

    print(f"Forecast written to {output_dir / 'forecast_output.csv'}")
    print(f"Charts written to {output_dir / 'forecast_exploratory.png'} and forecast_branded.png")


if __name__ == "__main__":
    main()