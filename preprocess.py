import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


def preprocess_text(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenization
    tokens = word_tokenize(text)

    # Stopword removal
    stop_words = set(stopwords.words('english'))

    filtered_words = []

    for word in tokens:
        if word not in stop_words:
            filtered_words.append(word)

    # Stemming
    stemmer = PorterStemmer()

    stemmed_words = []

    for word in filtered_words:
        stemmed_words.append(stemmer.stem(word))

    # Convert list to sentence
    processed_text = ' '.join(stemmed_words)

    return processed_text


# Test
question = "How can I apply for admission?"

result = preprocess_text(question)

print("Original Question:")
print(question)

print("\nProcessed Question:")
