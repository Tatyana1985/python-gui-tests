def test_delete_group(app):
    old_list = app.groups.get_group_list()
    if len(old_list) < 2:
        app.groups.add_new_group("my_group")
    app.groups.delete_group()
    new_list = app.groups.get_group_list()
    if len(old_list)>1:
        old_list.remove(old_list[1])
    assert sorted(old_list) == sorted(new_list)