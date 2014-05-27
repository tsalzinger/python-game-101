import sys
import sdl2
import sdl2.ext
from field_drawer import FieldDrawer
from field import Field

__author__ = 'issue'

path = [(0, 0), (5, 5), (7, 7), (10, 10)]  # left upper to lower right
size = (10, 10)
test_field = Field(path, size, entry_point=(2, 2), base=(8, 8))


def run():
    sdl2.ext.init()
    window = sdl2.ext.Window("ToDO", size=(640, 600))
    window.show()
    renderer = sdl2.ext.Renderer(window)
    fd = FieldDrawer(test_field, renderer)
    fd.draw()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
        window.refresh()
    return 0


if __name__ == "__main__":
    sys.exit(run())