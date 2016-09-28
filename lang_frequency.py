import argparse

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as error:
        return error

def getord(start, end):
    return [x for x in range(start, end + 1)]

EXCLUDE_CHARACTERS_ORD = [9, 10, 13] \
    + getord(32, 47) + getord(58, 64) \
    + getord(91, 96) + getord(123, 126) \
    + getord(161, 191) + [8211]

def mystrip(word=''):
    if not word:
        return None
    if ord(word[:1]) in EXCLUDE_CHARACTERS_ORD:
        word = word.strip(word[:1])
        return mystrip(word)
    if ord(word[len(word)-1:]) in EXCLUDE_CHARACTERS_ORD:
        word = word.strip(word[len(word)-1:])
        return mystrip(word)
    return word

def get_most_frequent_words(text, word_length=10):
    words = {}
    word = ''
    for symbol in text:
        symbol_ord = ord(symbol.lower())
        if symbol_ord in [10, 13, 32] and word != '':
            word = mystrip(word)
            if word is not None:
                words[word] = words.get(word, 0) + 1
            word = ''
        else:
            if symbol_ord not in [9, 10, 13, 32]:
                word += symbol.lower()
    return list(sorted(words.items(), key=lambda x: x[1], reverse=True))[:word_length]

def get_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('--path', action='store', dest='filepath',
                        help='Path to text file you want to calculate the frequency of words.')
    return args.parse_args()

if __name__ == '__main__':
    arguments = get_arguments()
    data = load_data(arguments.filepath)
    if isinstance(data, str):
        word_length = 10
        most_frequent_words = get_most_frequent_words(data, word_length)
        print(most_frequent_words)
    else:
        print(data)
