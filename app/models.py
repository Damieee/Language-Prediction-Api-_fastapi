import joblib
import os
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import pandas as pd
from utils.text_cleaning import clean_text

# Initialize variables
svm = None
tf = None
label_encoder = None

# Load and preprocess data
def pre_process_data():
    df = pd.read_csv("./app/static/dataset.csv")
    df = df.drop_duplicates(subset='Text').dropna(subset=['Text']).reset_index(drop=True)
    df["Text"] = df["Text"].apply(clean_text)

    label_encoder = LabelEncoder()
    df["Encoded language"] = label_encoder.fit_transform(df["language"])

    X = df["Text"]
    Y = df["Encoded language"]

    tf = TfidfVectorizer()
    train_data = tf.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(train_data, Y, test_size=0.2, random_state=42)
    return X_train, X_test, Y_train, Y_test, tf, label_encoder

# Train the model
def train_model(X_train, Y_train):
    svm = SVC()
    svm.fit(X_train, Y_train)
    joblib.dump(svm, "./app/static/svm_model.pkl")
    return svm

# Load model
def load_model():
    global svm, tf, label_encoder
    if os.path.exists("./app/static/svm_model.pkl"):
        svm = joblib.load("./app/static/svm_model.pkl")
        tf = joblib.load("./app/static/tfidf_vectorizer.pkl")
        label_encoder = joblib.load("./app/static/label_encoder.pkl")
    else:
        X_train, X_test, Y_train, Y_test, tf, label_encoder = pre_process_data()
        svm = train_model(X_train, Y_train)
        joblib.dump(tf, "./app/static/tfidf_vectorizer.pkl")
        joblib.dump(label_encoder, "./app/static/label_encoder.pkl")
