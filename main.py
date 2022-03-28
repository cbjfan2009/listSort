 # Purpose: open mailing address lists to re-sort trays based on most-full trays first
import csv
from tkinter import filedialog as fd

# OPEN CSV, EXTRACT HEADERS AND ROWS

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



# loop through 'rows' to make dictionary of lists with tray_number as the key and associated addresses as values

tray_count = 1
dict_trays = {}

for row in rows:
    if row[tray_number_index] not in dict_trays.keys():
        dict_trays[row[tray_number_index]] = row
    else:
        dict_trays[row[tray_number_index]].append(row)

 # print tray number (x), number of items in the list (pieces in tray), the addresses in the tray.
for x, y in dict_trays.items():
    print(x, len(y) ,y)


res = ' '.join(sorted(dict_trays, key = lambda key: len(dict_trays[key]), reverse=True))

print("Here is the output of sorting trays by length of list (res) \n", res)