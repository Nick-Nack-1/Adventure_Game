import pygame

class Mouse():
    def __init__(self):
        self.L_press = False
        self.M_press = False
        self.R_press = False
    
    def pressed(self, button):
        ##button: (str) "Left", "Middle", "Right"
        L_click, M_click, R_click = pygame.mouse.get_pressed(num_buttons=3)
        if button == "Left":
            return L_click
        elif button == "Middle":
            return M_click
        elif button == "Right":
            return R_click
        else:
            print("Unknow button: " + button)
