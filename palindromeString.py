#checking the string is palindrome or not

def palinString(str):
    rev_str = ""
    for i in range(len(str)-1,-1,-1):
        rev_str = rev_str+str[i]
    return rev_str

def checking(str):
    revString = palinString(str)
    if revString == str:
        print(f"The og string is {str}, Reversed string is {revString} So this is a PALINDROME string")
    else:
        print(f"The og string is {str}, Reversed string is {revString} So this is not a PALINDROME string")


checking("racecar")
