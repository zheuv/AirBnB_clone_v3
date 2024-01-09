#!/usr/bin/python3


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.today()
        self.updated_at = self.created_at
    def __str__(self):
        return ("[BaseModel] ({}) {}".format(self.id, self.__dict__))
    def save(self):
        self.updated_at = datetime.datetime.today()
    def to_dict(self):
        dicti = dict()
        dicti["__class__"] = "BaseModel"
        for key in self.__dict__.keys():
            value = getattr(self, key)
            if type(value) is datetime.datetime:
                value = value.isoformat()
            dicti[key] = value
        return dicti

