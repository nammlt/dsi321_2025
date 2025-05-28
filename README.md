# DSI321_BT_Materials
Real-Time News Scraper for Alternative Construction Materials

## Project Overview
This repository contains a Prefect-based ETL pipeline that scrapes real-time Google News headlines related to alternative construction materials, stores the data in CSV format, and prepares it for basic machine learning analysis. The project simulates a data engineering and data analysis workflow from data ingestion to insight generation.

This project was developed as part of the DSI321 coursework and is designed to fulfill all technical and reporting requirements outlined in the assessment criteria.

## Repository Structure
DSI321/
├── Dockerfile.cli              # Dockerfile for Prefect Worker and CLI customization
├── docker-compose.yml          # Docker Compose file for running services (Prefect, PostgreSQL, etc.)
├── main.py                     # Main script for scraping news using Prefect flow (manual run version)
├── deploy.py                   # Show realtime data, visualize wordcloud and table of topic modeling on Streamlit
├── config_path.py              # Configuration file for paths and constants
├── requirements.txt            # Python dependencies required for the project
├── pyproject.toml              # Project configuration (for build systems like Poetry)
├── data/                       # Directory for storing collected data
│   └── scrap_data.csv          # Collected news articles from Google News RSS
└── README.md                   # Documentation file describing the project (this file)


## Technologies Used
- Python 3.13
- Docker + Docker Compose
- Prefect – Data orchestration and scheduling
- Feedparser – RSS Feed reader for news headlines
- Pandas, Matplotlib, Scikit-learn – For data analysis and ML

## Project Objective
To build a robust and scalable news scraping pipeline that helps track emerging trends in construction materials, particularly sustainable and alternative technologies. The output can help inform decisions in construction R&D, procurement, and material sourcing.

## 📊 Dataset Description
- >1,000 records collected
- Covers 24 hours using multiple keywords (e.g., "green building materials", "supply chain construction")
- 90%+ completeness
- Duplicates and object-type columns removed
- CSV format ready for ML pipelines

Schema sample:
| title               | link        | published           | fetched\_at               | keyword                  |
| ------------------- | ----------- | ------------------- | ------------------------- | ------------------------ |
| Green Bricks for... | http\://... | Sat, 25 May 2025... | 2025-05-25T13:42:00+00:00 | sustainable construction |

## Data Pipeline Workflow
1. Create data folder
2. Load existing data
3. Fetch RSS by keyword
4. Append to CSV

## Visualization (ตามรายวิชา DSI324)
- Wordcloud

## Machine Learning Analysis
- Topic Modeling

## Weekly Plan and Milestones
| Week | Task |
|---------|--------|
| Week 1  | Create repository dsi321, initial commit |
| Week 1–3 | Commit at least 5 times/week showing progress |
| Week 2–3 | Write this README (over 1,000 characters) |
| Week 3  | Collect 1,000+ records, ensure schema validity and completeness |
| Week 4  | Data cleaning: drop duplicates, validate types |
| Week 5  | Visualization + ML (Linear Regression) + final report |

## How to Run the Project
```bash
git clone ...
docker compose up --build


