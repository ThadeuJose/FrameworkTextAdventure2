"""Basic framework objects"""
from Framework.Exceptions import EmptyStringException

__author__ = 'Thadeu Jose'


class TextObject(object):
    """Basic object of the framework
    Name and Description cant be empty string
    """

    def __init__(self, name, description):
        self._name = None
        self._description = None
        self.status = dict()
        self.name = name
        self.description = description

    @property
    def name(self):
        """The name of the object
        Use to index in the framework
        """
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            raise EmptyStringException('name')

    @property
    def description(self):
        """Describe the object
        Cant be empty string
        """
        return self._description

    @description.setter
    def description(self, value):
        if value:
            self._description = value
        else:
            raise EmptyStringException('description')

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not __eq__(self, other)

    def __str__(self):
        return self._name+"\n"+self._description

    def getstatus(self, idx):
        return self.status[idx]

    def setstatus(self, idx, value):
        self.status[idx] = value

    def hasstatus(self, idx):
        return idx in self.status

