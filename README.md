# Data Worn Thin

**Fashion trends, decoded by who actually pays the price.**

The data and analysis behind [@datawornthin](https://www.instagram.com/datawornthin/), a weekly Instagram and LinkedIn carousel series on the fashion industry: what clothes cost, what workers earn, and who covers the gap during a cost-of-living crisis.

Each post is an "issue". Every number in an issue traces back to a public source and to a notebook in this repo.

## Why this exists

Most fashion-data content predicts what's coming next. This project asks a different question: who absorbs the cost?

It starts from the view that buying cheap clothes is often the sensible choice when money is tight. It then follows the numbers to see where the rest of the bill lands: on a worker, on the environment, or on the shopper later through debt. No lectures, just the data.

## What it covers

Issues rotate through five recurring pillars:

1. **Price per wear vs. real wages.** How many hours of minimum-wage work a haul costs, adjusted for inflation.
2. **Trend cycle speed.** How fast micro-trends rise and get discarded.
3. **Who actually gets paid.** How a garment's price splits between worker, brand, and retailer.
4. **"Affordable" isn't the same as cheap.** Whether fast fashion saves money for low-income shoppers or costs more over time.
5. **Trend forecast, with receipts.** Upcoming trends, plus what each one costs.

## Published issues

| Issue | Title | Pillar |
| --- | --- | --- |
| 00 | Intro carousel (Issue 0) | N/A |
| 01 | Buy Now Owe Later | 4 |
| 02 | The Denim Divide | 1 |
| 03 | Hot Take Cold Coat | 2 |
| 04 | Threaded Through Credited Nowhere | 3 |
| 05 | Glowy Sheen Repurposed | 5 |
| 06 | Coat of Many Colors | 4 |
| 07 | Reign, Rewear. | 1 |
| 08 | One's Uniform, Everyone's Aesthetic | 2 |
| 09 | Behind The Label, Worn At The Seams. | 3 |
| 10 | Long Story, Short Skirt. | 5 |

Pillar numbers match the list under "What it covers" above.

## How an issue gets made

1. **Scope.** A question, a working hypothesis, and a plan for which data could answer it.
2. **Analyse.** One notebook pulls live economic data, a second handles hand-collected figures such as retail prices and wages.
3. **Check the story against the data.** Copy is written only after the charts exist. If the data doesn't support the hypothesis, the story changes.
4. **Write and cite.** Slide copy, caption, and a full reference list.
5. **Design and publish.** Charts are rebuilt in Canva in the brand style, checked against the notebook versions, and posted as a carousel.

## How the numbers are sourced

- **Public data first.** Wage and price series come from US government sources (Bureau of Labor Statistics, the Federal Reserve's FRED database and household survey).
- **Primary sources only.** Statistics are traced back to the original study. One widely repeated figure turned out not to be in the paper everyone cites for it, so it was dropped.
- **Hand-collected figures are logged.** Each one is recorded with its date, link, screenshot, and exchange rate in `/sources`.
- **Citations follow APA 7th edition.**
- **If a number can't be traced, it doesn't get published.**

## What's in here

```
brand/        Colour palette and visual assets
content/      Slide copy, captions, and references for each issue
data/         Processed data (raw pulls are not committed)
notebooks/    The analysis behind each issue
scripts/      Reusable Python for pulling data and tracking trends
sources/      Source log and screenshots for each issue
calendar.csv  Overview of every issue and its status
```

Content, notebooks, data, and sources are grouped by `cycle N/issue-XX`.

## Tools

- **Analysis:** Python (pandas, matplotlib), Jupyter notebooks
- **Data:** FRED and BLS APIs via requests, Google Trends via trendspy
- **Design:** Canva, using a shared brand palette
- **Workflow:** Git and GitHub, one branch and one tracked issue per post

## Running the analysis

```bash
git clone https://github.com/juvinciariadi/data-worn-thin.-.git
cd data-worn-thin.-
pip install pandas matplotlib requests python-dotenv trendspy notebook
```

Notebooks that pull from FRED need a free [API key](https://fred.stlouisfed.org/docs/api/api_key.html). Save it in a file named `.env` in the repo root:

```
FRED_API_KEY=your_key_here
```

## About

Built by Juvincia Riadi, a Data Science student at the University of Western Australia. I handle every step: research, analysis, writing, and design.

[LinkedIn](https://www.linkedin.com/in/juvincia-riadi-309432316) · [Instagram](https://www.instagram.com/datawornthin/)

## Licence

- **Code** (`/scripts`): MIT, see [LICENSE](LICENSE).
- **Content and analysis** (`/content`, `/brand`, `/sources`, `/notebooks`): CC BY-NC-ND 4.0, see [CONTENT_LICENSE.md](CONTENT_LICENSE.md). Share with credit, no commercial use, no remixes.
- **Underlying government data** is public domain. Only the original analysis and presentation are covered above.