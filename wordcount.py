"""Count words in file."""

import sys

filename = sys.argv[1]

def tokenize(filename):
    """Return a list of words"""
    file = open(filename)

    words_list = []

    for line in file:
        line = line.rstrip().split(' ')
        line = normalize_words(line)
        words_list.extend(line)

        # for word in line:
        #     words_list.append(word)
    
    return words_list

def normalize_words(line):
    normalized = []
    # Filter for alphabet characters
    for word in line: #"Ives?"
        clean = "".join(filter(str.isalpha, word))
        normalized.append(clean.lower())
    return normalized


# put your code here.
def count_words(words):
    """Return a dictionary of words with its count as value"""
    words_dict={}

    for word in words:
        words_dict[word] = words_dict.get(word,0) + 1

    return words_dict

def print_words_counts(word_counts):
    """Prints key and value from the dictionary"""
    
    for key, value in word_counts.items():
        print(f"{key}" + " " f"{value}")

tokens = tokenize(filename)
word_counts = count_words(tokens)
print_words_counts(word_counts)
