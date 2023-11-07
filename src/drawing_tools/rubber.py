from typing import Tuple
import pygame as pg
from ..config import Color
from .drawing_tool_interface import DrawingToolInterface

class Rubber(DrawingToolInterface):
    def __init__(self, surface: pg.Surface) -> None:
        self.size = 5
        self.color = Color.WHITE.value
        self.surface = surface
    
    def set_size(self, new_size: int) -> None:
        self.size = new_size
    
    def set_color(self, new_color: Tuple[int, int, int]) -> None:
        pass
    
    def draw(self, mouse_pos: Tuple[int, int]) -> None:
        position = (mouse_pos[0] - 22, mouse_pos[1] - 22)
        pg.draw.circle(self.surface, self.color, position, self.size)