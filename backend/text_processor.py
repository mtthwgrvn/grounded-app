import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer

#This module provides two functions:

#process_text(file_path): This function takes a file path as input, reads the text from the file, and preprocesses it by replacing newlines and other white space with spaces, and tokenizing the text into sentences using the sent_tokenize function from NLTK. The function returns a list of preprocessed sentences.

#get_keywords(sentences, stop_words_file=None): This function takes a list of preprocessed sentences as input, and extracts keywords from them. The function removes stop words and punctuation from the words in the sentences, and stems the remaining words using the Porter stemmer from NLTK. The function then counts the frequency of each word, sorts the words by frequency in descending order, and returns a list of (word, count) tuples representing the keywords and their frequencies.

#The stop_words_file parameter is optional, and if specified, the function will load the stop words from the given file instead of using the default stop words from NLTK.

def process_text(file_path):
    """Processes the text in the given file and returns a list of sentences."""
    with open(file_path, 'r') as f:
        text = f.read()

    # Replace newlines and other white space with spaces
    text = re.sub(r'\s+', ' ', text)

    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    return sentences

def get_keywords(sentences, stop_words_file=None):
    """Extracts keywords from the given list of sentences and returns a list of (keyword, count) tuples."""
    # Load the stop words
    if stop_words_file is not None:
        with open(stop_words_file, 'r') as f:
            stop_words = set(f.read().splitlines())
    else:
        stop_words = set(stopwords.words('english'))

    # Create a stemmer
    stemmer = PorterStemmer()

    # Tokenize and preprocess each sentence
    words = []
    for sentence in sentences:
        # Tokenize the sentence into words
        tokens = word_tokenize(sentence)

        # Remove stop words and punctuation, and stem the remaining words
        for token in tokens:
            if token.lower() not in stop_words and token.isalpha():
                words.append(stemmer.stem(token.lower()))

    # Count the frequency of each word
    word_counts = Counter(words)

    # Sort the words by frequency in descending order
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    return sorted_words

