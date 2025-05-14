from prefect import flow, task
import feedparser
import csv

@task
def fetch_news(query: str) -> list:
    rss_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(rss_url)
    return feed.entries

@task
def save_news_to_csv(entries: list, filename: str = "google_news_results.csv"):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Link", "Published", "Summary"])
        for entry in entries:
            writer.writerow([entry.title, entry.link, entry.published, entry.summary])

@task
def print_news(entries: list):
    for entry in entries:
        print("Title:", entry.title)
        print("Link:", entry.link)
        print("Published:", entry.published)
        print("Summary:", entry.summary)
        print("-----------")

@flow
def news_pipeline(query: str = "alternative construction materials"):
    entries = fetch_news(query)
    print_news(entries)
    save_news_to_csv(entries)

# เรียกใช้ flow
if __name__ == "__main__":
    news_pipeline()
