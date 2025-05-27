import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Download deleted stopwords and News organization
df = pd.read_csv("data/filtered_by_topic.csv")

# Join all column cleaned_title
all_text = " ".join(df["cleaned_title"].dropna().astype(str))

# Word Cloud
wordcloud = WordCloud(
    width=1000,
    height=600,
    background_color='white',
    max_words=200,
    colormap='viridis',      
    collocations=False       
).generate(all_text)

# Result
plt.figure(figsize=(12, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Construction Material Topics", fontsize=16)
plt.show()
