#!/usr/bin/python3
"""
Write a class LockedClass with no class or object attribute
"""


class LockedClass:
    def __setattr__(self, name, value):
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError("You cannot create new instance attributes for LockedClass")

locked_obj = LockedClass()
locked_obj.first_name = "John"
print(locked_obj.first_name)

locked_obj.last_name = "Doe"
