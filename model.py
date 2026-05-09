import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from preprocess import clean_text
data = pd.read_csv("data.csv")
data['cleaned'] = data['feedback'].apply(clean_text)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['cleaned'])
y = data['sentiment']

model = LogisticRegression()
model.fit(X, y)

def predict_feedback(text):
    cleaned = clean_text(text)
    vector = vectorizer.transform([cleaned])
    return model.predict(vector)[0]
