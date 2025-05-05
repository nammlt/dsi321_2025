# scrape_news_csv.py
# Script to scrape DuckDuckGo news articles on a specific topic and save to CSV

import csv
from duckduckgo_search import DDGS


def news(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: str | None = None,
    max_results: int | None = None,
) -> list[dict[str, str]]:
    """DuckDuckGo news search. Query params: https://duckduckgo.com/params.

    Args:
        keywords: keywords for query.
        region: wt-wt, us-en, uk-en, ru-ru, etc. Defaults to "wt-wt".
        safesearch: on, moderate, off. Defaults to "moderate".
        timelimit: d, w, m. Defaults to None.
        max_results: max number of results. If None, returns results only from the first response. Defaults to None.

    Returns:
        List of dictionaries with news search results.
    """
    with DDGS() as ddgs:
        # Use the news() method to fetch news results
        results = ddgs.news(
            keywords,
            region=region,
            safesearch=safesearch,
            timelimit=timelimit,
            max_results=max_results,
        )
    return results


def main():
    topic = "construction materials"
    # Fetch up to 20 results
    articles = news(topic, max_results=20)

    # Define CSV filename and headers
    csv_file = "news_alternative_materials.csv"
    fieldnames = ["date", "title", "content"]

    # Write results to CSV
    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles:
            writer.writerow({
                "date": article.get("date", ""),
                "title": article.get("title", ""),
                "content": article.get("body", ""),
            })

    print(f"Saved {len(articles)} articles to {csv_file}")


if __name__ == "__main__":
    main()
