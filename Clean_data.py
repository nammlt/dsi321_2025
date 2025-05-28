import pandas as pd
from nltk.corpus import stopwords
import nltk
import re

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# custom stopwords
custom_stopwords = {
    # News
    "news", "update", "latest", "breaking", "read", "watch", "live", "video",
    "media", "outlet", "journal", "articles", "headline", "source", "coverage", "information",
    "say", "says", "said", "report", "reports", "reported",
    "announced", "introduced", "launch", "revealed", "expects",
    "statements", "highlighted", "unveiled", "discussed", "talk", "asks", "request",
    "today", "week", "now",
    "company", "group", "corporation", "organization", "firm", "business",
    "ltd", "inc", "co", "plc", "association", "partner", "entity", "owner",
    "market", "investment", "opportunity", "cost", "revenue",
    "u.s", "china", "europe", "asia", "india", "africa", "japan", "korea",
    "middle", "east", "north", "america", "latin",
    "province", "city", "region", "district", "country",
    "is", "will", "with", "for", "by", "on", "at", "in", "to",
    "and", "or", "that", "as", "during", "through", "along",
    "from", "above", "around", "of", "between", "under", "over",
    "products", "services", "materials", "solutions", "technologies", "construction", "building",
    "supply", "demand", "development", "design", "researchgate"
    "engineering", "value", "growth", "trend", "innovation", "technology",
    "cement", "industry", "s", "weak", "strat", "new"
    "smm", "made", "engineering", "sale", "travis", "perkins", "finding",
    "material", "insights", "german", "researchers", "prices", "start", "new"
    "driven", "forecast", "analysis", "launched", "study", "data", "reporting", "trends"
    "usd", "billion", "million", "cagr", "year", "years", "2030", "2035", "2025", "2031", "research"
}
stop_words.update(custom_stopwords)

# News Organiztion and useless word
remove_words = [
    "BBC", "DW", "ResearchGate", "Dezeen", "HowStuffWorks",
    "Power Line Magazine", "ET EnergyWorld", "trend", "promoting", "about", "About", "and", "use"
]

# Function
def remove_companies(text):
    for word in remove_words:
        text = re.sub(rf"\b{re.escape(word)}\b", "", text)
    return re.sub(r"\s{2,}", " ", text).strip()

# Load CSV
df = pd.read_csv("data/scrap_data.csv", header=0, encoding='utf-8-sig')
print("📄 Columns in file:", df.columns.tolist())

# Remove rows no title or keyword
df = df.dropna(subset=["title", "keyword"])

# Processing
filtered_rows = []
for _, row in df.iterrows():
    title = str(row["title"]).lower()
    title = remove_companies(title)  # Delete News Organiztion after do lowercase
    keyword = row["keyword"]

    words = title.split()
    filtered = [word for word in words if word not in stop_words and word.isalpha()]
    filtered_title = " ".join(filtered)

    filtered_rows.append({
        "cleaned_title": filtered_title,
        "keyword": keyword
    })

# Build New File
filtered_df = pd.DataFrame(filtered_rows)
filtered_df.to_csv("data/filtered_by_topic.csv", index=False, encoding="utf-8")
print("Successful File")

# object to string for prevent 'object' dtype
for col in filtered_df.columns:
    if filtered_df[col].dtype == 'object':
        filtered_df[col] = filtered_df[col].astype(str)

# Remove Duplicates (based on all columns)
filtered_df = filtered_df.drop_duplicates()

# Scan dtype (No object should be str)
print("\nประเภทข้อมูลหลังแปลง:")
print(filtered_df.dtypes)

# New Csv
filtered_df.to_csv("data/filtered_by_topic_cleaned.csv", index=False, encoding="utf-8")
print("บันทึกไฟล์ที่ลบ object และข้อมูลซ้ำเรียบร้อยแล้ว")
