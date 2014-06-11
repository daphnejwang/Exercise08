#!/usr/bin/env python

from sys import argv
import random
script, filename = argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    input_text = corpus.read()
    # print input_text
    words = input_text.split()
    # print words

    chain_dict = {}
    for i in range(len(words) -2):
        tuple_words = (words[i], words[i+1])
        if chain_dict.get(tuple_words, 0):
            chain_dict[tuple_words].append(words[i+2])
        else:
            chain_dict[tuple_words] = [words[i+2]]
    # print chain_dict
    return chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""

    rand_tuple = random.choice(chains.keys())
    # print "random tuple: %s" % str(rand_tuple)
    paragraph = []

    for indices in range(10):
        found_value = chains.get(rand_tuple, 0)
        if found_value == 0:
            break
        # print found_value
        rand_word = random.choice(found_value)
        rand_tuple = (rand_tuple[1],rand_word)
        # print "random tuple: %s" % str(rand_tuple)
        paragraph.append(rand_tuple[1])

    text_string = ' '.join(paragraph)
    # print text_string
    return text_string

def main():
    # args = sys.argv
    # my_file = argv[1]
    input_text = open(filename)
    


    # Change this to read input_text from a file
    # input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
