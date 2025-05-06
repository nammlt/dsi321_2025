# scrape_mediastack_multiple_topics.py
# Script to scrape Media Stack API for multiple topics and save results to a single CSV

import csv
import requests
from typing import List, Dict


def fetch_mediastack_news(
    query: str,
    access_key: str,
    languages: str = "en",
    countries: str = "us,gb",
    limit: int = 50
) -> List[Dict]:
    """
    ดึงข่าวจาก Media Stack API ของหัวข้อหนึ่ง

    Args:
        query: คำค้น (topic)
        access_key: API Access Key จาก mediastack.com
        languages: รหัสภาษา (comma-separated)
        countries: รหัสประเทศ (comma-separated)
        limit: จำนวนผลลัพธ์สูงสุด (max 100)

    Returns:
        List ของ dict แต่ละข่าวมี keys เช่น published_at, title, url, description, source
    """
    url = "http://api.mediastack.com/v1/news"
    params = {
        "access_key": access_key,
        "keywords": query,
        "languages": languages,
        "countries": countries,
        "limit": limit,
        "sort": "published_desc"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("data", [])


def scrape_topics_to_csv(
    topics: List[str],
    access_key: str,
    output_file: str = "media_multiple_topics.csv",
    languages: str = "en",
    countries: str = "us,gb",
    limit: int = 100
) -> None:
    """
    Scrape multiple topics and save all articles to a single CSV with an extra 'topic' column.

    Args:
        topics: List ของคำค้น (topics)
        access_key: API Access Key
        output_file: ชื่อไฟล์ CSV ที่จะบันทึก
        languages: รหัสภาษา
        countries: รหัสประเทศ
        limit: จำนวนผลลัพธ์ต่อ topic
    """
    fieldnames = ["topic", "published_at", "title", "url", "description", "source_name"]

    with open(output_file, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for topic in topics:
            print(f"Scraping topic: {topic}")
            articles = fetch_mediastack_news(topic, access_key, languages, countries, limit)
            for art in articles:
                writer.writerow({
                    "topic": topic,
                    "published_at": art.get("published_at", ""),
                    "title": art.get("title", "").strip(),
                    "url": art.get("url", ""),
                    "description": art.get("description", "").strip(),
                    "source_name": art.get("source", "")
                })

    print(f"Saved articles for {len(topics)} topics to {output_file}")


if __name__ == "__main__":
    ACCESS_KEY = "13f32e3ec9093d6661b1b9eb16769c85"  # ใส่ API Access Key ของคุณ
    # ระบุหลายหัวข้อที่ต้องการ
    topics = [
        "construction materials",
        "construction",
        "materials",
        "alternative materials for construction",
        "sustainable building materials",
        "recycled concrete",
        "bamboo architecture",
        "hempcrete",
        "rammed earth construction",
        "fiber-reinforced polymers",
        "self-healing concrete",
        "phase change materials for insulation",
        "3D printed concrete"
    ]
    scrape_topics_to_csv(
        topics,
        ACCESS_KEY,
        output_file="media_multiple_topics.csv",
        languages="en",
        countries="us,gb",
        limit=30
    )
