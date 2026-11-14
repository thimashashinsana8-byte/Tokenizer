import re

def tokenize(text):

    pattern = (
        r"\d{4}-\d{2}-\d{2}"
        r"|\d+(?:\.\d+)?"
        r"|\w+(?:['’]\w+)*"
        r"|[^\w\s]"
    )
    tokens = re.findall(pattern, text)
    return tokens

text1 = "I don't like bad weather."
text2 = "The price is 25.50 dollars."
text3 = "The examination is on 2026-11-14."

print(tokenize(text1))
print(tokenize(text2))
print(tokenize(text3))

print("...............................")
sentence = input("Enter a sentence: ")
result = tokenize(sentence)
numOfWords = len(result)
print(result)
print(f"The number of tokens:{(numOfWords)}")