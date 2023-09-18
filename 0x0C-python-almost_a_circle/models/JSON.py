#!usr/bin/python3

"""Update the class Base by adding the class 

The filename must be: <Class name>.csv - example: Rectangle.csv
Has the same behavior as the JSON serialization/deserialization
"""

import csv

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_dictionary(obj):
        if type(obj) is dict:
            return obj
        obj_dict = {}
        for key in obj.__dict__:
            if key.startswith("_"):
                obj_dict[key[1:]] = obj.__dict__[key]
            else:
                obj_dict[key] = obj.__dict__[key]
        return obj_dict

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                obj_dict = cls.to_dictionary(obj)
                if cls.__name__ == "Rectangle":
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        obj_list = []
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(0, 0)
                        obj.id = int(row[0])
                        obj.width = int(row[1])
                        obj.height = int(row[2])
                        obj.x = int(row[3])
                        obj.y = int(row[4])
                    elif cls.__name__ == "Square":
                        obj = cls(0)
                        obj.id = int(row[0])
                        obj.size = int(row[1])
                        obj.x = int(row[2])
                        obj.y = int(row[3])
                    obj_list.append(obj)
            return obj_list
        except FileNotFoundError:
            return []

if __name__ == "__main__":
    pass
