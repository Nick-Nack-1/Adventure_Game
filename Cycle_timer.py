import time
import pygame

class timer():
    def __init__(self,scn):
        ##By calling init you start this timer
        pygame.font.init()
        self.start = time.perf_counter()
        self.time = 0
        self.screen = scn
        self.font1 = pygame.font.SysFont("Amasis MT Pro Light",15)

        self.counter = 0
        self.average_sum = 0
        self.average = 0
    

    def stop(self):
        self.time = time.perf_counter()-self.start
        self.start = time.perf_counter()

        if self.counter != 0 and self.counter % 20 == 0:
            self.average = self.average_sum / 20
            self.average_sum = 0
        else:
            self.average_sum += self.time

        text = self.font1.render("- Speed: "+str(int(self.time*1000))+" ms", 1,(255,255,255))
        self.screen.blit(text, (0, 3))
        text2 = self.font1.render("- Avg_speed: "+str(int(self.average*1000))+" ms", 1,(255,255,255))
        self.screen.blit(text2, (0, 13))

        self.counter += 1