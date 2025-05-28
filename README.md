# DSI321_BT_Materials
Real-Time News Scraper for Alternative Construction Materials

## Project Overview
This repository contains a Prefect-based ETL pipeline that scrapes real-time Google News headlines related to alternative construction materials, stores the data in CSV format, and prepares it for basic machine learning analysis. The project simulates a data engineering and data analysis workflow from data ingestion to insight generation.

This project was developed as part of the DSI321 coursework and is designed to fulfill all technical and reporting requirements outlined in the assessment criteria.

## Repository Structure
```bash
DSI321/
├── Dockerfile.cli              # Dockerfile for Prefect Worker and CLI customization
├── docker-compose.yml          # Docker Compose file for running services (Prefect, PostgreSQL, etc.)
├── main.py                     # Main script for scraping news using Prefect flow (manual run version)
├── app.py                      # Streamlit app to visualize Word Cloud and Topic Modeling
├── config_path.py              # Configuration file for paths and constants
├── requirements.txt            # Python dependencies required for the project
├── pyproject.toml              # Project configuration (for Poetry or other build systems)
├── data/                       # Folder containing collected data
│   └── scrap_data.csv          # Collected news articles from Google News RSS
└── README.md                   # This file - documentation of the project
```

## Technologies Used
- Python 3.13
- Docker + Docker Compose
- Prefect – Data orchestration and scheduling
- Feedparser – RSS Feed reader for news headlines
- Pandas, Matplotlib, Scikit-learn – For data analysis and ML

## Project Objective
To build a robust and scalable news scraping pipeline that helps track emerging trends in construction materials, particularly sustainable and alternative technologies. The output can help inform decisions in construction R&D, procurement, and material sourcing.

## Dataset Description
- ≥1,000 records collected
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

## Visualization (DSI324)
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
This project includes a data pipeline to collect news via RSS feeds, store them, and visualize them with a Streamlit web app. It uses Docker, Prefect, and optionally LakeFS for versioned data.

### Prerequisites
- Docker and Docker Compose installed
- Python 3.13 (for local runs without Docker)
- poetry or pip (if running Python manually)
- Internet access (to fetch news via RSS)

1. Clone the repository
```bash
git clone https://github.com/yourusername/dsi321.git
cd dsi321
```

2. Start services
```bash 
docker compose --profile server up -d
```

3. Start the Prefect Worker
```bash
docker compose --profile worker up -d
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Run the scraper flow
```bash
python main.py
```

6. Run the Streamlit web app
```bash
streamlit run app.py
```
## Related Courses
DSI321 – BIG DATA INFRASTRUCTURE
DSI324 – PRACTICAL DATA GOVERNANCE PROJECT

## Author
Kodchaporn Sittiphaisal
3rd Year | BSc Data Science and Innovation | Thammasat University