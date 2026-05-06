#Exercicio 20
#Faça um programa que toca uma musica (arquivo mp3) quando executado
import pygame
import time

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("ex20.mp3")
pygame.mixer.music.play()

#Maneter o programa rodando enquanto a musica toca

while pygame.mixer.music.get_busy():
    time.sleep(1)