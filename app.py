import json 
from difflib import get_close_matches

data = json.load(open("data.json"))

x = ["1", "3"]

def similar_word(word):
    word = word.lower()
    first_letter = word[0]
    return get_close_matches(word, data.keys(), n=1)


def find_word(word):
    
    word = word.lower()
    if word in data:
        return data[word]
    #word not found instantly but may have close matches. Find close matches and suggest them
    elif word not in data and len(similar_word(word)) > 0: 
        closest_word = similar_word(word)
        return "Perhaps did you mean " + closest_word[0]

    else:
        return "Word does not exist. Please double check it"


#print(find_word(text))


word = input("Word:")
print(find_word(word))