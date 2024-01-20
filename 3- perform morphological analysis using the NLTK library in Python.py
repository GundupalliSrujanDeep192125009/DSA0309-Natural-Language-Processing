Write program demonstrates how to perform morphological analysis using the NLTK library in Python.

PROGRAM :-

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
def morphological_analysis(text):
    words = word_tokenize(text)
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
    print("Original Words:", words)
    print("Stemmed Words:", stemmed_words)
    print("Lemmatized Words:", lemmatized_words)
if __name__ == "__main__":
    example_text = "The cats are running and jumping around."
    morphological_analysis(example_text)
