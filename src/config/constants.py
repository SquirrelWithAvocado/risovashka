from enum import Enum

SCREEN_SIZE = (1200, 800)
SCENE_SIZE = (900, 750)
VIDECAM_SIZE = (230, 160)
TOOLS_SIZE = (230, 200)

DEFAULT_BUTTON_SIZE = (109, 94)

SCENE_POS = (25, 25)
VIDEOCAM_POS = (950, 25)
TOOLS_POS = (950, 210)

class Color(Enum):
    GRAY = (128, 128, 128)
    DARK_GRAY = (100, 100, 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 50, 125)