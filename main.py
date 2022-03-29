 # Purpose: open mailing address lists to re-sort trays based on most-full trays first
import csv, os
from tkinter import filedialog as fd
from pprint import pprint

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
        if v == 'Tray_Number' or v == 'Tray Number':
            tray_number_index = c

#print(f"'Tray Number' index is: {tray_number_index}")



# loop through 'rows' to make dictionary of lists with tray_number as the key and associated addresses as values


dict_trays = {}
'''the loop – checking tray_number_index (tray#) is in dictionary key.  If no, add that tray# as key and the row as
 value; If yes, add each row to that key.  When new tray#, new key made, etc.'''

for row in rows:
    if row[tray_number_index] not in dict_trays.keys():
        dict_trays[row[tray_number_index]] = [row]
    else:
        dict_trays[row[tray_number_index]].append(row)

# print tray number (x), number of items in the list (pieces in tray), the addresses in the tray.
for x, y in dict_trays.items():
    print(x, len(y) ,y)


# sorting the dictionary by length of list (aka number of pieces in the tray)

res = sorted(dict_trays, key=lambda key: len(dict_trays[key]), reverse=True)
#print("Here is the output of sorting trays by length of list (res2) \n", res)

# reassemble list with new sort based on piece count.

final_output = []
for number in res:
    final_output.append(dict_trays[number])

#pprint(final_output)

with open('sorted_output.csv', 'w', encoding='iso-8859-1', newline='') as f:
    writer = csv.writer(f, delimiter=',')

    # write the header
    for x in headers:
        writer.writerow(x)

    # write the data
    for line in final_output:
        writer.writerows(line)


#print("Output is located at " + os.path.abspath('sorted_output.csv'))
#print("File exists? " + str(os.path.exists('sorted_output.csv')))
