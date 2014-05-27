__author__ = 'issue'
from field import Field


SCALE_FACTOR = 60


def scale(field):
    """
    Scale the game field for drawing
    """

    scaled_path = [(a * SCALE_FACTOR, b * SCALE_FACTOR) for (a, b) in field.path]
    scaled_size = tuple([a * SCALE_FACTOR for a in field.size])
    scaled_entry_point = tuple([a * SCALE_FACTOR for a in field.entry_point])
    scaled_base = tuple([a * SCALE_FACTOR for a in field.base.position])

    return Field(scaled_path, scaled_size, scaled_entry_point, scaled_base)


def _create_rectangle(coords):
    return coords[0], coords[1], 30, 30


class FieldDrawer(object):
    def __init__(self, field, renderer):
        self.scaled_field = scale(field)
        self.renderer = renderer
        self.draw()

    def draw(self):
        """
        Draws the scaled field on a given SDL2 surface
        SDL2 renderer.draw_line wants a tuple and start and end points
        """
        #print(self._create_rectangle())
        self.renderer.draw_rect(_create_rectangle(self.scaled_field.base))
        self.renderer.draw_rect(_create_rectangle(self.scaled_field.entry_point))
        self.renderer.draw_line(self._calculate_path()) # fixed in git version of pysdl2
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






