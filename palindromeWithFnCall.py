#using function call

def palindrome(num):
    rev_num = 0
    while num > 0:
        remainder = num % 10
        rev_num = (rev_num*10)+remainder
        num //= 10
    return rev_num

def checkingFunction(num):

    reversedNum = palindrome(num)

    # return reversedNum == num   #if needed or use conditional statements to chk

    if reversedNum==num:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")


checkingFunction(121)