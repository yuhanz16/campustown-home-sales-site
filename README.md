# Median Sale Price by College Town

## What this site is for

This site compares home prices across 18 college towns around 11 U.S. universities. It answers one question: **in which college towns is a typical home most and least expensive?** It is written for students, families, and university staff who are thinking about buying or renting near campus.

## Live site

https://yuhanz16.github.io/campustown-home-sales-site/

## Data notes

- **Source:** College-town home sales dataset v1.0, 35,442 sales dated March 2023 to March 2026.
- **Rows left out:** The 40 sales under $10,000 (including one at $0) are dropped as impossible prices, which leaves 35,402 sales. Sales over $5M are kept: the site reports medians, and a few extreme values barely move a median.
- **How the figure is defined:** Median `sale_price` per city, computed on the 35,402 kept sales and rounded to the nearest dollar.
- **No deduplication by address:** 66 rows share a street address, mostly separate condo units in State College. Each row is counted once by `listing_id`.
- **Columns not used:** `home_type` is unreliable (State College condos are labeled `SINGLE_FAMILY`). `list_date` is blank for up to 38% of sales in some cities, and those blanks are not random, so the site does not report days on market. `living_area_sqft` is 0 on 127 rows, so the site does not report price per square foot.

## City median sale prices

(keep the existing section as it is)

## Tools we used

- Claude (AI coding agent) to write the page and the data script
- Python 3 (standard library only) for `scripts/make_city_median_prices.py`
- Plain HTML, CSS, and JavaScript, with no chart library
- GitHub Pages and GitHub Actions for publishing

## Citation

(keep as it is)
