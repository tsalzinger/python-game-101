__author__ = 'Thomas Scheinecker'

from static_entity import StaticEntity
from string_util import StringUtil

class BaseEntity(StaticEntity):
    def __init__(self, hitpoints, cost, name, description, position, attack_rate, attack_damage, attack_damage_area,
                 size):
        super(BaseEntity, self).__init__(hitpoints, cost, name, description, position, attack_rate, attack_damage,
                                         attack_damage_area, size)


    def __str__(self, *args, **kwargs):
        return '#Base' + StringUtil.dict_to_str(self.__dict__)