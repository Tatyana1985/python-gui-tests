from comtypes.client import CreateObject
import os
import random

def read_from_groups():
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    xl = CreateObject("Excel.Application")
    book = xl.Workbooks.Open(os.path.join(project_dir, "groups.xlsx"))
    row = book.Worksheets(1).UsedRange.Rows.Count
    num = random.randrange(row)
    my_group = xl.Range["A%s" % str(num)].Value[()]
    xl.Quit()
    return my_group

