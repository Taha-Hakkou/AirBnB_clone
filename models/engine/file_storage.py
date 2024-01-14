#!/usr/bin/env python3
"""
file_storage.py
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class FileStorage:
    """"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        'returns the dictionary __objects'
        return (FileStorage.__objects)

    def new(self, obj):
        'sets in __objects the obj with key <obj class name>.id'
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        'serializes __objects to the JSON file (path: __file_path)'
        with open(FileStorage.__file_path, 'w+', encoding='utf-8') as file:
            json.dump({k: v.to_dict() for k, v in FileStorage.__objects.items()}, file)

    def reload(self):
        'deserializes the JSON file to __objects if JSON file __file_path exists'
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                FileStorage.__objects = {k: eval(v["__class__"])(**v) for k, v in json.load(file).items()}
        except:
            pass
