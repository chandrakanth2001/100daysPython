#rock paper scissor game

import random

#computer choice

comp_choice = random.randint(0,2)
# print(f"Computer choice is {comp_choice}")2

#User choice : 0-Rock, 1-Paper, 2-Scissors

user_choice = int(input("Enter your choice: 0-Rock, 1-Paper, 2-Scissors : "))

#condtions

if user_choice == comp_choice:
    print(f"Computer choice : {comp_choice}, Your Choice: {user_choice}, Draw!🙂")
elif user_choice == 3 and comp_choice == 2:
    print(f'Computer choice : {comp_choice}, Your Choice: {user_choice}, U Won!🕺💃🕺💃👯‍♀️')
elif user_choice == 2 and comp_choice == 0:
    print(f"Computer choice : {comp_choice}, Your Choice: {user_choice}, Computer Won! 💩💩")
elif comp_choice>user_choice:
    print(f"Computer choice : {comp_choice}, Your Choice: {user_choice}, Computer Won! 💩💩")
elif user_choice>comp_choice:
    print(f"Computer choice : {comp_choice}, Your Choice: {user_choice}, U Won!🕺💃🕺💃👯‍")