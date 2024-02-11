#!/usr/bin/python3
"""Define the BaseModel class"""
import models
from uuid import uuid4
from datetime import datetime



class BaseModel:
    """"Represents the BaseModel of the HBnB project."""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")        
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        from models import storage
        """ updates instance attributes with current datetime"""
        self.updated_at = datetime.utcnow()
        #from models.engine.file_storage import storage
        storage.new(self)
        storage.save()
    def to_dict(self):
        """Convert instance into dict format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict