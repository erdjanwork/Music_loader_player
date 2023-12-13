import pygame
import time
import load_data

pygame.init()

playlist = load_data.obj_list

pygame.mixer.init()

for song in playlist:
    print()
    print(f"Now playing: {song.singer} - {song.song}")
    pygame.mixer.music.load(song.path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)

pygame.quit()