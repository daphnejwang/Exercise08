#!/usr/bin/env python

from sys import argv
script, filename = argv

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    input_text = corpus.read()
    words = input_text.split()

    chain_dict = {}
    for i in range(len(words) -2):
        tuple_words = (words[i], words[i+1])
        chain_dict[tuple_words] = words[i+2]
    # print chain_dict
    return chain_dict

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    original_text = "everyone cuddles"
    





    return "Here's some random text."

def main():
    # args = sys.argv
    # my_file = argv[1]
    input_text = open(filename)
    


    # Change this to read input_text from a file
    # input_text = "Some text"

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
