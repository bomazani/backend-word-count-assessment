#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
Program identifies each unique word in a text file and the number of occurrences
& provides the top 20 words by occurrence.
"""
__author__ = "bomazani"

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

def create_dict(filename):
    """ creates a dictionary with keys=words, and values= count of the word."""
    with open(filename, "r") as f:
        key_list = {}
        for line in f:
            line = line.lower()
            for word in line.split():
                if word not in key_list:
                    key_list[word] = 1
                else:
                    key_list[word] += 1
    return key_list

def print_words(filename):
    """Alphabetize words"""
    word_dict = create_dict(filename)

    for key in sorted(word_dict):
        print(key, word_dict[key])
 

def print_top(filename):
    """ Print top 20 number of occurrences. """
    word_dict = create_dict(filename)

    sorted_items = sorted(word_dict.items(), key=lambda t : t[1], reverse=True)
    print("Top 20 words in {}".format(filename))
    for k,v in sorted_items[:20]:
        print("{}  {}".format(k,v))


def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)


if __name__ == '__main__':
    main()
