#Palindrome num

def palindrome(num):
    rev_num = 0
    check_no = num

    while check_no > 0:
        remainder = check_no%10
        rev_num = (rev_num*10)+remainder
        check_no = check_no // 10
    if num == rev_num:
        print(f"The og num is {num} , Reversed is {rev_num} . So this is a PALINDROME")
    else:
        print(f"The og num is {num} , Reversed is {rev_num} . So not a PALINDROME")

palindrome(1221)