#hangman game

import random
import hangMan_stages


print("Welcome to HANGMAN Game!☠️")
print("Number of lives : 6❤️ ")
print("Good Luck ! ")

#words list to generate a word=========================================================================
lives = 6
words = [
    "apple", "banana", "orange", "grape", "cherry", "peach", "plum", "pear", "melon", "berry",
    "house", "tree", "river", "mountain", "valley", "forest", "ocean", "desert", "lake", "field",
    "happy", "sad", "angry", "excited", "bored", "scared", "nervous", "calm", "joyful", "sleepy",
    "cat", "dog", "fish", "bird", "horse", "sheep", "cow", "goat", "chicken", "duck",
    "car", "bus", "train", "plane", "boat", "bike", "truck", "scooter", "tractor", "skateboard",
    "book", "pen", "paper", "desk", "chair", "lamp", "shelf", "notebook", "computer", "tablet",
    "rain", "snow", "wind", "storm", "cloud", "sun", "fog", "hail", "thunder", "lightning",
    "pizza", "burger", "pasta", "salad", "soup", "sandwich", "steak", "chicken", "fries", "cake",
    "blue", "red", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white",
    "run", "jump", "swim", "fly", "walk", "crawl", "climb", "dance", "sing", "read"
]

genWord = random.choice(words)
# print(genWord)

#random word generated=================================================================================




#generating number of blanks to guess
display = []
for i in range(len(genWord)):
    display += '_'
print(display)

#blanks generated======================================================================================




#Guess a letter

gameOver = False

while not gameOver:
    userInput = input("Guess a letter: ").lower()

    for position in range(len(genWord)):
        letter = genWord[position]
        if letter == userInput:
            display[position] = userInput
            print(display)

    if userInput not in genWord:
        lives = lives - 1
        print(f"Lives - {lives}❤️")
        if lives == 0:
            gameOver = True
            print("You lose - 0❤️")

    if '_' not in display:
        gameOver = True
        print("You Won 💃👯‍♀️🕺")
    print(hangMan_stages.hangman_stages[lives])