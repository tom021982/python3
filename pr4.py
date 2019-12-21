# if .. else statement

age = input("Enter Age: ")

if int(age) > 72:
    print("Eligible for Senior Citizen Concession")
elif int(age) < 20:
    print("Eligible for Student Concession")
else:
    print("Normal Charges")
