from typing import Tuple

from ..app.mouse_handler import MouseHandler
from .default_widget import DefaultWidget
from .scene_widget import SceneWidget
from ..config import Color, TOOLS_POS, DEFAULT_BUTTON_SIZE
from .button_states import ButtonStates
from ..drawing_tools import DrawingToolInterface
import pygame as pg

class ButtonWidget(DefaultWidget):
    def __init__(
            self, 
            screen: pg.Surface, 
            size: Tuple[int, int], 
            position: Tuple[int, int],
            mouse_handler: MouseHandler,
            drawing_tool: DrawingToolInterface,
            scene_widget: SceneWidget,
            cursor: pg.cursors,
            text_str: str,
    ) -> None:
        super().__init__(screen, size, position, mouse_handler)
        
        self.fill_colors = {
            ButtonStates.NORMAL: Color.WHITE.value,
            ButtonStates.PRESSED: Color.DARK_GRAY.value,
        }
        self.cursor = cursor
        self.drawing_tool = drawing_tool
        self.scene_widget = scene_widget
        self.cur_state = ButtonStates.NORMAL

        position = (position[0] + TOOLS_POS[0], position[1] + TOOLS_POS[1])
        self.rect = pg.Rect(position, size, width=2)
        
        font = pg.font.SysFont('arial', 18)
        self.text = font.render(text_str, True, Color.BLACK.value)

    def set_state(self, new_state: ButtonStates):
        if new_state != self.cur_state and new_state == ButtonStates.PRESSED:
            self.scene_widget.change_drawing_tool(self.drawing_tool)
        self.cur_state = new_state

    def update(self):
        if self.cur_state == ButtonStates.PRESSED:
            pg.mouse.set_cursor(self.cursor)

        self.surface.fill(self.fill_colors[self.cur_state])

        self.surface.blit(
            self.text, 
            (
                0, 
                DEFAULT_BUTTON_SIZE[1] - 20
            )
        )

        self.screen.blit(self.surface, self.position)
