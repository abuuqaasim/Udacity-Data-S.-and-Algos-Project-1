#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:49:57 2019

@author: joscelynec
"""

# Your work here
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name



def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    #check the group's immediate visible users
    users = group.get_users()
    if user in users:
        return True
    else:
        #now recurse through the group's groups
        group_list = group.get_groups()
        for item in group_list:
            return is_user_in_group(user, item)
    return False

print("""**** Group with no Users test ****""")
empty_grp = Group("empty")
user = "user"
print(empty_grp.get_name(), "group has user?", is_user_in_group(user, empty_grp))
print("""*******************************""")

print("""**** Group with several users test ****""")
grp = Group("test_grp")
user1 = "user1"
user2 = "user2"
user3 = "user3"
user4 = "user4"
grp.add_user(user1)
grp.add_user(user2)
grp.add_user(user3)
print(grp.get_name(), "group have user1?", is_user_in_group(user1, grp))
print(grp.get_name(), "group have user2?", is_user_in_group(user2, grp))
print(grp.get_name(), "group have user3?", is_user_in_group(user3, grp))
print(grp.get_name(), "group have user4?", is_user_in_group(user4, grp))
print("""*******************************""")

"""**** Udacity Test Code ****"""        
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child_user_a = "sub_child_user_a"


child.add_group(sub_child)
parent.add_group(child)

print("****Udacity Test Code****")
print(parent.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, parent))
print(child.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, child))
print(sub_child.get_name(),"group has sub_child_user?",is_user_in_group(sub_child_user, sub_child))
print(parent.get_name(),"group has sub_child_user_a?",is_user_in_group(sub_child_user_a, parent))


"""
**************  End of Program  *****************
"""
"""
*** Group with no Users test ****
empty group has user? False
*******************************
**** Group with several users test ****
test_grp group have user1? True
test_grp group have user2? True
test_grp group have user3? True
test_grp group have user4? False
*******************************
****Udacity Test Code****
parent group has sub_child_user? True
child group has sub_child_user? True
subchild group has sub_child_user? True
parent group has sub_child_user_a? False
"""




