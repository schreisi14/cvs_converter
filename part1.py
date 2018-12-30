#!/usr/bin/env python3

# Imports
import csv

# Filenamen
file = 'C110473-3-100000'
wiederstand = 3
untergrenze = 45
obergrenze = 40

# Variablen
line = 0
deletefrom = 5
myarray = []
first_lines = []
third = []
filename = file + ".csv"
endfile = file + "_part1.csv"

# Programmstart
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in csv.reader(csvfile):
        if line < deletefrom:
            # ersten Zeielen speichern
            first_lines.append(row)
        else:
            # Wert U1
            row[-1] = int(float(row[-1]))
            # Wert t
            row[0] = float(row[0])
            # Wert U
            row.append(row[-1] * 100000)
            #Wert I
            row.append(round(row[-1] / wiederstand, 2))
            myarray.append(row)
        line += 1

for element in myarray:
    if element[1] >= obergrenze:
        third.append(element)

line = 0

for element in third:
    line = (line + 1) % len(third)
    nextelem = third[line]
    element.append(round(float(element[0]) - float(nextelem[0]),8))
    pws = element[3] * element[-1] * element[0]
    element.append(pws)
    element.append(pws / wiederstand * 1000)


for element in third:
    if element[1] >= untergrenze:
        first_lines.append(element)
    else:
        break

# OUTPUT
with open(endfile, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(first_lines)

print("Done!")
