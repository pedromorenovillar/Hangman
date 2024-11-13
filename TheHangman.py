# 👉 Day 39 Challenge
# Once the word has been picked, the following things need to happen:

# Prompt the user to type in a letter. X
# Check if the letter is in the word.  X
# If it does, output the word with all blanks apart from the letter(s) they've already guessed. X
# Keep a running list of the letters they've used. X
# Count how many times they've picked a letter that isn't in the word - more than 6 and they lose. X
# Output a 'win' message if they reveal all the letters. X
# 🥳 Extra points for using ASCII art to draw the hangman as the player makes incorrect guesses. X


import random
import os
import time

default = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"

listOfWords = ["potato", "Sweden", "castle", "sharp", "decline", "Andalusia", "purple"]

wordChosen = random.choice(listOfWords) # randomizes word selection
lives = 6
lettersPicked = [] # stores letters selected by user
wordLength = len(wordChosen) # used to keep score 
lettersFound = 0 # used to keep score

def hiddenWord(color, default): # displays found letters or _ for not found ones
  result = ""
  for letter in wordChosen:
    if letter in lettersPicked:
      result += f'{color}{letter}{default}'
    else:
      result += "_"
  return result

while True:
  print()
  print('😵̷̊̊̊̊̊   Hangman 😵̷̊̊̊̊̊')
  print('—————————————————')
  if lives == 0:
    print(f'-- {red}YOU DIED!{default} --')
  else:  
    print('Lives:', lives)
    print('Letters found:', f'{green}{lettersFound}{default}')
    print('Used letters:', ", ".join(lettersPicked))
    print('Word:', hiddenWord(green, default))
  print()
  print('+—————+')
  print('|/    |')
  if lives >= 6:
    print('|')
    print('|')
    print('|')
  if lives == 5:
    print('|     0')
    print('|')
    print('|')
  if lives == 4:
    print('|     0')
    print("|     |")
    print("|")
  if lives == 3:
    print('|     0')
    print("|    /|")
    print("|")
  if lives == 2:
    print('|     0')
    print("|    /|\\")
    print("|")
  if lives == 1:
    print('|     0')
    print("|    /|\\")
    print("|    / ")
  if lives == 0:
    print('|     0')
    print("|    /|\\")
    print("|    / \\")
  print('|______')
  print('|      |')
  print('========')
  print('—————————————————')
  choice = input(f'{yellow}Choose{default} a letter: ').lower()

  if len(choice) > 1:
    print(f'You can only pick {red}one{default} letter.')
    time.sleep(1)
    os.system("clear")
  elif choice.isalpha() == False:
    print(f'You can {yellow}only{default} pick {blue}a letter character{default}.')
    time.sleep(1)
    os.system("clear")
  elif choice in wordChosen.lower():
    if choice in lettersPicked:
      print(f'Letter {red}already{default} selected; pick again!')
      lives -= 1
      print(f'You have {red}{lives}{default} lives left!')
    else:
      lettersPicked.append(choice)
      lettersFound += wordChosen.lower().count(choice.lower())
      print(f'{green}Correct!{default}')
      if choice.upper() in wordChosen:
        lettersPicked.append(choice.upper())
    time.sleep(1)
    os.system("clear")
  elif choice not in wordChosen:
    lettersPicked.append(choice)
    print(f'You have chosen... {purple}poorly{default}!')
    lives -= 1
    print(f'You have {red}{lives}{default} lives left!')
    time.sleep(1)
    os.system("clear")
  if lettersFound == wordLength:
    print(f'{yellow}You have beaten the gallows!{default}')
    print()
    print(f' {blue}{wordChosen.upper(): ^12}{default}')
    print(f'{yellow}    \\0/')
    print("     |")
    print(f"    / \\{default}")
    time.sleep(5)
    os.system("clear")
    break