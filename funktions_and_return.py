#you make a funktion with def
def say_hi():
    print("Hey")
    
#call the funktion
say_hi()

#parameters a informatons you can give a information
def user(name, age):
    print("Hey "+ name)
    print("your " + str(age) + " years old")
    
nam1e = input()
age2 = input()

user(nam1e, age2)

#with return you can return informations from a funktion
def cube(num):
    a = num*num*num
    return a
print(cube(3))