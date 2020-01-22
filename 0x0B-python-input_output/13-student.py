#!/usr/bin/python3


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if isinstance(attrs, list):
            for name in attrs:
                if isinstance(name, str):
                    for dir_names in self.__dict__:
                        if name == dir_names:
                            new_dict[name] = self.__dict__[dir_names]
            return new_dict
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        for dic in json:
            self.__dict__[dic] = json[dic]
