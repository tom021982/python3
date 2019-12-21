import csv

sampleFile = open('Europe.csv')
sampleReader = csv.reader(sampleFile)
for row in sampleReader:
    print('Row #' + str(sampleReader.line_num) + ' ' + str(row))
