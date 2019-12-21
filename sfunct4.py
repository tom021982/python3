
import sys

def menu():
    print("Welcome to calculator.py")
    print("Your options are: ")
    print(" ")
    print("1) Addition")
    print("2) Substraction")
    print("3) Multiplication")
    print("4) Division")
    print("5) Quit calculator.py")
    print(" ")
    return int(input("Choose your option: "))

def add(a, b):
    print(a, "+", b, "=", a + b)

def sub(a, b):
    print(b, "-", a, "=", b - a)

def mul(a, b):
    print(a, "*", b, "=", a * b)

def div(a, b):
    print(a, "/", b, "=", a / b)

loop = True
choice = 0
while loop:
    choice = menu()
    print("Choice is ", choice)
    if choice == 1:
        add(int(input("Add this: ")),int(input("to this: ")))
    elif choice == 2:
        sub(int(input("Subtract this: ")),int(input("from this: ")))
    elif choice == 3:
        mul(int(input("Multiply this: ")),int(input("by this: ")))
    elif choice == 4:
        div(int(input("Divide this: ")),int(input("by this: ")))
    elif choice == 5:
        loop = False

print("Thankyou for using calculator.py!")
