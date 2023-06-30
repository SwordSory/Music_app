import pygame

def play_audio(file_path):
    # Initialize pygame
        pygame.init()

        # Load the audio file
        pygame.mixer.music.load(file_path)

        # Play the audio file
        pygame.mixer.music.play()

        while True:
            user_input = input("Enter 'p' to pause, 'r' to resume, 'q' to quit: ")

            if user_input == "p":
                # Pause audio playback
                pygame.mixer.music.pause()
                print("Audio paused.")
            elif user_input == "r":
                # Resume audio playback
                pygame.mixer.music.unpause()
                print("Audio resumed.")
            elif user_input == "q":
                # Stop audio playback and quit
                pygame.mixer.music.stop()
                print("Audio stopped. Quitting...")
                break

        # Quit pygame
        pygame.quit()

# Play the audio (replace "audio.mp3" with your audio file path)
play_audio("/home/no/Code/Music/4.mp3")
