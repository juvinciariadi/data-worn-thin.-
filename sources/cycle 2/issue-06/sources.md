# Issue #6 — Sources

Working sourcing log. Screenshots referenced here stay local only (`sources/issue-06/screenshots/`), not committed to the repo, per project convention.

---

## Hook stats

**University of Florida News.** (1996, October 2). *Brand names hinder school uniform policies, says UF researcher.*
https://archive.news.ufl.edu/articles/1996/10/brand-names-hinder-school-uniform-policies-says-uf-researcher.html
Institutional source (UF's own news archive, not a secondary aggregator). Study: Lake City, FL public school, voluntary uniform policy. 114 student essays, average 3.5 brand names mentioned each, 91% cited brand names as a major reason for clothing choices. Researcher: David Jamison.

**CNN.** (2018, November 16). *High school bans Canada Goose and Moncler jackets to protect poorer children.*
https://edition.cnn.com/2018/11/16/uk/school-coat-ban-poverty-gbr-scli-intl/index.html
Woodchurch High School, Wirral, England. Banned Canada Goose, Moncler, Pyrenex coats after Christmas break 2018. Headteacher: Rebekah Phillips. Framed explicitly as "poverty-proofing," a term also used by Children North East, referenced in the same article. Coats up to ~£1,000 / ~$1,280 USD (2018 GBP-to-USD conversion, performed by CNN, not by DWT). Cross-verified against BBC, ABC News, and Fox News coverage.

---

## 06a — Apparel CPI vs. Wages (live FRED pull)

**Federal Reserve Bank of St. Louis.** (n.d.). *Consumer Price Index for All Urban Consumers: Apparel [CPIAPPSL].* FRED.
https://fred.stlouisfed.org/series/CPIAPPSL

**Federal Reserve Bank of St. Louis.** (n.d.). *Average Hourly Earnings of Production and Nonsupervisory Employees [AHETPI].* FRED.
https://fred.stlouisfed.org/series/AHETPI

Pulled: 2026-08-28. Raw data saved locally at `data/raw/issue-06/` (gitignored). Processed/indexed data saved at `data/processed/issue-06/apparel_cpi_vs_wages_indexed.csv`.

**Finding:** Apparel CPI indexed to ~289 by 2026-07, wages indexed to ~1,296 over the same period (base year = 100, ~1964 start). Apparel costs did not rise faster than wages, they fell substantially behind. Drives the "clothes got cheaper, the status garment didn't" framing.

---

## 06b — Coat price gap (manual pricing)

**Budget coat: Primark, 7-15yrs Hooded Puffer Jacket** (Product No. 991175559804)
https://www.primark.com/en-us/p/7-15yrs-hooded-puffer-jacket-black-991175559804
Price observed: **$14.00 USD** (natively listed currency, Primark's US site)
Converted: AU$19.46 (derived, not independently sourced from an AU listing)
Screenshot: `sources/issue-06/screenshots/primark-puffer-2026-08-28.png` *(capture pending)*
Date checked: 2026-08-28

**Designer coat: Canada Goose AU, Kids Snowy Owl Parka**
https://canadagoose.com.au/collections/kids
Price observed: **AU$1,100.00 USD** (corrected figure, verified directly by Juvincia on-site; superseded an earlier AU$750.00 figure found via search, which appears to have been outdated or inaccurate)
Converted: $791.45 USD (derived from AUD)
Screenshot: `sources/issue-06/screenshots/canadagoose-parka-2026-08-28.png` *(capture pending, especially important here given the price correction)*
Date checked: 2026-08-28
Note: this is a collection listing page, not a direct single-product URL (the direct product page returned a 404 when checked). Worth grabbing a precise product-page link if the catalog changes.

**Exchange rate:** 1 AUD = 0.7195 USD, as of 2026-08-27, via Xe/Forbes Advisor.

**Price gap:** AU$1,080.54 / $777.45 USD, **56.5x** (rounded to 57x for slide copy, per bold-number/readability convention; precise figure preserved here).

---

## Currency direction notes

Two prices were sourced in different native currencies, worth keeping explicit for any future re-verification:
- Primark: natively USD → AUD is the derived/converted figure
- Canada Goose: natively AUD → USD is the derived/converted figure

This issue converts directly between currencies (per Juvincia's direction), consistent with the style guide's rule for manual price data paired against a USD wage benchmark (06a).

---

## Open items

- [ ] Capture and save both price screenshots locally (Primark and Canada Goose), not yet done as of this log
- [ ] Confirm whether the earlier AU$750 Canada Goose figure was a genuine price change or a search-result inaccuracy, for the internal record only, not required for publishing since the corrected AU$1,100 figure is verified on-site