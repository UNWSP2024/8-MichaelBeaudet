# Title: Program 2 Week 8
# Author: Michael Beaudet
# Data 3/21/25

def word_separator(sentence):
# initialize new_sentence
    new_sentence = ""
    #    Add your logic here
# Start the process
    new_sentence += sentence[0].upper()
# Create the loop starting from the second character
    for char in sentence[1:]:
        if char.isupper():
# Add a space and make it lowercase
            new_sentence += " " + char.lower()
        else:
# If its not uppercase just add the character
            new_sentence += char
    return new_sentence.strip()
# Get user input
sentence = input("Write a sentence in which all the words are not separated by spaces, but the first letter of each word is capitalized: ")
# call the variable
new_sentence = word_separator(sentence)

# Display results
print(new_sentence)