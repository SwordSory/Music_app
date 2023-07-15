import pygame
from pygame.locals import *
import os
import random
from mutagen.mp3 import MP3

pygame.init()


screen = pygame.display.set_mode((525, 675))
pygame.display.set_caption("M25")
pmfont = pygame.font.Font(None, 80)
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()



def assects_pather(filename):
    asfp = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("Assects"))
    return (os.path.join(asfp, filename))



bg_img = pygame.image.load(assects_pather("Bg.jpg"))
bg_img = pygame.transform.scale(bg_img, (525, 675))
footer_bg = pygame.image.load(assects_pather("footer.png"))
footer_bg = pygame.transform.scale(footer_bg, (525, 675))


play_b = pygame.image.load(assects_pather("shuffle.png"))
play_b = pygame.transform.scale(play_b, (127.5, 127.5))
shuffle_color = (173, 216, 230)
playrect = pygame.Rect(198.75, 525, 127.5, 127.5)


p_b_clicked = False
paused = False
loop = False
playing = False
loop_pause = False
play = False
loop_count = 0
pause_count = 0
song_length = 0
sp = 0

running = True
while running:
    for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == VIDEORESIZE:
                pygame.display.set_mode((s_w, s_h))



    screen.blit(bg_img, (0, 0))
    screen.blit(footer_bg, (0, 0))
    pygame.draw.circle(screen, shuffle_color, (262.5, 589), 67.5, 100)
    screen.blit(play_b, (198.75, 525))



    pygame.display.flip()
    clock.tick(60)

pygame.quit()