from typing import Tuple
import cv2
import mediapipe as mp
import numpy as np
from .gesture_states import GestureStates


class VideoProcessEngine:
    def __init__(self) -> None:
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_hands = mp.solutions.hands

        self.hands_object = self.mp_hands.Hands(
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5)

        self.video_capture = cv2.VideoCapture(0)

    def get_frame(self) -> Tuple[np.ndarray, Tuple[float, float], GestureStates]:
        if self.video_capture.isOpened():
            success, image = self.video_capture.read()
        if not success:
            print("Ignoring empty camera frame.")

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands_object.process(image)

        image.flags.writeable = True
        coord_proportions = (0.0, 0.0)
        state = GestureStates.DEFAULT
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS,
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )
                
                index_tip = hand_landmarks.landmark[8]

                if (index_tip.y < hand_landmarks.landmark[12].y and
                    index_tip.y < hand_landmarks.landmark[16].y
                ):
                    state = GestureStates.POINTS

                coord_proportions = (
                    1 - round(hand_landmarks.landmark[9].x, 3), 
                    round(hand_landmarks.landmark[9].y, 3)
                )
        return image, coord_proportions, state

    def release(self):
        self.hands_object.release()
        self.video_capture.release()
