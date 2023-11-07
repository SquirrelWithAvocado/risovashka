from abc import ABC, abstractmethod
from typing import Tuple

class DrawingToolInterface(ABC):
    @abstractmethod
    def draw(self, mouse_pos: Tuple[int, int]) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    def set_size(self, new_size: int) -> None:
        raise NotImplementedError()

    @abstractmethod
    def set_color(self, new_color: Tuple[int, int, int]) -> None:
        raise NotImplementedError()
