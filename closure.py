# main purpose of closure function is to save memory.
# even after deleting the main function, it is able to make the calculation from the virtual memory.

def beginFrom(begin):
    def stepby(num):
        return begin + num
    return stepby

f = beginFrom(10)
h = beginFrom(120)

print(f(2), h(4))

del beginFrom

print(f(8))
