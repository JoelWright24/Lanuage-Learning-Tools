import numpy as np
import random

# First import the cvs file

Words_List = np.genfromtxt('GermanEnglishList.csv', encoding="utf8", delimiter=';', dtype=None)

# Generate a random number for indexing. 
number = np.random.randint(0, high=len(Words_List)) 
# Select the row
row = Words_List[number]
German_word = row[0]
English_word = row[1]
#Create a random float between 0 and 1
rand_float= random.uniform(0,1)

if rand_float<0.5:
    # The German word is ... what is the English word?
    print ("The German word is", German_word)
    attempt=input("What is the English Word? ")
    if attempt==English_word:
        print ("Great Success!")
    else:
        print ("That was not quite right")
        print ("The answer was ",English_word)
else:
    #The Enlish word is ... what is the German word?
    
    print ("The English word is", English_word)
    attempt=input("What is the Deutsche Word? ")
    if attempt==German_word:
        print ("Viel Erfolg!")
    else:
        print ("Das war fast richtig...")
        print ("Die Antwort war ",German_word)