import re
import argparse
from collections import Counter

# The symbols of the word are excluded.
# {ord('symbol'): 'symbol'}
_EXCLUDE_SYMBOLS_ALL = {
    9: '\t',
    10: '\n',
    13: '\r',
    32: ' ',
    33: '!',
    34: '"',
    35: '#',
    36: '$',
    37: '%',
    38: '&',
    39: "'",
    40: '(',
    41: ')',
    42: '*',
    43: '+',
    44: ',',
    45: '-',
    46: '.',
    47: '/',
    58: ':',
    59: ';',
    60: '<',
    61: '=',
    62: '>',
    63: '?',
    64: '@',
    91: '[',
    92: '\\',
    93: ']',
    94: '^',
    95: '_',
    96: '`',
    123: '{',
    124: '|',
    125: '}',
    126: '~',
    161: '¡',
    162: '¢',
    163: '£',
    164: '¤',
    165: '¥',
    166: '¦',
    167: '§',
    168: '¨',
    169: '©',
    170: 'ª',
    171: '«',
    172: '¬',
    174: '®',
    175: '¯',
    176: '°',
    177: '±',
    178: '²',
    179: '³',
    180: '´',
    181: 'µ',
    182: '¶',
    183: '·',
    184: '¸',
    185: '¹',
    186: 'º',
    187: '»',
    188: '¼',
    189: '½',
    190: '¾',
    191: '¿',
    8211: '–',
}
# Characters are word delimiters.
# {ord('symbol'): 'symbol'}
_TRANSFER_SYMBOLS = {
    9: '\t',
    10: '\n',
    13: '\r',
    32: ' '
}

def load_data(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print('Error: File not found: "{}"'.format(filepath))
    except PermissionError:
        print('Error: Access to file denied: "{}"'.format(filepath))

def strip_exclude_symbols_to_word(word=''):
    if not word:
        return None
    if ord(word[:1]) in _EXCLUDE_SYMBOLS_ALL:
        word = word.strip(word[:1])
        return strip_exclude_symbols_to_word(word)
    if ord(word[len(word)-1:]) in _EXCLUDE_SYMBOLS_ALL:
        word = word.strip(word[len(word)-1:])
        return strip_exclude_symbols_to_word(word)
    return word

def get_most_frequent_words(text, show_words_length=10):
    words = {}
    word = ''
    for symbol in text:
        symbol_ord = ord(symbol.lower())
        if symbol_ord in _TRANSFER_SYMBOLS and word != '':
            normal_word = strip_exclude_symbols_to_word(word)
            if normal_word is not None:
                words[normal_word] = words.get(normal_word, 0) + 1
            word = ''
        else:
            if symbol_ord not in _TRANSFER_SYMBOLS:
                word += symbol.lower()
    return list(sorted(words.items(), key=lambda x: x[1], reverse=True))[:show_words_length]

def get_most_frequent_words_to_regexp(text, show_words_length=10):
    text = re.split('\W+', text)
    counted_words = Counter(text)
    return counted_words.most_common()[:show_words_length]

def test_two_methods_most_frequent_words(text, show_words_length=10):
    most_frequent_words = get_most_frequent_words(text, show_words_length)
    most_frequent_words_to_regexp = get_most_frequent_words_to_regexp(text, show_words_length)
    if most_frequent_words != most_frequent_words_to_regexp:
        print('Two methods return different results.')
    else:
        print('Two methods return the same results.')
    print('The result of the method "get_most_frequent_words":\n', most_frequent_words)
    print('The result of the method "get_most_frequent_words_to_regexp":\n', most_frequent_words_to_regexp)

def get_arguments():
    args = argparse.ArgumentParser()
    args.add_argument('--path', action='store', dest='filepath',
                        help='Path to text file you want to calculate the frequency of words.')
    args.add_argument('--testing', action='store_true', dest='testing', default=False,
                        help='Starts testing two different methods.')

    return args.parse_args()

if __name__ == '__main__':
    arguments = get_arguments()
    text = load_data(arguments.filepath)
    if text:
        show_words_length = 10
        if not arguments.testing:
            most_frequent_words = get_most_frequent_words(text, show_words_length)
            print(most_frequent_words)
        else:
            test_two_methods_most_frequent_words(text, show_words_length)


