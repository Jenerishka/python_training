# -*- coding: utf-8 -*-
from model.group import Group


def test_modification_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for test modify group"))
    old_groups = app.group.get_group_list()
    group = Group(name="344fdf", header="dfdf",
                                      footer="sfdfdfew")
    group.id = old_groups[0].id
    app.group.modif_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,
                                                             key=Group.id_or_max)


def test_modification_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for test modify group2"))
    old_groups = app.group.get_group_list()
    group = Group(name="New name")
    group.id = old_groups[0].id
    app.group.modif_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,
                                                             key=Group.id_or_max)


# def test_modification_first_group_header(app):
    # if app.group.count() == 0:
        # app.group.create(Group(name="Group for test modify group3"))
    # old_groups = app.group.get_group_list()
    # app.group.modif_first_group(Group(header="New header"))
    # new_groups = app.group.get_group_list()
    # assert len(old_groups) == len(new_groups)

