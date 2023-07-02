import pygame
from pygame.locals import *
import os
import random


pygame.init()

screen = pygame.display.set_mode((700, 900))
pygame.display.set_caption("Shuffler")
pmfont = pygame.font.Font(None, 80)
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()

volume = 0.8




def assects_pather(filename):
    asfp = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("Assects"))
    return (os.path.join(asfp, filename))


bg_img = pygame.image.load(assects_pather("Bg.jpg"))
footer_bg = pygame.image.load(assects_pather("footer.png")) 

pb = pygame.image.load(assects_pather("shuffle.png"))
p_b = pygame.transform.scale(pb, (170,170))
shuffle_color = (173, 216, 230)
playrect = pygame.Rect(265, 700, 170, 170)

pab = pygame.image.load(assects_pather("pause.png"))
pa_b = pygame.transform.scale(pab, (100, 100))
pt = pygame.image.load(assects_pather("circle.png"))
ptt = pygame.transform.scale(pt, (110, 110))
pauserect = pygame.Rect(145, 735, 100, 100)

rb = pygame.image.load(assects_pather("play.png"))
r_b = pygame.transform.scale(rb, (100,100))

lb = pygame.image.load(assects_pather("loop.png"))
l_b = pygame.transform.scale(lb , (120, 120))
looprect = pygame.Rect(10, 725, 120, 120)

loop_true = pygame.image.load(assects_pather("circle.png"))
lt = pygame.transform.scale(loop_true, (120, 120))

stop = pygame.image.load(assects_pather("stop.png"))
s_b = pygame.transform.scale(stop, (120, 120))
stoprect = pygame.Rect(570 , 725, 120, 120)


vol_plus = pygame.Rect(500, 700, 50, 50)
vp = pygame.Rect(500, 700, 50, 50)
plus = pmfont.render("+", True, "White")

vol_minus = pygame.Rect(500, 825, 50, 50)
vm = pygame.Rect(500, 825, 50, 50)
minus = pmfont.render("–", True, "White")


active_song = "NONE"
Playing_text = "PLAYING:- "
what_playing_rect = pygame.Rect(0, 580, 700, 70)
wp_border = pygame.Rect(0, 580, 700, 70)
pt_render = font.render(Playing_text, True, (255, 215, 0))


p_b_clicked = False
paused = False
loop = False
playing = False
loop_pause = False
play = False
loop_count = 0
pause_count = 0
songs_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("Songs"))



def mp3_player(random_file):
    global active_song
    pygame.mixer.init()
    pygame.mixer.music.load(random_file)
    pygame.mixer.music.play()

    if pygame.mixer.music.get_busy() or paused == True:
            active_songg = (os.path.basename(random_file))
            namee, extensionn = os.path.splitext(active_songg)
            active_song = namee

    p_b_clicked = True
    


def randomize():
    while True:
        folder_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("Songs"))
        file_list = os.listdir(folder_path)
        randomizer = random.choice(file_list)
        randomized_file_path = os.path.join(folder_path, randomizer)
            
        if os.path.splitext(randomized_file_path)[1] == ".mp3":
            return (randomized_file_path)     
            break  
        elif os.path.splitext(randomized_file_path)[1] != ".mp3":
            os.remove(randomized_file_path)            


running = True
while running:

    
    try: 
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == VIDEORESIZE:
                pygame.display.set_mode((700, 900))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if playrect.collidepoint(pos) and event.button == 1 and not p_b_clicked and not paused:
                    play = True
                    mp3_player(randomize())

                            
                elif pauserect.collidepoint(pos) and event.button == 1:
                    if pygame.mixer.music.get_busy() or pause_count%2 != 0:
                        pause_count += 1

                    if pause_count%2 != 0:
                        pygame.mixer.music.pause()
                        paused = True
                        p_b_clicked = False
                    else:
                        pygame.mixer.music.unpause()
                        paused = False

                elif looprect.collidepoint(pos) and event.button == 1:
                    loop_count += 1
                    if loop_count%2 != 0:
                        loop = True
                    else:
                        loop = False
                        play = False
                
                elif stoprect.collidepoint(pos) and event.button == 1:
                    pygame.mixer.music.stop()
                    if paused == True:
                        pause_count += 1
                        paused = False
                    play = False

                elif vol_plus.collidepoint(pos) and event.button == 1:
                    if volume < 1:
                        volume += 0.025

                elif vol_minus.collidepoint(pos) and event.button == 1:
                    if volume > 0:
                        volume -= 0.025
    except:
        pass


    if not os.path.exists(songs_folder):
        os.mkdir(songs_folder)
    
    vol_height = 875 - (volume * 175)
    what_playing = font.render(active_song, True, (255, 215, 0))


    screen.blit(bg_img, (0, 0))
    screen.blit(footer_bg, (0, 0))
    pygame.draw.circle(screen, shuffle_color, (350, 785), 90, 100)
    screen.blit(p_b, (265, 700))
    screen.blit(pa_b, (145, 735))
    screen.blit(l_b, (10, 725))
    screen.blit(s_b, (570, 725))
    pygame.draw.line(screen, "Black", (485, 700), (485, 875), 10)
    pygame.draw.line(screen, "Red", (485, vol_height), (485, 875), 10)
    pygame.draw.circle(screen, "Red" , (486.9, vol_height), 8, 100)
    pygame.draw.circle(screen, (255, 105, 97) , (486.9, vol_height), 8, 2)
    pygame.draw.rect(screen, "Black", vol_plus, 100)
    pygame.draw.rect(screen, "Blue", vp, 5)
    screen.blit(plus, (508, 694))
    pygame.draw.rect(screen, "Black", vol_minus, 100)
    pygame.draw.rect(screen, "Blue", vm, 5)
    screen.blit(minus, (509, 819))
    pygame.draw.rect(screen, "Black", what_playing_rect, 100)
    pygame.draw.rect(screen, "Blue", wp_border, 10)
    screen.blit(pt_render, (15, 600))
    screen.blit(what_playing, (230, 600))
    


    if loop == False and not pygame.mixer.music.get_busy():
        play = False


    if not pygame.mixer.music.get_busy() and p_b_clicked:
        p_b_clicked = False


    with os.scandir(songs_folder) as entries:
        if pygame.mixer.music.get_busy() or paused == True:
            shuffle_color = (255, 105, 97)
            loop_pause = True

        elif not any(entry.is_file() for entry in entries):
            shuffle_color = (255, 255, 0)

        else:
            loop_pause = False
            active_song = "NONE"
            shuffle_color = (173, 216, 230)

    if loop == True:
        screen.blit(lt, (10, 725))

    if paused == True:
        screen.blit(r_b, (145, 735))
        screen.blit(ptt, (140, 730))

    if loop_pause == False and loop == True and paused == False and play == True:
        mp3_player(randomize())

    pygame.mixer.music.set_volume(volume)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()