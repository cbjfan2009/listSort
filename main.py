 # Purpose: open mailing address lists to re-sort trays based on most-full trays first
import csv
from tkinter import filedialog as fd

 #TODO Find and Access CSV list

headers = []
rows = []

fileName = fd.askopenfilename()

with open(fileName, 'r') as csvfile:
    # reader object
    reader = csv.reader(csvfile)

    # first row = list of HEADERS
    headers.append(next(reader))

    # each row is a list
    for row in reader:
        rows.append(row)

    # get total number of rows
    print(f"Total no. of rows: {reader.line_num}")


for x in headers:
    print(f"Column headers: {x}")


 # find tray number position in list

tray_number_index = 0
for x in headers:
    for c, v in enumerate(x):
        if v == 'Tray_Number':# or 'Tray Number': -- when I add the 'or' clause then it breaks....?
            tray_number_index = c

print(f"'Tray Number' index is: {tray_number_index}")



 #TODO Count pieces per tray and keep trays in order

tray_count = 1
dict = {}

for row in rows:
    if row[tray_number_index] not in dict.keys():
        dict[row[tray_number_index]] = row
    else:
        dict[row[tray_number_index]].append(row)

 # print tray number (x), number of items in the list (pieces in tray), the addresses in the tray.
for x, y in dict.items():
    print(x, len(y) ,y)


pass
