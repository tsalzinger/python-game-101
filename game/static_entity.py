__author__ = 'issue'

from game_entity import GameEntity
from string_util import StringUtil


class StaticEntity(GameEntity):
    def __init__(self, hitpoints, cost, name, description, position, attack_rate, attack_damage, attack_damage_area,
                 size):
        super(StaticEntity, self).__init__(hitpoints, cost, name, description, position, attack_rate, attack_damage,
                                           attack_damage_area)
        self.size = size


    def __str__(self, *args, **kwargs):
        return '#StaticEntity' + StringUtil.dict_to_str(self.__dict__)

