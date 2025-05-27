# DSI321_BT_Materials
The project includes a Web Cloud built with Streamlit to visualize the topics by scraping real-time news on sustainable construction materials topics from Google News RSS.

## ✅ Project Compliance & Evaluation Criteria

This project is designed to meet the core evaluation criteria of DSI321, including:

- The news scraping pipeline is scheduled to run every 15 minutes and is expected to collect **at least 1,000 news records** over the data collection period, covering a continuous **24-hour time span**.

- The dataset schema is structured and consistent, containing only relevant fields with no `object` types or duplicate entries.

- All collected data is validated to ensure **over 90% completeness**.

- The repository includes **more than 15 commits across 3 weeks**, ensuring consistent development progress.

- The **README file exceeds 1,000 characters**, covering project overview, usage, tools, and benefits in detail.

- A **Streamlit dashboard** is provided for visualizing news trends and word cloud generation.

- (Optional) A simple Machine Learning model such as **Linear Regression** can be integrated for further analysis to align with DSI324 objectives.


## Project Overview
●   Scrapes real-time news about alternative construction materials from Google News RSS.

●   Uses Prefect 2.0 to manage workflows and schedule scraping every 15 minutes.

●   Stores news articles as partitioned Parquet files in lakeFS, enabling version-controlled data lake functionality.

●   Visualizes results in a Streamlit dashboard with a Word Cloud to highlight the most frequently mentioned topics."

## Benefits of This Project

#### Industry Relevance

●   Tracks real-time developments in alternative and sustainable construction materials.

●   Helps businesses, researchers, or developers stay updated on market trends, supply chain issues, and innovation in the construction sector.


#### Insight Generation

●   Uses a Word Cloud visualization to reveal the most-discussed topics across news sources.

●   Enables quick understanding of public focus areas, such as "green building", "material shortage", or "price increases".


#### Decision Support

●   Provides structured, timestamped data that can support decision-making for:

●   Material procurement strategies

●   ESG-related reporting or planning

●   Marketing and communication alignment"

## Automation & Efficiency
●   Automatically runs every 15 minutes with Prefect 2.0 scheduling.

●   Stores data in lakeFS for easy retrieval, version control, and reproducibility — no manual scraping or data loss.

## Tool used

●   Web Scraping: feedparser to fetch news via Google News RSS (no login or Selenium required)

●   Data Processing: pandas for data manipulation and transformation

●   Data Storage: lakeFS (local S3-compatible object store) with Parquet files, partitioned by year/month/day

●   Orchestration: Prefect 2.0 for workflow management and scheduled scraping every 15 minutes

●   Visualization: Streamlit dashboard with matplotlib and WordCloud to display most-discussed topics

●   Text Cleaning: re, string, nltk.stopwords for title preprocessing

●   Environment Management: Docker Compose for multi-service setup (Prefect Server, lakeFS, 
PostgreSQL, CLI, Worker)

●   Version Control & Deployment: Git, GitHub (manual deploy or CLI-based flow registration)

## Prepare & Run the Project
#### 1. Create and activate a virtual environment

```bash
    python -m venv .venv
    .venv\Scripts\activate
    source .venv/bin/activate
```

Install dependencies:

```bash
    prepip install -r requirements.txt
```

#### 2. Start Docker Services (Prefect + lakeFS + DB)

```bash
    docker compose --profile server up -d     # Start Prefect server & database
    docker compose --profile worker up -d     # Start Prefect worker
    docker compose --profile cli run cli      # (Optional) Get a shell in CLI container
```

#### 3. Deploy or Run the Scraping Flow

To deploy the Prefect flow that runs every 15 minutes:

```bash
    python main_2.py
```

Or to run it manually (once):

```bash
    python main_2.py
```

#### 4. Launch the Streamlit Dashboard

```bash
    streamlit run dashboard.py
```

#### 5. View Prefect UI

```bash
Open your browser and go to localhost,

then you can monitor scheduled runs and logs.
```

## Author
"Thanyarat Thirathanapornanan 6524650048"


