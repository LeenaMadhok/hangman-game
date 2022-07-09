#import stages and logo from hangeman_art.py
#import the word to be guessed from hangeman_words.py
import random
import hangman_words
import hangman_art

word_list=hangman_words.word_list
chosen_word=random.choice(word_list)

#*********************************************************************************************************************
#the word that system have selected/chosen for hangeman.
# print(chosen_word)
#*********************************************************************************************************************

word_length=len(chosen_word)

stages=hangman_art.stages
logo=hangman_art.logo
print(logo)

 
display=[]
lives=6

for i in range(0,word_length):
    display+='_'
# print(display)
i=word_length
# print(word_length)
# print("i+",i)
while(i!=0):
  guess = input("Guess a letter: ").lower()

  if guess in display:
      print("already entered")

  if guess not in chosen_word:
    i-=1
    lives-=1

  for a in range(0,word_length):
    if(chosen_word[a]==guess):
      display[a]=guess

  # print(display)              #this will show ["_","_","_",......]
  print(f"{' '.join(display)}")     #this will show _ _ _.......
  # print(lives)
  print(stages[lives])

  if '_' not in display or lives==0:
    i=0

if '_' not in display :
  print("you won")
else:
  print("you lose")
