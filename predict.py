from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
from bs4 import BeautifulSoup
import re
import unicodedata
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib
import os

# Define FastAPI app
app = FastAPI()

# Function to clean text
def clean_text(text):
    # Remove HTML tags if present
    if "<" in text:
        text = BeautifulSoup(text, 'html.parser').get_text()
    # Remove URL addresses
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    # Remove accented characters
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Remove punctuation and non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    text = ' '.join(filtered_words)
    return text

def pre_process_data():
    # Load the dataset
    df = pd.read_csv("./dataset.csv")

    # Drop duplicates and null values
    df = df.drop_duplicates(subset='Text').dropna(subset=['Text']).reset_index(drop=True)

    # Clean the text
    df["Text"] = df["Text"].apply(clean_text)

    # Label Encoding: Convert the "language" feature using label encoding
    label_encoder = LabelEncoder()
    df["Encoded language"] = label_encoder.fit_transform(df["language"])

    # Define features (X) and target (Y)
    X = df["Text"]
    Y = df["Encoded language"]

    # Initialize TfidfVectorizer
    tf = TfidfVectorizer()

    # Transform the text data
    train_data = tf.fit_transform(X)

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(train_data, Y, test_size=0.2, random_state=42)
    return X_train, X_test, Y_train, Y_test, tf, label_encoder

def train_model(X_train, Y_train):

    svm = SVC()
    svm.fit(X_train, Y_train)
    # Save the trained model to disk
    joblib.dump(svm, "svm_model.pkl")

# Train the SVM model only if the trained model is not already saved
if not os.path.exists("svm_model.pkl"):
    X_train, X_test, Y_train, Y_test, tf, label_encoder = pre_process_data()
    train_model(X_train, Y_train)
    # Save the trained model and associated objects to disk
    joblib.dump(tf, "tfidf_vectorizer.pkl")
    joblib.dump(label_encoder, "label_encoder.pkl")
else:
    # Load the trained model and associated objects from disk
    svm = joblib.load("svm_model.pkl")
    tf = joblib.load("tfidf_vectorizer.pkl")
    label_encoder = joblib.load("label_encoder.pkl")

# Function to predict language
def predict_language(sentence):
    # Clean the input sentence
    cleaned_sentence = clean_text(sentence)
    
    # Transform the cleaned text using TfidfVectorizer
    transformed_sentence = tf.transform([cleaned_sentence])
    
    # Predict the language of the transformed text
    predicted_language = svm.predict(transformed_sentence)
    
    # Inverse transform the predicted label to get the language name
    predicted_language_name = label_encoder.inverse_transform(predicted_language)
    
    return predicted_language_name[0]

# Define request body model
class SentenceInput(BaseModel):
    sentence: str

# Define API route for language prediction
@app.post("/predict_language/")
async def get_language(input_data: SentenceInput):
    sentence = input_data.sentence
    predicted_language = predict_language(sentence)
    return {"sentence": sentence, "predicted_language": predicted_language}

# Run the FastAPI app using Uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
