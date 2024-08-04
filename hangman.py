#choose a random word
import random
import  hangman_stages
print("Welcome to Hangman Game!!")
print("Best of luck and enjoy!!!!")
word_list=["apple", "banana","orange","grapes","mango","strawberry","pineapple"]
lives=6
choice_word= random.choice(word_list)
#diplay the blank space
display=[]
for i in range (len(choice_word)):  #0 1 2 3 4 5
    display+= '_'
print(display)    
#taking input and applying conditions
game_over= False 
while not game_over:
    guessed_letter=input("Guess a Letter: ").lower()
    for position in range (len(choice_word)):
        letter=choice_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)    
    #subtracting lives if the word not matched    
    if guessed_letter not in choice_word:
        lives-=1
        if lives==0:
            game_over=True
            print("Game Over!! You Lose")   #Game Over
    if '_' not in display:
           
        print("You Win..")
    
    print(hangman_stages.stages[lives])
    print("You are left with only",lives,"lives") 
    

        