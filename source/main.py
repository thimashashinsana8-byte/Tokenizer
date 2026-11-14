from tokenizer import tokenize

text1 = "I don't like bad weather."
text2 = "The price is 25.50 dollars."
text3 = "The examination is on 2026-11-14."
text4 = "මගේ නම තිමාෂ් ආශිංසන 😊"

print(tokenize(text1))
print(tokenize(text2))
print(tokenize(text3))
print(tokenize(text4))

print("...............................")

"""
sentence = input("Enter a sentence: ")
result = tokenize(sentence)
numOfWords = len(result)
print(result)
print(f"The number of tokens:{(numOfWords)}")
"""