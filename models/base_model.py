#!/usr/bin/env python3
"""
base_model.py
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ BaseModel class """
    def __init__(self, *args, **kwargs):
        """instantiates"""
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """"""
        objdict = self.__dict__.copy()
        objdict['__class__'] = self.__class__.__name__
        objdict['created_at'] = objdict['created_at'].isoformat()
        objdict['updated_at'] = objdict['updated_at'].isoformat()
        return (objdict)
