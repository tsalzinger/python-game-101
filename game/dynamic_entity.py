__author__ = 'issue'

from game_entity import GameEntity


class DynamicEntity(GameEntity):
    def __init__(self, movement_rate, hitpoints, cost, name, description, position, attack_rate, attack_damage,
                 attack_damage_area):
        super(DynamicEntity, self).__init__(hitpoints, cost, name, description, position, attack_rate, attack_damage,
                                            attack_damage_area)
        self.movement_rate = movement_rate