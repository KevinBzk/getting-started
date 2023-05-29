#Working with strings

#how to use the next line
print("Hey \n whats up?")

#using "" in a string
print("The book \"the millionaire fastline\"")

#string funktions
text = "Kevin is a realy nice person and he is 17 years old"

#make every letter a lowercase/uppercase letter
print(text.lower())
print(text.upper())

#check if every letter is a uppercase/lowercase letter
print(text.isupper())
print(text.islower())

#check the lengh of the text
print(len(text))

#check which letter is at this index position (the index begins with 0)
print(text[9])

#check at which index the letter is 
print(text.index("n"))

#replace a part of a text
print(text.replace("Kevin", "Jonathan"))