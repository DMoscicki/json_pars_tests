import json
from pprint import pprint
import win32com.client as win32
import os

json_data = json.loads(open("test1.json", encoding='utf-8').read())
pprint(json_data)

rows = []

for rec in json_data['headers']:
    name_test = rec['properties']['QuickInfo']
    rows.append(name_test)
    print(rows)

rows1 = []
for rec1 in json_data['values']:
    name_test1 = rec1['properties']['Text']
    rows1.append(name_test1)
    print(rows1)

Excel = win32.Dispatch('Excel.Application')
Excel.Visible = True

wb = Excel.Workbooks.Add()
ws = wb.Worksheets(1)
wa = wb.Worksheets(2)
wd = wb.Worksheets(3)

header_labels = rows
text_labels = rows1

row_tracker = 2
column_size = len(header_labels)


for indx, val in enumerate(header_labels):
    ws.Cells(1, indx + 1).Value = val
    wa.Cells(1, indx + 1).Value = val
    wd.Cells(1, indx + 1).Value = val

for lnds, valu in enumerate(text_labels[0:4]):
    ws.Cells(2, lnds + 1).Value = valu
    wa.Cells(2, lnds + 1).Value = valu
    wd.Cells(2, lnds + 1).Value = valu

for indexes, values in enumerate(reversed(text_labels[4:8])):
    ws.Cells(3, indexes + 1).Value = values
    wa.Cells(3, indexes + 1).Value = values
    wd.Cells(3, indexes + 1).Value = values


# for row in rows1[0:4]:
#     ws.Range(
#         ws.Cells(row_tracker, 1),
#         ws.Cells(row_tracker, column_size)
#     ).value = row
#     row_tracker += 1
#     print(row)




