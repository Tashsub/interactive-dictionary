import json 
from difflib import get_close_matches

data = json.load(open("data.json"))



#finds simialr word from json file
def similar_word(word):
    word = word.lower()
    first_letter = word[0]
    return get_close_matches(word, data.keys(), n=1)

#if a word has more than pne meaning prints on 
#seperate lines. 
def seperate(arr): 
    for x in arr: 
        print (x)

def find_word(word):
    
    word = word.lower()

    if word in data:
        return data[word]
    #word not found instantly but may have close matches. Find close matches and suggest them
    elif(word not in data and len(similar_word(word)) > 0): 
        closest_word = similar_word(word)
        question = input("Wait, did you mean %s ? Enter yes or no: " % closest_word[0])
        question = question.lower()
        
        if question == "yes" :
            correct_word = data[closest_word[0]]
            return correct_word

        elif question == "no":
            return "The word doesnt exist, try again"
        else: 
            return "Sorry we didn't understand that"
    else:
        return "word does not exist"
    


word = input("Enter a word: ")

word_def = find_word(word)


if type(word_def) == list: 
    for x in word_def: 
        print(x)
else: 
    print(word_def)

