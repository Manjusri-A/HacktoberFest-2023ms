from textblob import TextBlob

def Convert(string):
    # Convert the string to a list of words
    li = list(string.split())
    return li

str1 = input("Enter your words: ")  # Changed "word" to "words" for clarity
words = Convert(str1)
corrected_words = []

# Correct spelling for each word
for i in words:
    corrected_words.append(TextBlob(i).correct())  # Correct spelling directly here

print("Wrong words: ", words)
print("Corrected words are: ")
print(" ".join(str(word) for word in corrected_words))  # Print corrected words as a string
