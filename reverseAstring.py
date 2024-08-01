#reverse a string

def revString(str):
    rev_str = ""
    for i in range(len(str)-1,-1,-1):
        rev_str = rev_str+str[i]
    print(rev_str)

revString("chandrakanth")