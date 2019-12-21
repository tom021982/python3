
def part1(cntry1, cntry2):
    print("I visited %s and %s last year"%(cntry1, cntry2))

def travel(x,y):
    x(*y)

travel(part1,("France", "Spain"))
