# scrape_news_csv_prefect.py
# Prefect-enhanced script to scrape DuckDuckGo news articles and save to CSV

from prefect import flow, task
import csv
from duckduckgo_search import DDGS


@task
def fetch_news(
    keywords: str,
    region: str = "wt-wt",
    safesearch: str = "moderate",
    timelimit: str | None = None,
    max_results: int | None = 20,
) -> list[dict[str, str]]:
    with DDGS() as ddgs:
        results = ddgs.news(
            keywords,
            region=region,
            safesearch=safesearch,
            timelimit=timelimit,
            max_results=max_results,
        )
    return results


@task
def save_to_csv(articles: list[dict[str, str]], csv_file: str):
    fieldnames = ["date", "title", "content"]
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


@flow
def duckduckgo_news_pipeline(topic: str = "construction materials", max_results: int = 20):
    articles = fetch_news(topic, max_results=max_results)
    save_to_csv(articles, "news_alternative_materials.csv")


if __name__ == "__main__":
    duckduckgo_news_pipeline()
