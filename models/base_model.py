#!/usr/bin/python3
"""
The base model
"""


from datetime import datetime
import uuid


class BaseModel:
    """Defining all common attributues and methods.
    id: string - assign with an uuid when an instance is ceated
    created_at: assigning with current datetime
    updated_at: assigning with current datetime

    __str__: prints the [<class name>] (<self.id>) <self.__dict__>
    save(self): updates the public instance attribute updated_at
    to_dict(self): returns a dictionary containing all keys
    """

    def __init__(self):
        """Public instance attributes for the Class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Should print some attributes"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updating updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary containing all keys/values"""
        object_dict = self.__dict__.copy()
        object_dict['__class__'] = self.__class__.__name__
        object_dict['created_at'] = self.created_at.isoformat()
        object_dict['updated_at'] = self.updated_at.isoformat()
        return object_dict
