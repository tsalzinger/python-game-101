__author__ = 'issue'
from static_entity import StaticEntity


class Field(object):
    def __init__(self, path, size, entry_point, base):
        self.path = path
        self.size = size
        self.entry_point = entry_point
        self.base = base


