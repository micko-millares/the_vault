#### Update Log ####
# 3/6/2020, morseMain2.py created

import pygame
import array

class tone(pygame.mixer.Sound):

    def __init__(self, frequency , volume=.1):
        self.frequency = frequency
        pygame.mixer.Sound.__init__(self, self.build_tone())
        self.set_volume(volume)

    def build_tone(self):
        period = int(round(pygame.mixer.get_init()[0]/self.frequency))
        tones = array.array("h", [0] * period)
        amplitude = 2 ** (abs(pygame.mixer.get_init()[1])-1)-1
        for time in range(period):
            if time < period / 2:
                tones[time] = amplitude
            else:
                tones[time] = -amplitude
            return tones

if __name__ == "__main__":
    # Function drivers/init
    pygame.mixer.pre_init(20000, -16, 1, 512)
    pygame.init()

    screen = pygame.display.set_mode((100, 100))

    # Objects
    tones = {
        pygame.K_KP_ENTER: tone(67)
    }

    # Main loop
    debounce = True

    while debounce == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                debounce = False
    
    #keyPress
            elif event.type == pygame.KEYDOWN:
                 if event.key in tones:
                    #print('Press:', event.key)
                    tones[event.key].play(-1)

     #keyRelease
            elif event.type == pygame.KEYUP:
                 if event.key in tones:
                    #print('Press:', event.key)
                    tones[event.key].stop()

pygame.quit()

