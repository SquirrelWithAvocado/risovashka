class MouseHandler:
    def __init__(self) -> None:
        self.__mouse_clicked = False
        self.__click_id = 0
    
    def is_clicked(self):
        return self.__mouse_clicked
    
    def click(self):
        self.__click_id = (self.__click_id + 1) % 2
        self.__mouse_clicked = True
    
    def get_click_id(self):
        return self.__click_id

    def unclick(self):
        self.__mouse_clicked = False
    
        