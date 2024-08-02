#password generator
import random

words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1','2','3','4','5','6','7','8','9','10']

symbols = ['!','@','#','$','%','^','&','&','*','(',')','+','=','[','<','>','?','/','~']
print("Welcome to Password generator ! ")

hWords = int(input("How many letters you want ? "))
hNums = int(input("How many numbers you want ? "))
hSymbs = int(input("How many symbols you want ? "))

passWord = []

#for letters

for i in range(0,hWords):
    char = random.choice(words)
    passWord += char

#for numbers

for num in range(0,hNums):
    char = random.choice(numbers)
    passWord += char
#for symbols

for i in range(0,hSymbs):
    char = random.choice(symbols)
    passWord += char

#without shuffling
print(f"Without shuffling: {passWord}")

random.shuffle(passWord)

#after shuffling
print(f"After shuffling: {passWord}")

password_string = ""

for i in passWord:
    password_string+=i
print(f"This is your Password: {password_string}")
