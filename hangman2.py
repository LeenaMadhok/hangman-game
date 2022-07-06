#Step 2&3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length=len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')
# print(type(chosen_word))
#TODO-1: - Create an empty List called display.
display=[]
for i in range(0,word_length):
    display+='_'
print(display)

  #For each letter in the chosen_word, add a "_" to 'display'.
  #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
i=word_length
# print(word_length)
# print("i+",i)
while(i!=0):
  guess = input("Guess a letter: ").lower()
  if guess not in chosen_word:
    i-=1
  #TODO-2: - Loop through each position in the chosen_word;
  #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
  #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

  # print(len(chosen_word))
  for a in range(0,word_length):
    if(chosen_word[a]==guess):
      display[a]=guess
      i-=1

  #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
  #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
  print(display)
  # print(i)
# print(str(display))
# print(list(chosen_word),display)
if(list(chosen_word)==display):
  print("you won")
else:
  print("you lose")
