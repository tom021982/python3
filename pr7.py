# break statement

while True:
    qty = input("Quantity Sold : ")
    if int(qty) == 0 :
        print("Enter Quantity more than Zero !")
        break
    price = input("Unit Price : ")
    sales = 0
    sales = int(qty) * int(price)
    print("Sales Value :  ", sales)
