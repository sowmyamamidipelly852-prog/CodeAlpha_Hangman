#Hangman Game:
#importing random to select the word from list randomly
import random 
print("*********************************")
print("\tWelcome to HANGMAN")
print("*********************************")
print()

#creating a list that contain 5 prefined words
my_words=['student','python','bottle','lab','laptop']

#choosing a word randomly from list using choice() function
selected_word=random.choice(my_words)


hidden_word=[]
for i in selected_word:
    hidden_word.append("_")
print("You have only 6 Chances so try guess the word in 6 attempts")
print(" ".join(hidden_word))



guessed_letters=[] #it store the letters was guessed
count=0 #this variable is used to count wrong attempts

#while loop repeats until the word is guessed or 6 attempts are completed
while(("_" in hidden_word) and (count<6)):
    
    #player guess a letter
    l=input("\nGuess a letter:").lower()


    #only letter should be guessed at a time
    if(len(l)!=1):
        print("Please enter one letter at a time")
        continue

    #repeated guesses are not allowed
    if l in guessed_letters:
        print("you already guessed",l,"letter.")
        continue
    guessed_letters.append(l) 

    #display the place value of letter in word if guess is correct
    if(l in selected_word ):
        print("Correct!")
        for i in range(len(selected_word)):
            if(selected_word[i]==l):
                hidden_word[i]=l
        print(" ".join(hidden_word))
    
    #display the remaining chances if guess is wrong      
    else:
        count=count+1
        print("Wrong!")
        print("Remaining Chances:",6-count)



if("_"  not in hidden_word):
    print("\n\n YOU WON THE GAME")#guess word is correct
else:
    print("\n\n YOU lOSE THE GAME")
    print("The word was",selected_word)#6 attempts are failed

print("********************************************************")
print("\t\t\tGAME OVER")
print("*******************************************************")



 
    






