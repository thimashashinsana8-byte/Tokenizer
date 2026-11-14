import re

def tokenize(text):

    pattern = r"\w+|[^\w\s]"
    tokens = re.findall(pattern, text)
    return tokens


#sentence = input("Enter the sentence: ")
sentence = "I love learning Python!"

result = tokenize(sentence)
numOfWords = len(result)

print(result)
print(f"The number of tokens:{(numOfWords)}")
