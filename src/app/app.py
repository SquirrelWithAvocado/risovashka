import cv2 as cv
import pygame as pg
from ..config import (
    Color,
    SCREEN_SIZE,
    SCENE_SIZE,
    VIDECAM_SIZE,
    TOOLS_SIZE,
    SCENE_POS,
    VIDEOCAM_POS,
    TOOLS_POS
)

from .mouse_handler import MouseHandler

from ..widgets import SceneWidget, VideoCamWidget, ToolsWidget


class App:
    def __init__(self) -> None:
        self.is_running = True
        self.window_name = "Risovashka"

        pg.init()
        self.screen = pg.display.set_mode(SCREEN_SIZE)

        self.mouse_handler = MouseHandler()
        self.scene_widget = SceneWidget(
            self.screen, 
            SCENE_SIZE, 
            SCENE_POS, 
            self.mouse_handler
        )
        self.videocam_widget = VideoCamWidget(
            self.screen, 
            VIDECAM_SIZE, 
            VIDEOCAM_POS, 
            self.mouse_handler
        )
        self.tools_widget = ToolsWidget(
            self.screen, 
            TOOLS_SIZE, 
            TOOLS_POS, 
            self.scene_widget,
            self.mouse_handler
        )

        self.cur_widget = self.scene_widget

        
        pg.mouse.set_cursor(pg.cursors.tri_left)

    def run(self):
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    self.mouse_handler.click()
                if event.type == pg.MOUSEBUTTONUP:
                    self.mouse_handler.unclick()

            self.screen.fill(Color.GRAY.value)
            self.scene_widget.update()
            self.videocam_widget.update()
            self.tools_widget.update()

            pg.display.update()
