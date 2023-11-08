from typing import Tuple
from ..config import SCENE_SIZE, Color
from ..app.mouse_handler import MouseHandler

import pygame as pg

class DefaultWidget:
    def __init__(
            self, 
            screen: pg.Surface, 
            size: Tuple[int, int], 
            position: Tuple[int, int],
            mouse_handler: MouseHandler
    ) -> None:
        self.surface = pg.Surface(size)
        self.position = position
        self.screen = screen
        self.surface.fill(Color.WHITE.value)
        self.mouse_handler = mouse_handler
        self.click_id = self.mouse_handler.get_click_id()
        self.draw_design()
    
    def draw_design(self):
        bounding_rect = self.surface.get_bounding_rect()
        pg.draw.rect(
            self.surface, 
            Color.BLACK.value, 
            bounding_rect,
            4
        )
    
    def update(self):
        self.screen.blit(self.surface, self.position)
        self.click_id = self.mouse_handler.get_click_id()

    def release(self):
        pass