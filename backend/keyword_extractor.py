import argparse
from text_processor import process_text, get_keywords

#This script uses the argparse module to parse command-line arguments. The script takes a required argument corpus, which is the path to the corpus folder containing the text files to be processed. The script also takes an optional argument --stop-words, which is the path to a file containing a list of stop words to be used during keyword extraction.

#The script processes each file in the corpus by calling the process_text and get_keywords functions from the text_processor module, and concatenates the resulting list of keywords. The script then sorts the keywords by frequency in descending order, and prints the top 10 keywords and their frequencies to the console.

#Note that this implementation assumes that the corpus contains only text files with the .txt extension. If your corpus contains files with other extensions, you will need to modify the glob pattern accordingly.

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Extract keywords from a corpus of text files.')
    parser.add_argument('corpus', help='path to the corpus folder')
    parser.add_argument('--stop-words', help='path to the stop words file')
    args = parser.parse_args()

    # Process each file in the corpus
    keywords = []
    for file_path in Path(args.corpus).glob('*.txt'):
        sentences = process_text(file_path)
        keywords += get_keywords(sentences, args.stop_words)

    # Sort the keywords by frequency in descending order
    sorted_keywords = sorted(keywords, key=lambda x: x[1], reverse=True)

    # Print the top 10 keywords
    for keyword, count in sorted_keywords[:10]:
        print(f'{keyword}: {count}')
