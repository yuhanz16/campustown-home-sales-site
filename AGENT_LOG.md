# Agent log

Add a dated entry each time you work with your AI coding agent, with the newest entry at the bottom. Each entry records what you asked the agent, what it produced, and what you checked or changed. Paste your key prompts in exactly as you typed them. Include at least one time the agent got something wrong, and how you caught it.

Copy this outline for each entry:

```markdown
## YYYY-MM-DD: What you worked on

- **Asked:** "Paste your prompt here."
- **Agent produced:** What it made or changed.
- **Checked or changed:** How you checked it, and what you fixed.
```

## 2026-11-06: Replace the placeholder page with city median sale prices (Claude Code)

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then replace the placeholder index.html with a page that shows the median sale price for each city, computed from data/college_town_home_sales.csv. Leave out sales under $10,000 and state that rule on the page."
- **Agent produced:** A script, `scripts/make_city_median_prices.py`, that drops the 40 sales under $10,000 (keeping 35,402) and writes `data/city_median_sale_prices.csv`. A new `index.html` that loads that file and shows a table of all 18 cities, sorted by median, with sales counts and the $10,000 rule stated. A README section on how to rerun the script. It pushed to the branch `claude/pensive-turing-9cc961` but did not open a pull request.
- **Checked or changed:** The agent cross-checked its medians against a separate pandas calculation and loaded the page in a headless browser. I noticed Ann Arbor's median ($572,000) differs from the description sheet ($571,000); the agent explained the sheet uses a $1,000 cutoff instead of $10,000. I opened PR #1 and merged it into main so the site would publish.

## 2026-11-06: Same task given to GitHub Copilot

- **Asked:** "Read AGENTS.md and docs/data_description_sheet.md first. Then replace the placeholder index.html with a page that shows the median sale price for each city, computed from data/college_town_home_sales.csv. Leave out sales under $10,000 and state that rule on the page."
- **Agent produced:** No changes. Copilot found that the page and script from the Claude Code session already did this, and re-checked all 18 cities and the 35,402 qualifying sales against the source CSV.
- **Checked or changed:** I confirmed it didn't overwrite or duplicate the existing work. This showed me that a second agent can re-check the first agent's numbers.

## 2026-11-06: Add a bar chart of city medians (GitHub Copilot)

- **Asked:** I sent only a screenshot (image.png), with no text. Then: "Create pull request"
- **Agent produced:** A horizontal bar chart above the existing table in `index.html`. It uses the same `city_median_sale_prices.csv`, orders cities from highest to lowest median, and adds no chart library. The table and the $10,000 rule are unchanged. For the PR, it noticed the change was sitting on `main`, moved it to a feature branch, committed, pushed, and opened PR #2, "Add city median price bar chart".
- **Checked or changed:** Copilot told me to "open the site in a browser" to check the chart, but the live site publishes only from `main`, so the chart couldn't appear there until the PR was merged. This was the agent's mistake: its check instruction didn't work yet. I merged PR #2, then checked on the live site that the new bar chart sits above the original table. I also compared my site with the instructor's example screenshot on Canvas to confirm the content matches.
