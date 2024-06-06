import csv

inputFile = 'security_incidents.csv'
outputFile = 'security_incidents_modified.csv'

with open(inputFile, mode='r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

newColumn = 'Status'
value = 'Pending'
header = data[0] + [newColumn]
rows = [row + [value] for row in data[1:]]

with open(outputFile, mode='w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Modified data saved to '{outputFile}'")

