from typing import Tuple

from ..app.mouse_handler import MouseHandler
from ..config import VIDECAM_SIZE, Color
from .default_widget import DefaultWidget
import pygame as pg

class VideoCamWidget(DefaultWidget):
    def __init__(
            self, 
            screen: pg.Surface, 
            size: Tuple[int, int], 
            position: Tuple[int, int],
            mouse_handler: MouseHandler
    ) -> None:
        super().__init__(screen, size, position, mouse_handler)
