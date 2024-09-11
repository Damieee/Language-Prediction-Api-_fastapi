from app.models import load_model
from app.utils.text_cleaning import clean_text

def predict_language(sentence):
    svm, tf, label_encoder = load_model()
    cleaned_sentence = clean_text(sentence)
    transformed_sentence = tf.transform([cleaned_sentence])
    predicted_language = svm.predict(transformed_sentence)
    return label_encoder.inverse_transform(predicted_language)[0]
