#!/usr/bin/env python3

# Imports
import csv

# Filenamen
file = 'WA000002'
wiederstand = 90
untergrenze = 135
obergrenze = 40

# Variablen
line = 0
deletefrom = 10
myarray = []
first_lines = []
third = []
filename = file + ".CVS"
endfile = file + "part2.csv"

# Programmstart
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in csv.reader(csvfile):
        if line < deletefrom:
            # ersten 10 Zeielen speichern
            first_lines.append(row)
        else:
            row[-1] = int(float(row[-1]))
            row[1] = round(float(row[-2]) * (-1),10)
            row[2] = row[-1] * 100000
            row[3] = row[-1]
            row[-1] = round(row[-1] / wiederstand, 2)
            myarray.append(row)
        line += 1

for element in myarray:
    if element[3] >= obergrenze:
        third.append(element)

line = 0
for element in third:
    line = (line + 1) % len(third)
    nextelem = third[line]
    element[0] = (float(element[1]) - float(nextelem[1])) *10
    element[0] = round(element[0],6)
    pws = round(element[3] * element[-1] * element[0],4)
    element.append(pws)
    element.append(round(pws / wiederstand * 1000 , 2))

for element in third:
    if element[3] >= untergrenze:
        # beistrich durch strichpunkt ersetzen
        # punkt durch beistrich erstetzen
        first_lines.append(element)
    else:
        break

# OUTPUT
with open(endfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(first_lines)

print("Done!")
