#!/usr/bin/python3
"""
FileStorage Class of Module Models
"""

from models import base_model, game, prompt


class FileStorage():
    """
    FileStorage Class for storing objects
    """
    __file_path = "./improv_live.json"
    __objects = {}
    classes = {'BaseModel': base_model.BaseModel,
               'Game': game.Game,
               'Prompt': prompt.Prompt}

    def all(self):
        """
        all()
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new(obj)
        Sets in __objects the obj with key of <obj class name>.id
        """
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        save
        Serializes __objects to the JSON file
        path: __file_path
        """
        import json
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(new_dict, file)

    def reload(self):
        """
        reload
        Deserializes the JSON file to __objects if the file exists
        """
        import json
        from models.base_model import BaseModel
        classes = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__file_path,
                      mode="r", encoding="utf-8") as file:
                reloaded = json.load(file)
        except:
            return {}

        for key, value in reloaded.items():
            cls_name = value['__class__']
            FileStorage.__objects[key] = FileStorage.classes[cls_name](**value)
