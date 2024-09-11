import re
import unicodedata
from bs4 import BeautifulSoup

def clean_text(text):
    if "<" in text:
        text = BeautifulSoup(text, 'html.parser').get_text()
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
