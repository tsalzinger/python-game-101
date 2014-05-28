import os
import sys

import libs.sdl2 as sdl2
import libs.sdl2.ext
from libs.sdl2 import sdlimage

from field_drawer import FieldDrawer
from field import Field
from base_entity import BaseEntity
from libs.sdl2.video import SDL_WINDOW_RESIZABLE

__author__ = 'issue'

WINDOW_SIZE = (1500, 520)
path = [(0, 0), (1, 2), (2, 1), (3, 7), (10, 10)]  # left upper to lower right
size = (10, 10)
base_point = (3, 7)
base = BaseEntity(100, 0, "BASE", "Your base", base_point, 2, 3, 5, (2, 2))

test_field = Field(path, size, entry_point=(0, 0), base=base)


def run():
    libs.sdl2.ext.init()
    window = libs.sdl2.ext.Window("ToDO", WINDOW_SIZE, flags=SDL_WINDOW_RESIZABLE)
    window.show()

    renderer = libs.sdl2.ext.Renderer(window)
    fd = FieldDrawer(test_field, renderer, WINDOW_SIZE)

    running = True
    while running:
        renderer.clear()
        fd.draw()
        events = libs.sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    return 0


if __name__ == "__main__":
    sys.exit(run())