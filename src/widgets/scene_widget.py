from typing import Tuple

from ..app.mouse_handler import MouseHandler
from ..config import SCENE_SIZE, Color
from .default_widget import DefaultWidget
from ..drawing_tools import Pen, Cursor
from ..drawing_tools.drawing_tool_interface import DrawingToolInterface
import pygame as pg


class SceneWidget(DefaultWidget):
    def __init__(
            self, 
            screen: pg.Surface, 
            size: Tuple[int, int], 
            position: Tuple[int, int],
            mouse_handler: MouseHandler
    ) -> None:
        super().__init__(screen, size, position, mouse_handler)
        self.cur_tool = Cursor()

    def change_drawing_tool(self, new_tool: DrawingToolInterface):
        self.cur_tool = new_tool

    def update(self):
        if self.mouse_handler.is_clicked():
            self.cur_tool.draw(pg.mouse.get_pos())

        self.screen.blit(self.surface, self.position)
