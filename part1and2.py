#!/usr/bin/env python3

# Imports
import csv

# Filenamen
file = 'WA000002'
wiederstand = 3
untergrenze_pt1 = 45
untergrenze_pt2 = 90

# Variablen
line = 0
deletefrom = 10
myarray = []
end_array_pt1 = []
end_array_pt2 = []
third = []
filename = file + ".cvs"
endfile1 = file + "part1.cvs"
endfile2 = file + "part2.cvs"

# Programmstart
with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in csv.reader(csvfile):
        if line < deletefrom:
            # ersten 10 Zeielen speichern
            end_array_pt1.append(row)
        else:
            row[-1] = int(float(row[-1]))
            row[1] = round(float(row[-2]) * (-1),10)
            row[2] = row[-1] * 100000
            row[3] = row[-1]
            row[-1] = round(row[-1] / wiederstand, 2)
            myarray.append(row)
        line += 1

for element in myarray:
    if element[3] >= 40.0:
        third.append(element)

# spezifisch Part 1
line = 0
for element in third:
    line = (line + 1) % len(third)
    nextelem = third[line]
    element [0] = round(float(element[1]) - float(nextelem[1]),8)
    pws = round(element[3] * element[-1] * element[0],4)
    element.append(pws)
    element.append(round(pws / wiederstand * 1000 , 2))

for element in third:
    if element[3] >= untergrenze_pt1:
        # beistrich durch strichpunkt ersetzen
        # punkt durch beistrich erstetzen
        end_array_pt1.append(element)
    else:
        break

# OUTPUT1
with open(endfile1, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(end_array_pt1)

# spezifisch Part 2
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
    if element[3] >= untergrenze_pt2:
        # beistrich durch strichpunkt ersetzen
        # punkt durch beistrich erstetzen
        end_array_pt2.append(element)
    else:
        break

# OUTPUT2
with open(endfile2, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(end_array_pt2)

print("Done!")
