#Hangman Game 
import random 
print("*****************************")
print("Welcome to HANGMAN")
print("*****************************")

#creating a list
my_words=['Student','python','bottle','lab','laptop']
selected_word=random.choice(my_words)
##print("choosen word:",selected_word)

list=[]
for i in selected_word:
    print("_",end=" ")
    list.append("_")


count=0
while(("_" in list) and (count<6)):
    l=input("Guess a letter:")
    if(l in selected_word ):
        print("Correct!")
        for i in range(len(selected_word)):
            if(selected_word[i]==l):
                list[i]=l
        print(list)
            
    else:
        count=count+1
        print("Wrong!")
        print("Remaining Chances:",6-count)   
if("_"  not in list):
    print("You won the game")
else:
    print("You lose the game")
print("GAME OVER")



 
    






