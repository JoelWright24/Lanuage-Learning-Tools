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

#Create a random float between 0 and 1
rand_float= random.uniform(0,1)

if rand_float>0.5:

    # The German word is ... what is the English word?
    print ("The German word is", correct_German_word)

    # Need to create a random placement of the correct answer

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
            
    print ("Is the translation: \n 1.) ",answer_order[0]," \n 2.) ",answer_order[1],"  \n 3.) ",answer_order[2]," ?")

    selected_answer=int(input("Select Answer 1, 2 or 3: "))

    #need to check if 0 index matched the correct_German_word
    selected_index=selected_answer-1

    if answer_order[selected_index] == correct_English_word:
        print("Congratulations! You are correct!")
    else:
        print("Not Quite!")
        print ("The correct translation of the German \"",correct_German_word,"\" was the English word \"",correct_English_word,"\". ")

else:
    
    # The English word is ... what is the German word?
    print ("The English word is", correct_English_word)

    # Need to create a random placement of the correct answer

    placement_index=[0, 1, 2]
    random.shuffle(placement_index)
    answer_order=[]
    for ii in range (len(placement_index)):
        if (placement_index[ii]==0):
            answer_order.append(correct_German_word)
        elif (placement_index[ii]==1):
            answer_order.append(false1_German_word)
        elif (placement_index[ii]==2):
            answer_order.append(false2_German_word)    
            
    print ("Is the translation: \n 1.) ",answer_order[0]," \n 2.) ",answer_order[1],"  \n 3.) ",answer_order[2]," ?")

    selected_answer=int(input("Select Answer 1, 2 or 3: "))

    #need to check if 0 index matched the correct_German_word
    selected_index=selected_answer-1

    if answer_order[selected_index] == correct_German_word:
        print("Congratulations! You are correct!")
    else:
        print("Not Quite!")
        print ("The correct translation of the English \"",correct_English_word,"\" was the German word \"",correct_German_word,"\". ")


