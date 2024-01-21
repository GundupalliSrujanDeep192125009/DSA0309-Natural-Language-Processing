Use the Porter Stemmer algorithm to perform word stemming on a list of words using python libraries.

PROGRAM :-

from nltk.stem import PorterStemmer

def perform_stemming(words):
    porter_stemmer = PorterStemmer()
    stemmed_words = [porter_stemmer.stem(word) for word in words]
    return stemmed_words

if __name__ == "__main__":

    words_to_stem = ['running', 'jumps', 'swimming', 'happiness', 'running']
    stemmed_words = perform_stemming(words_to_stem)

    for original, stemmed in zip(words_to_stem, stemmed_words):
        print(f"Original: {original} \t Stemmed: {stemmed}")
