import sys
print("This is a calculator")

num1 = input("num1: ")
try:
    int(num1)
except:
    print("invalid num")
    sys.exit(1)

num1 = int(num1)

zeichen = input("operator: ")

num2 = input("num1: ")
try:
    int(num2)
except:
    print("invalid num")
    sys.exit(1)

num2 = int(num2)
print("\n")

if zeichen == "+":
    print(num1 + num2)
elif zeichen == ":" or zeichen == "/":
    print(num1 / num2)
elif zeichen == "x" or zeichen == "*":
    print(num1 * num2)
elif zeichen == "-":
    print(num1 - num2)
else:
    print("invalid")