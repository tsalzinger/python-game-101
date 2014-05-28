import os
from base_entity import BaseEntity
from field import Field
import libs.sdl2.ext as sdl2ext
import sdl2

__author__ = 'issue'

SCALE_FACTOR = 60

game_path = os.path.dirname(os.path.abspath(__file__))
resources = sdl2ext.Resources(os.path.join(game_path, "resources"))


def scale(field):
    """
    Scale the game field for drawing
    """

    scaled_path = [(a * SCALE_FACTOR, b * SCALE_FACTOR) for (a, b) in field.path]
    scaled_size = tuple([a * SCALE_FACTOR for a in field.size])
    scaled_entry_point = tuple([a * SCALE_FACTOR for a in field.entry_point])
    scaled_base = tuple([a * SCALE_FACTOR for a in field.base.position])
    tmp_base = field.base

    tmp_base.position = scaled_base

    return Field(scaled_path, scaled_size, scaled_entry_point, tmp_base)


def _create_rectangle(coords):
    return coords[0], coords[1], 30, 30


class FieldDrawer(object):
    def __init__(self, field, renderer, window_size):
        self.scaled_field = scale(field)
        self.renderer = renderer
        self.window_size = window_size

        self.sp_factory = sdl2ext.SpriteFactory(sdl2ext.TEXTURE, renderer=self.renderer)
        self.base_sp = self.sp_factory.from_image(resources.get_path("house.png"))
        self.tower_sp = self.sp_factory.from_image(resources.get_path("tower.png"))
        self.back_ground_sp = self.sp_factory.from_image(resources.get_path("grass.png"))
        self.entry_sp = self.sp_factory.from_image(resources.get_path("red.png"))
        self.grass_rect = (0, 0, 600, 600)
        self.tower_rect = (200, 300, 32, 32)
        self.entry_rect = (self.scaled_field.entry_point[0], self.scaled_field.entry_point[1], 32, 32)
        self.base_rect = (self.scaled_field.base.position[0], self.scaled_field.base.position[1], 32, 32)

        self.draw()


    def draw(self):
        """
        Draws the scaled field on a given SDL2 surface
        SDL2 renderer.draw_line wants a tuple and start and end points
        components of the game field are blitted onto the renderer
        """

        self.renderer.copy(self.back_ground_sp, dstrect=self.grass_rect)
        self.renderer.copy(self.tower_sp, dstrect=self.tower_rect)
        self.renderer.copy(self.base_sp, dstrect=self.base_rect)
        self.renderer.copy(self.entry_sp, dstrect=self.entry_rect)
        #self.renderer.draw_rect(_create_rectangle(self.scaled_field.base))
        #self.renderer.draw_rect(_create_rectangle(self.scaled_field.entry_point))
        self.renderer.draw_line(self._calculate_path())  # fixed in git version of pysdl2
        self.renderer.present()


    def _calculate_path(self):
        """
        Path needs to have an start point and end point for every line to draw
        """
        new_path = ()
        for elem in self.scaled_field.path:
            thiselem = elem
            try:
                nextelem = self.scaled_field.path[self.scaled_field.path.index(elem) + 1]
            except IndexError as e:
                break
            new = thiselem + nextelem
            new_path = new_path + new
        return new_path






