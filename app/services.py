from app.models import svm, tf, label_encoder
from app.utils.text_cleaning import clean_text

def predict_language(sentence):
    cleaned_sentence = clean_text(sentence)
    transformed_sentence = tf.transform([cleaned_sentence])
    predicted_language = svm.predict(transformed_sentence)
    return label_encoder.inverse_transform(predicted_language)[0]
