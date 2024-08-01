#longest word in the sentence

def lonWord(sentence):

    words = sentence.split(" ")

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    print(f"The longest word in this sentence is '{longest}'")

lonWord("chandrakanth is coding")
