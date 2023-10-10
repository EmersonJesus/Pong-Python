import pygame as pg
from pygame.locals import *
import sys

pg.init()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)

# Configurações da tela
largura = 900
altura = 500
tamanho_tela = (largura, altura)
tela = pg.display.set_mode(tamanho_tela)
tela.fill(preto)
pg.display.set_caption('PONG')

# Loop do jogo
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            
    pg.display.update()