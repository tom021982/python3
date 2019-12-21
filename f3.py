
def countries(mine, *others):
    """The script accepts variable number of 
    paramaters by using the *args
    pointers(s)
    """

    print("My Country is : ", mine)
    for cntry in others:
        print("Foreign Country is : ", cntry)

countries('India', 'Japan', 'China', 'UK')
print(countries.__doc__)
