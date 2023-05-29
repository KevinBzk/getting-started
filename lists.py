#how to use lists
friends = ["Kevin", "Julius", "Norman"]

age = ["12", "123", "8772"]

#how to get data out of the list
print(friends[1])

#with a : you can get all data after the index
print(friends[0:3])

#to cahnge something in the list you take the index an set it equal to something
friends[2] = "Justin"
print(friends[2])

#funktions

#merge two lists
friends.extend(age)

#add something to the end
friends.append("Jeff")

#insert something to an index, every name after that will have an new index
friends.insert(1, "Kakak")

#remove things from a list
friends.remove("Kevin")


#will delete this specific index
friends.pop(1)

#tell on which index the name is
print(friends.index("Jeff"))

#counts how many this specific name is in the list
print(friends.count("Jeff"))

#it will sort the list after the alphabetic order 
friends.sort()

#it will sort the list in the reverse alphabetic order
friends.reverse()

#copy a list
friends2 = friends.copy()

#clear the whole list
friends.clear()
