# Trend-tooling architecture

This documents the set of scripts built to support Data, Worn Thin.'s content pillars. The scripts have been scoped through discussions with Claude before any code was written. This file captures what each piece is for and why it's shaped the way it is. It shall also be continuously updated as the design evolves to ensure that it remains a fair reflection of what's been built instead of what's been scoped.

## Why multiple files?
Each piece has different resposibilities, use-cases and dependencies. Keeping them separate makes them easier to understand, test, change and lines up with how the work is being branched (roughly one file per branch).

## Files

### `trend_fetchers.py`
**Purpose:** To surface fashion-releveant trending searches without needing to already know what to look for. 
- Uses trendspy's `trending_now()`. This doesn't require a keyword.
- Filters results down to genuinely fashion-relevant items (the exact filtering method is still to be worked out and tested, `trending_now()`'s support for category filtering isn't confirmed yet. Currently debating whether the filter should be done after the fetch or at the API level).
- If a short time window (4h/24h) comes up thin, it should widen to a longer one (48h, then 7 days) before giving up.
- Reports however many fashion-reevant trends genuinely qualify, rather than padding to a fixed number.
- Output is a shortlist tio glance at. It doesn't automatically feed into the forecast engine.
- Candidates are manually picked from this stage.

