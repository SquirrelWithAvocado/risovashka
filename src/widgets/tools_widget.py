from typing import Tuple

from ..app.mouse_handler import MouseHandler
from ..config import TOOLS_SIZE, Color, DEFAULT_BUTTON_SIZE
from .default_widget import DefaultWidget 
from .button_widget import ButtonWidget
from .button_states import ButtonStates
from ..drawing_tools import Pen, Rubber, Cursor
from .scene_widget import SceneWidget
import pygame as pg

class ToolsWidget(DefaultWidget):
    def __init__(
            self, 
            screen: pg.Surface, 
            size: Tuple[int, int], 
            position: Tuple[int, int],
            scene_widget: SceneWidget,
            mouse_handler: MouseHandler,
    ) -> None:
        super().__init__(screen, size, position, mouse_handler)
        self.buttons = {
            'pen': ButtonWidget(
                self.surface, 
                DEFAULT_BUTTON_SIZE, 
                (4, 4), 
                self.mouse_handler, 
                Pen(scene_widget.surface),
                scene_widget,
                pg.cursors.ball,
                "pen"
            ),
            'cursor': ButtonWidget(
                self.surface, 
                DEFAULT_BUTTON_SIZE, 
                (117, 4), 
                self.mouse_handler,  
                Cursor(),
                scene_widget,
                pg.cursors.tri_left,
                "cursor"
            ),
            'rubber': ButtonWidget(
                self.surface, 
                DEFAULT_BUTTON_SIZE, 
                (4, 102), 
                self.mouse_handler,  
                Rubber(scene_widget.surface),
                scene_widget,
                pg.cursors.diamond,
                "rubber"
            )
        }
        self.pressed_button = self.buttons['cursor']
        self.draw_design()
    
    def draw_design(self):
        bounding_rect = self.surface.get_bounding_rect()
        pg.draw.rect(
            self.surface, 
            Color.BLACK.value, 
            bounding_rect,
            4
        )

        pg.draw.line(
            self.surface, 
            Color.BLACK.value,
            (bounding_rect.x + TOOLS_SIZE[0] // 2 - 1, bounding_rect.y),
            (bounding_rect.x + TOOLS_SIZE[0] // 2 - 1, bounding_rect.y + TOOLS_SIZE[1]),
            4
        )

        pg.draw.line(
            self.surface, 
            Color.BLACK.value,
            (bounding_rect.x, bounding_rect.y + TOOLS_SIZE[1] // 2 - 1),
            (bounding_rect.x + TOOLS_SIZE[0], bounding_rect.y + TOOLS_SIZE[1] // 2 - 1),
            4
        )

    def update(self):
        mouse_pos = pg.mouse.get_pos()
        pressed_button = None
        if self.mouse_handler.is_clicked():
            for button in self.buttons.keys():
                if (self.buttons[button].rect.collidepoint(mouse_pos)):          
                    pressed_button = self.buttons[button]
            
        for button in self.buttons.keys():
            if (
                pressed_button and 
                pressed_button == self.buttons[button] and 
                self.click_id == self.mouse_handler.get_click_id() or
                self.pressed_button == self.buttons[button]
            ):
                self.buttons[button].set_state(ButtonStates.PRESSED)
                self.pressed_button = self.buttons[button]
            else:
                self.buttons[button].set_state(ButtonStates.NORMAL)
            self.buttons[button].update()
        
        self.click_id = self.mouse_handler.get_click_id()

        self.screen.blit(self.surface, self.position)
        
        
        