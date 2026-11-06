"""Write data/city_median_sale_prices.csv: the median sale price for each city.

Reads data/college_town_home_sales.csv (never edits it) and applies one rule:
sales under MIN_SALE_PRICE dollars are left out. Every row kept counts once,
keyed by listing_id, and no addresses are deduplicated.

Run from the repository root:

    python3 scripts/make_city_median_prices.py

Uses only the Python standard library.
"""

import csv
import statistics
from collections import defaultdict
from pathlib import Path

MIN_SALE_PRICE = 10_000  # sales below this many dollars are left out

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_sale_prices.csv"


def main() -> None:
    prices_by_city = defaultdict(list)
    sales_read = 0
    left_out = 0

    with SOURCE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            sales_read += 1
            price = int(row["sale_price"])  # every value is a whole number in this file
            if price < MIN_SALE_PRICE:
                left_out += 1
                continue
            prices_by_city[(row["city"], row["state"])].append(price)

    results = []
    for (city, state), prices in prices_by_city.items():
        results.append({
            "city": city,
            "state": state,
            "sales": len(prices),
            "median_sale_price": statistics.median(prices),
        })
    results.sort(key=lambda r: r["median_sale_price"], reverse=True)

    with OUTPUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow(["city", "state", "sales", "median_sale_price"])
        for r in results:
            writer.writerow([r["city"], r["state"], r["sales"], f'{r["median_sale_price"]:.1f}'])

    kept = sales_read - left_out
    print(f"Read {sales_read} sales from {SOURCE.name}")
    print(f"Left out {left_out} sales under ${MIN_SALE_PRICE:,}; kept {kept}")
    print(f"Wrote {len(results)} cities to {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
