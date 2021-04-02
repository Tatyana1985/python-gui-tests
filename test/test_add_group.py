from generator.read_from_groups import read_from_groups


def test_add_group(app):
    my_group = read_from_groups()
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(my_group)
    new_list = app.groups.get_group_list()
    old_list.append(my_group)
    assert sorted(old_list) == sorted(new_list)