# Faça um programa em Python que abra e reproduza um arquivo mp3

import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load('nome_do_arquivo.mp3')

# Inicia a reprodução
pygame.mixer.music.play()

# Aguarda o usuário para encerrar
input("Pressione Enter para parar a música...")
