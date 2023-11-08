from typing import Tuple
import numpy as np
from ..app.mouse_handler import MouseHandler
from ..config import VIDEOCAM_SIZE, Color, VIDEOCAM_POS, SCREEN_SIZE
from .default_widget import DefaultWidget
from ..hand_tracking import VideoProcessEngine
from ..hand_tracking import GestureStates
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
        self.video_process_engine = VideoProcessEngine()
        self.hand_position_proportions = (0, 0)

    def update(self):
        (frame, self.hand_position_proportions, state) = self.video_process_engine.get_frame()
        image = pg.surfarray.make_surface(np.rot90(frame))
        scaled_image = pg.transform.scale(image, VIDEOCAM_SIZE)
        self.surface.blit(scaled_image, (0, 0))
        self.screen.blit(self.surface, VIDEOCAM_POS)

        if state == GestureStates.POINTS:
            if not self.mouse_handler.is_clicked():
                self.mouse_handler.click()
        else:
            self.mouse_handler.unclick()

        pg.mouse.set_pos(
            SCREEN_SIZE[0] * self.hand_position_proportions[0], 
            SCREEN_SIZE[1] * self.hand_position_proportions[1]
        )

    def release(self):
        self.video_process_engine.release()