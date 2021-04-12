import numpy as np
import random

# First import the cvs file

Words_List = np.genfromtxt('Kapital5_Module5.csv', encoding="utf8", delimiter=';', dtype=None)

# Generate a random number for indexing. 
number_correct = np.random.randint(0, high=len(Words_List))
number_false1 = np.random.randint(0, high=len(Words_List))
number_false2 = np.random.randint(0, high=len(Words_List)) 
# Select the correct word in English and German
selection_English=[]
selction_German=[]
row = Words_List[number_correct]
correct_German_word = row[0]
correct_English_word = row[1]
# Select the false 1 word in English and German
selection_English=[]
selction_German=[]
row = Words_List[number_false1]
false1_German_word = row[0]
false1_English_word = row[1]
# Select the false 2 word in English and German
selection_English=[]
selction_German=[]
row = Words_List[number_false2]
false2_German_word = row[0]
false2_English_word = row[1]

# The German word is ... what is the English word?
print ("The German word is", correct_German_word)

#attempt=input("What is the English Word? ")

#Need to create a random placement of the correct answer in index 0, 1 or 2

placement_index=[0, 1, 2]
random.shuffle(placement_index)
answer_order=[]
for ii in range (len(placement_index)):
    if (placement_index[ii]==0):
        answer_order.append(correct_English_word)
    elif (placement_index[ii]==1):
        answer_order.append(false1_English_word)
    elif (placement_index[ii]==2):
        answer_order.append(false2_English_word)    
        
print (answer_order)

'''

if attempt==English_word:
    print ("Great Success!")
else:
    print ("That was not quite right")
    print ("The answer was ",English_word)

'''