#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
class BaseModel:
    """Represents the BaseModel of the HBnB project."""
    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    def save(self):
        """updates instance attributes with current datetime"""
        self.updated_at = datetime.utcnow()
    def to_dict(self):
        """Convert instance into dict format"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

