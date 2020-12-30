# Dictionary.py
# tony schwebach
# 11/8/2020
# notes

import json
import difflib

data = json.load(open("dictdata.json"))

def define(word):
    word = word.lower()
    if word in data:
        return(data[word])
    elif word.title() in data:
        return(data[word.title()])
    elif word.upper() in data:
        return(data[word.upper()])
    elif word.capitalize() in data:
        return(data[word.capitalize()])   
    else:
        sug = difflib.get_close_matches(word,data.keys())
        return(str(word)+ " not in dictionary. Did you mean " +str(sug) +"?")

while 0==0:
    word = input("Type word: ")
    definition = define(word)
    i=1
    if type(definition) == list:
        for item in definition:
            print(str(i),": ",item)
            i+=1
    else:
        print(definition)


