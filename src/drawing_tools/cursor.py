from typing import Tuple
import pygame as pg
from ..config import Color
from .drawing_tool_interface import DrawingToolInterface

class Cursor(DrawingToolInterface):
    def __init__(self) -> None:
        pass
    
    def set_size(self, new_size: int) -> None:
        pass
    
    def set_color(self, new_color: Tuple[int, int, int]) -> None:
        pass
    
    def draw(self, mouse_pos: Tuple[int, int]) -> None:
        pass
