# Issue #5 — Sources
"Glowy Sheen, Repurposed" | Pillar 5 (trend forecast, with receipts)

---

## Manual price sourcing log

All prices are each market's own published RRP, not a currency conversion. Checked 21/08/2026.
Screenshots stay local only (`sources/issue-05/screenshots/`), not committed to the repo.

| Product | Market | Price | Date checked | Source URL |
|---|---|---|---|---|
| Rimmel Kind & Free Skin Tint | AU | $21.95 | 21/08/2026 | https://www.amazon.com.au/dp/B09FY5DG8G?th=1 |
| Rimmel Kind & Free Skin Tint | US | $11.00 | 21/08/2026 | https://www.amazon.com/Rimmel-Kind-Free-Foundation-Vanilla/dp/B09FY5DG8G |
| Maybelline SuperStay 24hr Skin Tint | AU | $37.99 | 21/08/2026 | https://www.beautycrew.com.au/product/maybelline-super-stay-up-to-24hr-skin-tint-11980 |
| Maybelline SuperStay 24hr Skin Tint | US | $17.99 | 21/08/2026 | https://www.ulta.com/p/super-stay-24h-skin-tint-vitamin-c-pimprod2039657?sku=2610824 |
| The Ordinary Serum Foundation | AU | $12.70 | 21/08/2026 | https://theordinary.com/en-au/serum-foundation-100445.html |
| The Ordinary Serum Foundation | US | $7.50 | 21/08/2026 | https://theordinary.com/en-us/serum-foundation-100445.html |
| Hourglass Veil Hydrating Skin Tint | AU | $86.00 | 21/08/2026 | https://www.sephora.com.au/products/hourglass-veil-hydrating-skin-tint |
| Hourglass Veil Hydrating Skin Tint | US | $49.00 | 21/08/2026 | https://www.sephora.com/product/veil-hydrating-skin-tint-P506573 |
| MAKE UP FOR EVER HD Skin Balancing & Perfecting Foundation | AU | $74.00 | 21/08/2026 | https://www.sephora.com.au/products/make-up-for-ever-hd-skin-balancing-and-perfecting-foundation/v/100c-washi |
| MAKE UP FOR EVER HD Skin Balancing & Perfecting Foundation | US | $49.00 | 21/08/2026 | https://www.makeupforever.com/us/en/face/foundation/balancing-and-perfecting-foundation-MI000023621.html |

**Note on the Hourglass/MUFE pair:** both confirmed as the same exact product name in both AU and US
markets, no naming mismatch. An earlier candidate (Clinique Even Better Clinical™ Vitamin Makeup
SPF 25) was dropped from this table specifically because its AU listing didn't match any single US
product under the same name, the closest US equivalents were a different SPF (45) or a differently
named product (Serum Foundation) in the same line. Swapped for Hourglass to avoid that ambiguity.

---

## Data honesty notes

### 1. Google Trends data (first-party, primary stat)
Pulled via `trendspy` for "skin tint," "tinted moisturizer," "BB cream," and "skin-like finish,"
US geo, timeframe 2023-08-01 to 2026-08-21. Retrieved 21/08/2026.
- "skin-like finish" returned flat zero across the entire window. This is a real finding (pure
  marketing copy that never entered actual search behavior), not a data gap, worth keeping in the
  chart and possibly the copy.
- Locked hook stat: "skin tint" fell -75% over the trailing 3 months (60 → 15). Full window
  (2023-07-30 to 2026-08-09): 7 → 15. Peak: 100 on April 12, 2026 (the final day of Coachella
  Weekend 1). All three active terms peaked on that same date.

### 2. Market Defense / BeautyMatter quote — single-sourced, demoted to background color
BeautyMatter. (2026, August 18). *Inside complexion's formulation, supply chain, and consumer
shift: The new face of foundation.* https://beautymatter.com/articles/the-new-face-of-foundation-inside-complexions-formulation-supply-chain-and-consumer-shift
*(Exact publish date approximate — verify before final citation.)*
- Quotes Vanessa Kuykendall (Chief Engagement Officer, Market Defense) on rising search volumes
  for "skin tint" and related terms, and cites prestige face makeup at $5.2B in flat H1 2025 sales.
