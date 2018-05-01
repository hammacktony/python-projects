"""
Author: Tony Hammack
Program: Interactice Dictionary
"""

import json
from difflib import get_close_matches
import sys

def translate(w,data):
    """
    Used to translate user input to a usable dictionary key for their query.
    Also, searches for similar words in dictionary and asks the user if they want
    want to use tha word.
    """
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(), cutoff=0.6)) > 0:
        response = input('Did you mean {} instead? Enter Y if yes or N for no: '.format(get_close_matches(w,data.keys(), cutoff=0.6)[0]))
        if response.lower() == 'y':
            return data[get_close_matches(w,data.keys(), cutoff=0.6)[0]]
        elif response.lower() == 'n':
            return 'That word is not in the dictionary!'
        else:
            return "We did not understand your query."
            sys.exit()
    else:
        return 'That word is not in the dictionary!'

if __name__ == '__main__':
    try:
        # Initialize
        DATA = json.load(open('data.json'))

        # Input
        WORD = input('Please enter a word you want to define: ')
        OUTPUT = translate(WORD,DATA)
        # Display output
        if type(OUTPUT) == list:
            print('\nThe definition(s) is/are: ')
            for item in OUTPUT:
                print('-'+item)
        else:
            print(OUTPUT)
    except FileNotFoundError as err:
        print(err)
