#!/usr/bin/python3
# 4-hiden_discovery.py

if __name__ == "_main_":
    """print all names defined by hiden_4 module."""
    import hiden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "_":
            print(name)
