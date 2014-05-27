import sys

import libs.sdl2 as sdl2
import libs.sdl2.ext

from field_drawer import FieldDrawer
from field import Field
from base_entity import BaseEntity
__author__ = 'issue'

path = [(0, 0), (2, 3), (3, 7), (10, 10)]  # left upper to lower right
size = (10, 10)
base_point = (6, 6)
base = BaseEntity(100, 0, "BASE", "Your base", base_point, 2, 3, 5, (2, 2))

test_field = Field(path, size, entry_point=(2, 2), base=base)


def run():
    libs.sdl2.ext.init()
    window = libs.sdl2.ext.Window("ToDO", size=(640, 600))
    window.show()
    renderer = libs.sdl2.ext.Renderer(window)
    fd = FieldDrawer(test_field, renderer)
    fd.draw()

    running = True
    while running:
        events = libs.sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    return 0


if __name__ == "__main__":
    sys.exit(run())