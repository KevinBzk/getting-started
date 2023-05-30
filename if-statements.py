#if statements are only executet if the condition is true

#example

a = input("yes or no: ") 

if a == "yes":
    print("you entered yes")

#you can also say what the code needs to do when the condition is false

if a == "yes":
    print("you choose yes")
elif a== "no":
    print("you choose no")
else:
    print("invalid answer")

#you can also give two conditions
#if you type or only one condition has to be true
#if you type and both conditions need to be true

if a == "yes" or a== "wheyo":
    print("nice")