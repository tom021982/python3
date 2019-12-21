
import string

def function1():
    print("Cat mews")

def function2():
    print("Dog barks")

def function3():
    print("Bear growls")

tokenDict = {"cat": function1, "dog": function2, "bear": function3}

# simulate
lines = ["cat", "dog", "bear"]

for line in lines:
    # lookup the function to call for each line
    functionToCall = tokenDict[line]

    # and call it
    functionToCall()
