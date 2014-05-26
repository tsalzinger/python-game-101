__author__ = 'issue'
from static_entity import StaticEntity
from string_util import StringUtil


class Field(object):
    def __init__(self, path, size, entry_point,base):
        """
        :param path: list of tuple
        :param size: tuple
        :param entry_point: tuple
        :param base: StaticEntity
        """
        self.path = path
        self.size = size
        self.entry_point = entry_point
        self.base = base

    def __str__(self, *args, **kwargs):
        return '#Field' + StringUtil.dict_to_str(self.__dict__)




