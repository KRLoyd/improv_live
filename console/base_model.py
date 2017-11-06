#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""
import json
import models
from datetime import datetime
#from models import storage
from uuid import uuid4, UUID


date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """
    BaseModel class

    Attributes:
        id
        created_at
        updated_at
    Functions:
        __init__  Instantiates a BaseModel Object
    """

    def __init__(self, *args, **kwargs):
        """
        __init__
        Instantiation of new BaseModel Object
        """
        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid4())
            if 'created_at' not in kwargs:
                kwargs['created_at'] = datetime.now()
                kwargs['created_at'] = kwargs['created_at'].strftime(date_format)
            else:
                kwargs['created_at'] = datetime.strptime(kwargs['created_at'], date_format)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'], date_format)
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            self.__dict__ = kwargs
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __is_serializable(self, obj):
        """
        __is_serializable(obj)
        Returns True if object is serializable, False if not
        """
        try:
            temp = json.dumps(obj)
            return True
        except:
            return False

    def __str__(self):
        """
        __str__
        Returns string type representation of object instance
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        save()
        Updates instances's updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict()
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        obj_dict = {}
        for key, value in (self.__dict__).items():
            if (self.__is_serializable(value)):
                obj_dict[key] = value
            else:
                if type(value) is datetime:
                    value = value.isoformat()
                obj_dict[key] = str(value)
        obj_dict["__class__"] = type(self).__name__
        return obj_dict
