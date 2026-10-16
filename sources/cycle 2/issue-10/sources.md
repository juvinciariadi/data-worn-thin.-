# Issue #10 sources: Long Story, Short Skirt

Source log for Issue #10 (Pillar 5, closes cycle 2). Every figure on the slides traces to an entry here or to a notebook in `notebooks/cycle 2/issue-10/`. Full APA citations are in `references.md`.

---

## Slide 2: THE ICON

### Data, But Make It Fashion: miniskirt reel
- URL: https://www.instagram.com/reel/DW_qtHriQuI/
- Date: 11 April 2026 (Instagram omits the year for posts from the current year)
- Claim: miniskirt popularity up 78% in April so far, compared with the average of the previous six months; S&P 500 up 4% over the last six months
- Method stated in caption: online posts and their sentiment, Google search data, Pinterest search data
- Caption also credits the hemline index to "economist George Taylor" in the 1920s (see slide 4)
- Caption caveat: "just a fun correlation," "could totally just be seasonal"
- Engagement when checked (2026-10-16): about 28.4K likes, 576 reposts
- Screenshot kept local (another creator's content)

---

## Slide 3: THE STAT

### Data, But Make It Fashion: maxi skirt carousel
- URL: https://www.instagram.com/p/DHbO0OWuJoh/
- Date: 20 March 2025 (5 slides)
- Slide 1: maxi skirt popularity up 393%, read as a sign of heading into a recession
- Slides 2 to 4: lipstick +108%, corporate fashion +39%, minimalist fashion +38%
- Slide 5: bar chart, "based on analyses i ran on hundreds of thousands of online data points"
- Caption: "this is MY stock market"; S&P 500 "down nearly 7% this past month"; "not legitimate financial or investing advice"
- Engagement when checked (2026-10-16): about 220K likes, about 20.8K shares
- Screenshots kept local

### Data, But Make It Fashion: follow-up post (method source)
- URL: https://www.instagram.com/reel/DHd2JT2OGdw/?rpxt=MXQ5OWJsZ3M0eGJwMw==
- Date: 21 March 2025
- Caption: "hundreds of thousands of online data points to assess popularity of these trends one week ago vs today"
- Confirms the window for the 393% figure: one week
- Engagement when checked (2026-10-16): about 106K likes, about 16.6K shares
- Screenshot kept local

### Independent record of the one-week window
- Het Financieele Dagblad (2025, April 1). Dutch newspaper article; copy hosted by Erasmus School of Economics: https://eur.nl/media/127032
- Reports maxi skirt popularity up 393% "last week" (US), lipstick up 108%
- Also the source for Franses's quote (slide 5)

### "Almost 90 years"
- van Baardwijk & Franses (2010): monthly hemline data, January 1921 to December 2009 (see slide 5)

---

## Slide 4: THE ORIGIN

### George W. Taylor's thesis (primary source)
- Taylor, G. W. (1929). *Significant post-war changes in the full-fashioned hosiery industry*. University of Pennsylvania Press. https://www.jstor.org/stable/j.ctv4s7g3z
- Accessed via the UWA library (JSTOR), 2026-10-15
- Chapters checked: all 7 (I Purpose and Scope; II Trends in Production; III Evidences of Changed Management Problems; IV Equipment Trends; V Nature of the Equipment; VI Productivity of Different Types of Knitting Machinery; VII Summary and Conclusions). Front matter not checked.
- Every mention of skirts is about demand for stockings: pp. 27, 28, 37, 51, 87, 115
  - p. 27: the change to shorter skirts around the start of 1925 increased demand for silk stockings
  - p. 115 (Summary and Conclusions): stocking consumption kept rising in 1926 to 1928 "as the result of shorter skirts, the continued demand for silk and sheerness, and the vogue of colors"
- No link between skirts and the economy or stock market in any chapter checked
- p. 27 also quotes Arthur S. Gutman (president, Rivoli Silk Hosiery Co.) on short skirts; that quote is Gutman's, not Taylor's
- The widely repeated "1926" date is a misattribution: the thesis was published in 1929
- PDFs kept local only (JSTOR terms of use)

### Corroborating secondary source
- Komar, M. (2020, September 1). Is the hemline index actually real? *InStyle*. https://www.instyle.com/fashion/clothing/what-is-the-hemline-index-real
- Clara Berg (Curator of Collections, Museum of History & Industry, Seattle) says Taylor's 1929 thesis linked skirt length to hosiery sales, not the economy, and the idea was later distorted in retelling
- Also used (caption only): Berg on the post-1947 Dior New Look, when long skirts signalled prosperity

### Photo of George W. Taylor
- Library of Congress item 2017695792: https://www.loc.gov/item/2017695792/
- Credit line: Library of Congress, Prints & Photographs Division, Farm Security Administration/Office of War Information Black-and-White Negatives
- Rights: US government work (Office of War Information). Rights Advisory on page: Library of Congress, Prints & Photographs Division, Farm Security Administration/Office of War Information Black-and-White Negatives.
- Date: 1943
- Checked 2026-10-16: the Wharton economist and War Labor Board member, not the Civil War officer of the same name (https://www.loc.gov/item/2018666499/)

---

## Slide 5: THE TURN

### The 2010 study (primary source)
- van Baardwijk, M., & Franses, P. H. (2010). *The hemline and the economy: Is there any match?* (Econometric Institute Report 2010-40). Erasmus University Rotterdam. http://hdl.handle.net/1765/20147
- Full text: https://www.eur.nl/en/media/2020-11-hemline-and-economy-there-any-match
- Read 2026-10-15
- Data: monthly dress lengths coded from the French fashion magazine *L'Officiel*, January 1921 to December 2009, in 5 categories (mini to floor length); missing months filled with the previous issue's value
- Compared with US recession dates (NBER business cycle chronology)
- Finding: the economy leads the hemline by about 3 years
- Reverse test: no evidence that hemlines predict recessions, at the same time or with any delay
- A working paper, not peer-reviewed

### Franses's later view
- Het Financieele Dagblad (2025, April 1), copy hosted by Erasmus: https://eur.nl/media/127032
- Franses calls the hemline index an "urban legend" and says to look for regularity and causality, not coincidence

### Slide 5 image
- Cropped first page of the 2010 paper (The hemline and the economy: is there any match?, Marjolein van Baardwijk & Philip Hans Franses), from the full-text link above. https://www.eur.nl/en/media/2020-11-hemline-and-economy-there-any-match

---

## Slide 6: THE MECHANISM

### Google Trends pulls (notebook 10.3)
- Tool: `trendspy`, Google Trends, United States, web search, pulled 2026-10-16
- Raw files in `data/raw/cycle 2/issue-10/`:
  - `trends_monthly.csv`: "maxi skirt", "mini skirt", January 2004 to September 2026
  - `trends_monthly_prespike.csv`: same terms, January 2004 to December 2025
  - `trends_weekly.csv`: each term on its own scale, January 2022 to September 2026
  - `trends_weekly_combined.csv` and `trends_weekly_prespike.csv`: both terms on a shared scale (to September 2026; to February 2026)
  - `trends_weekly_controls.csv`: "skirt", "jeans", "sofa", "pizza", January 2022 to September 2026
- Google Trends values are relative (0 to 100 within each pull) and sampled, so repeat pulls can differ slightly. The saved CSVs are the record for this issue.

### Figures used
- Maxi skirt searches about 2x higher in May than January in a typical year (May 136.6, January 66.5; 100 = an average month; 2011 to 2025)
- Week containing 20 March 2025: maxi skirt searches up 13.2% on the previous week; a rise of that size occurs in about 1 week in 13 (January 2022 to February 2026)
- Week of 12 April 2026: "maxi skirt", "mini skirt", "skirt", "jeans" and "sofa" all peak at the same time with the same shape; "pizza" does not

### Public confirmation of the April 2026 spike
- Checked on trends.google.com, 2026-10-16: "mini skirt", "jeans", "sofa"; United States; January 1, 2024 to October 16, 2026; All Categories; Web Search
- All three peak together in spring 2026
- Screenshot: `sources/cycle 2/issue-10/screenshots/Screenshot 2026-10-16 103923`
- Cause of the spike: unknown. No public explanation found. Treated as a data blip, not real interest in skirts.

---

## Slide 7: WHO PAYS

### Who owns the stock market (notebook 10.1)
- Board of Governors of the Federal Reserve System, Distributional Financial Accounts, via FRED (Federal Reserve Bank of St. Louis). Pulled 2026-10-15.
- Share of corporate equities and mutual fund shares, quarterly, Q3 1989 to Q2 2026:
  - Top 1%: `WFRBST01122` (https://fred.stlouisfed.org/series/WFRBST01122)
  - 90th to 99th percentiles: `WFRBSN09149` (https://fred.stlouisfed.org/series/WFRBSN09149)
  - 50th to 90th percentiles: `WFRBSN40176` (https://fred.stlouisfed.org/series/WFRBSN40176)
  - Bottom 50%: `WFRBSB50203` (https://fred.stlouisfed.org/series/WFRBSB50203)
- Q2 2026: top 1% 50.9%, next 9% 37.2%, middle 40% 11.4%, bottom 50% 0.6% (sums to 100.1% because of rounding in the source)
- Q3 1989: top 1% 42.8%
- Raw file: `data/raw/cycle 2/issue-10/fred_wealth_shares.csv`
- FRED dates each quarter by its first day (2026-04-01 = Q2 2026)

---

## Slide 8: THE FORECAST

### Clothing spending by income group (notebook 10.2)
- U.S. Bureau of Labor Statistics, Consumer Expenditure Surveys, via FRED. Pulled 2026-10-16.
- Annual, 1984 to 2024, by quintile of income before taxes:
  - Apparel and services: `CXUAPPARELLB0102M` (lowest 20%) to `CXUAPPARELLB0106M` (highest 20%)
  - Total spending: `CXUTOTALEXPLB0102M` to `CXUTOTALEXPLB0106M`
- Change in clothing spending, year before vs. lowest year after (not adjusted for inflation):
  - 2008 to 2010: lowest +1.2%, second +10.5%, middle -17.7%, fourth -17.0%, highest -13.3%
  - 2020: lowest -6.8%, second -30.8%, middle -17.5%, fourth -34.8%, highest -21.0%
- Lowest 20% clothing spending: $765 (2007), $818 (2019)
- Raw file: `data/raw/cycle 2/issue-10/fred_clothing_spending.csv`
- Limitations: averages per household include those who spend little by choice; the lowest-income group includes retirees and students; self-reported survey; annual and released months after the year ends

### Unemployment by education (notebook 10.1)
- U.S. Bureau of Labor Statistics, via FRED. Pulled 2026-10-15.
  - Less than a high school diploma, 25 and over: `LNS14027659` (https://fred.stlouisfed.org/series/LNS14027659)
  - Bachelor's degree and higher, 25 and over: `LNS14027662` (https://fred.stlouisfed.org/series/LNS14027662)
- April 2020 peak: 21.2% (no diploma) vs. 8.4% (bachelor's or higher)
- October 2025 is missing in both series: household survey data were not collected because of the federal government shutdown and will not be collected retroactively (U.S. Bureau of Labor Statistics, 2025, December 16, *The employment situation: November 2025*: https://www.bls.gov/news.release/archives/empsit_12162025.htm)
- Raw file: `data/raw/cycle 2/issue-10/fred_unemployment_education.csv`

### Recession shading (charts only)
- NBER-based recession indicator, `USREC`, via FRED: https://fred.stlouisfed.org/series/USREC

---

## Caption and context only (not on slides)

### Data, But Make It Fashion: other posts reviewed
- Men's shorts reel, 19 April 2026: https://www.instagram.com/reel/DXUTnD7DuFF/ . Claim: the hemline index "applies to menswear too"; S&P 500 growth as the economic measure.
- S&P 500 reel, 9 May 2026: https://www.instagram.com/reel/DYHtlOyOdxZ/ . On-screen S&P 500 up 2.36% over 5 days, compared with "this past week" of fashion styles.
- Elle (2024) profile, in which she describes herself as "a big believer" in the hemline index: https://www.aol.com/data-scientist-cracking-fashion-codes-130000984.html

---

## Checked and not used

- **"George Taylor, 1926"** as the origin of the hemline index: a misattribution repeated widely online, including in the 2010 paper's introduction. The primary source is Taylor (1929), above.
- **Erasmus School of Economics news pages:** press summaries; the paper and Het Financieele Dagblad are cited instead.
- **The 2010 study's forecast** of ankle-length skirts around 2011 to 2012: maxi skirt searches did rise from 2011, but the term itself was only just entering common use, so the timing proves nothing.
- **Searchversity and similar pages:** no named sources or studies.