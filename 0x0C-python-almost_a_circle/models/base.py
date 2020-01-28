#!/usr/bin/python3
"""Base module"""
import json
from os import path


class Base:
    """This is the class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """This method initialize all the instance"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method recive a list of dictionaries
        (python) and converted to a string (json)"""

        if list_dictionaries is None or list_dictionaries == '\0':
            return "[]"
        else:
            return json.dumps(list_dictionaries, ensure_ascii=False)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method save a list of instance into a file,
        this file contain a string (json)"""

        new_list = []
        filename = "{}.json".format(cls.__name__)

        if list_objs is None:
            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(new_list, ensure_ascii=False))
        else:
            for objs in list_objs:
                new_list.append(objs.to_dictionary())

            with open(filename, mode="w", encoding="utf-8") as file:
                file.write(json.dumps(new_list, ensure_ascii=False))

    @staticmethod
    def from_json_string(json_string):
        """This method converted a string (json)
        to list of dictionaries (python)"""

        if json_string is None or json_string == '\0':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method converted a dictionary to instance"""

        if cls.__name__ == "Rectangle":
            instance = cls(7, 7)
        if cls.__name__ == "Square":
            instance = cls(7)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """This method converted a file (json) to a instance"""

        filename = "{}.json".format(cls.__name__)
        new_list = []

        if path.exists(filename):
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = file.read()
                dicty = cls.from_json_string(reader)
                for i in dicty:
                    instance = cls.create(**i)
                    new_list.append(instance)
                return new_list
        else:
            return new_list
