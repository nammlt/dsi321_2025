import feedparser

# หัวข้อที่คุณสนใจ เช่น "Alternative construction materials"
query = "alternative construction materials"
rss_url = f"https://news.google.com/rss/search?q={query.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"

# ดึง RSS Feed
feed = feedparser.parse(rss_url)

# แสดงข่าวที่ได้
for entry in feed.entries:
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("Published:", entry.published)
    print("Summary:", entry.summary)
    print("-----------")

import csv

with open('google_news_results.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Link", "Published", "Summary"])
    for entry in feed.entries:
        writer.writerow([entry.title, entry.link, entry.published, entry.summary])