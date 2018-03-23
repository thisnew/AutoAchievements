
# coding=utf-8

from openpyxl import load_workbook


wb = load_workbook('')
sheet = wb.get_sheet_by_name("第一营业部")

for i in range(2, tabRow):
    myadd.click()
print("add done")

for i in range(1, tabRow):
    print(i)