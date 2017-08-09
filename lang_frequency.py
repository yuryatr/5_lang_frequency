import os
import re
import sys
import argparse
from collections import Counter


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_most_frequent_words(text, show_words_length=10):
    words = re.findall(r'\w+', text.lower())
    return Counter(words).most_common(show_words_length)

def get_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('--path', action='store', dest='filepath',
                        help='Path to text file you want to calculate the frequency of words.')
    return args.parse_args()

if __name__ == '__main__':

    arguments = get_arguments()
    filepath = arguments.filepath

    if not os.path.exists(filepath):
        print('Error: File "{}" does not exists.'.format(filepath))
        sys.exit(1)
    
    text = load_data(filepath)
    show_words_length = 10
    
    most_frequent_words = get_most_frequent_words(text, show_words_length)
    for word, count in most_frequent_words:
        print('{:5} - {}'.format(word, count))








