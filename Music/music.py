import os
import random
from moviepy.editor import VideoFileClip
import pygame
import threading



def player(randomized_file_path):
    
    pygame.init()
    pygame.mixer.init()
    
    if os.path.splitext(randomized_file_path)[1] == ".mp3":
        pygame.mixer.music.load(randomized_file_path)
        pygame.mixer.music.play()
        pygame.event.wait()
        player(randomized_file_path)



def user_input():
    while True:
        command = input("Commands:- (play/pause/resume/quit/skip): ").lower()

        if command == "play":
            player()
        elif command == "pause":
            pygame.mixer.music.pause()
        elif command == "resume":
            pygame.mixer.music.unpause()
        elif command == "skip":
            pygame.mixer.quit()
            player()
        elif command == "quit":
            pygame.mixer.music.stop()
            break
        else:
            print("Invalid command.")


folder_path = os.path.dirname(os.path.realpath(__file__))
file_list = os.listdir(folder_path)
randomizer = random.choice(file_list)
randomized_file_path = os.path.join(folder_path, randomizer)



audio_thread = threading.Thread(target=player, args=(randomized_file_path,))
audio_thread.start()

user_input()