import csv

sourcefile = csv.DictReader(open("capitals.csv"))

country = input("Capital of which country ? ")
for row in sourcefile:
    if row['Country'] == country:
        print("The capital of %s is %s: " %(row['Country'],row['capital']))