- **Discrepancy, explained, not hidden:** this source frames search interest as climbing; our
  first-party data shows a -75% decline in the same window. Both are likely true, just measuring
  different three-month slices of the same spike-and-crash curve (this source's window plausibly
  caught the run-up into the April 12 peak; ours catches the crash afterward). Do not present the
  two as independently confirming each other.

### 3. Beauty waste stats — two different reports, do not conflate
There are **two separate industry reports** in circulation with similar-sounding but different
figures. We are using the British Beauty Council figures below. A different report (Avery
Dennison / covered by Global Cosmetic Industry and Premium Beauty News) gives a different number,
6.2% beauty industry overproduction loss vs. 3.9% apparel, 3% pharma, 2.9% food, 1.1% auto, which
is **not** the stat we're citing. Keep these separate; they use different methodologies.

Our stat: **~2% of cosmetic items are thrown away due to overproduction, a rate higher than
fashion, pharmaceutical, food, or the auto industry** (British Beauty Council). Corroborated
across two independent trade press write-ups (not a single-source claim), though we could not
locate the British Beauty Council's own primary report page directly, only secondary citations of
it:
- Business Waste. (2024, April 4). *Makeup waste statistics and facts.* https://www.businesswaste.co.uk/waste-facts/makeup-waste-statistics-and-facts/
- Professional Beauty. (2026, March 19). *95% of beauty packaging is thrown away.* https://professionalbeauty.co.uk/95-of-beauty-packaging-is-thrown-away

### 4. Correction — the "20-40% waste, Arnaud Plas" attribution could not be re-verified
The scope doc previously attributed a "20-40% of beauty products end up as waste" estimate
specifically to Arnaud Plas (Prose co-founder/CEO) via LinkedIn. Searching directly for this
quote did not turn up any interview, article, or post where Plas states this figure personally.
What the same 20-40% figure traces to instead is a **general industry estimate**, also attributed
to British Beauty Council in secondary sources (see Business Waste, above), with no personal
attribution to Plas found.
**Recommendation:** drop the Arnaud Plas/Prose attribution. Cite the 20-40% figure as a general
British Beauty Council estimate instead, same sourcing as the 2% and 70% figures above, or omit
it entirely and lead with the sharper, better-corroborated 2%-overproduction stat.

### 5. Coachella 2026 dates (confirms the hook-stat explanation)
Wikipedia contributors. (2026). *Coachella 2026.* Wikipedia. https://en.wikipedia.org/wiki/Coachella_2026
- Weekend 1: April 10-12, 2026. Weekend 2: April 17-19, 2026. Empire Polo Club, Indio, California.
  Headliners: Sabrina Carpenter, Justin Bieber, Karol G.

### 6. Rare Beauty launch date (secondary contributing factor)
Hypebae. (2026, March 16). *Rare Beauty announces a brand new foundation.* https://hypebae.com/2026/3/rare-beauty-selena-gomez-true-to-myself-natural-matte-longwear-foundation-where-to-buy
- True to Myself Natural Matte Longwear Foundation, $38 USD, launched April 2, 2026 at Sephora and
  RareBeauty.com, roughly ten days before the April 12 search-interest peak.

---

## Sources to avoid / flag
- Several "skin tints are replacing foundation" pieces (e.g., runwaylive.com) read as templated SEO
  content citing other SEO content in a loop, do not use as sourced claims.
- "Average woman owns 40 cosmetic products, uses only 5" appears in multiple beauty blogs without a
  traceable primary source. Needs verification or should be dropped.
- Generic "market research" aggregator sites (accio.com, marketintelo.com) returned speculative,
  unmethodologied growth numbers for skin tint specifically, avoid citing directly.