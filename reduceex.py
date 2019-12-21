
# importing functools for reduce()
import functools

# initializing list
lis = [4, 6, 2, 8, 12, ]

# using reduce to compute sum of list
# end= is to indicate a space after the end of statement.
# instead of a new line.
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a,b : a+b , lis))

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a,b : a if a > b else b, lis))
