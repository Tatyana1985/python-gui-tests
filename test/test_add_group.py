from comtypes.client import CreateObject
import os
import random

def test_add_group(app):
    project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    xl = CreateObject("Excel.Application")
    book = xl.Workbooks.Open(os.path.join(project_dir, "groups.xlsx"))
    row = book.Worksheets(1).UsedRange.Rows.Count
    num = random.randrange(row)
    my_group = xl.Range["A%s" % str(num)].Value[()]
    xl.Quit()

    old_list = app.groups.get_group_list()
    app.groups.add_new_group(my_group)
    new_list = app.groups.get_group_list()
    old_list.append(my_group)
    assert sorted(old_list) == sorted(new_list)