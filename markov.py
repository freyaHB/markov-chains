"""Generate Markov text from text files."""

from random import choice
import sys
file = sys.argv[1]
def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(file_path).read()
    print(contents)
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()
    #loop over every two word pair
    for i in range(len(text_list)-2):#for every 'index' in the range of the len of text_list except for the last two
        key = (text_list[i], text_list[i+1])#index of 0 then +1(until the len of text_list ends) saves as a tuple in the key var
        val = text_list[i+2] #index of +2 saved in val variable 
        chains[key] = chains.get(key,[]) + [val]  #saves keys into chains[key](dict) that aren't already in [key], if already in key from chain, will return an empty list 
        #print("This is text_list[i] and text_list[i+1} "+text_list[i],text_list[i+1])
        # chains[key].append(val)

    # print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    # your code goes here
    # get keys from chains dict, put all keys in to a list, randomly select a key (a tuple) from the list
    key = choice(list(chains.keys())) 

    words = []
    # save key tuple to a list of words
    words.append(key[0])
    words.append(key[1])


    # while the key (tuples, bigrams) is in the chains dict now
    while key in chains:
        # select a random element from the value (which is a list of words),
        # add it to the words list
        words.append(choice(chains[key])) 
        # assign the last and the second last tuple key
        # now change the key you are looking at, find last two words
        # that is now your new key (tuple)
        key = (words[-2], words[-1])

    # print(words)

    # give me a list of strings, tell me the character you want to join them w/
    return " ".join(words)


# input_path = "green-eggs.txt"
#input_path = "green-eggs.txt"


# Open the file and turn it into one long string
#input_text = open_and_read_file(input_path)
input_text = open_and_read_file(file)
# Get a Markov chain
chains = make_chains(input_text)

# # Produce random text
random_text = make_text(chains)

print(random_text)
