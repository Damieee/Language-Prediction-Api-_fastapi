import joblib
import os

# Initialize variables
svm = None
tf = None
label_encoder = None


# Load model
def load_model():
    global svm, tf, label_encoder
    if os.path.exists("./app/static/svm_model.pkl"):
        svm = joblib.load("./app/static/svm_model.pkl")
        tf = joblib.load("./app/static/tfidf_vectorizer.pkl")
        label_encoder = joblib.load("./app/static/label_encoder.pkl")
        return svm, tf, label_encoder
    else:
        return {"Message": "No Prediction Model. Run Notebook for training"}
        # X_train, X_test, Y_train, Y_test, tf, label_encoder = pre_process_data()
        # svm = train_model(X_train, Y_train)
        # joblib.dump(tf, "./app/static/tfidf_vectorizer.pkl")
        # joblib.dump(label_encoder, "./app/static/label_encoder.pkl")
