
import csv

sampleFile = open('sample.csv')
sampleReader = csv.reader(sampleFile)
sampleData = tuple(sampleReader)
print(sampleData)

# extract from list
print("\n \n")
print(sampleData[0][0])
print(sampleData[0][1])
print(sampleData[0][2])
print(sampleData[1][1])
#print(sampleData[6][1])
