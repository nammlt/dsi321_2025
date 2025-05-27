import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

nltk.download("punkt")
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in string.punctuation]
    tokens = [word for word in tokens if word not in stop_words]
    return tokens

processed_docs = [preprocess(doc) for doc in documents]
from gensim.corpora.dictionary import Dictionary
from gensim.models.ldamodel import LdaModel

# dictionary and corpus
dictionary = Dictionary(processed_docs)
corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

lda_model = LdaModel(
    corpus=corpus,
    id2word=dictionary,
    num_topics=5,  # เลือกจำนวนหัวข้อ
    random_state=42,
    passes=10,
    alpha='auto',
    per_word_topics=True
)

for idx, topic in lda_model.print_topics(-1):
    print(f"Topic {idx}: {topic}")
