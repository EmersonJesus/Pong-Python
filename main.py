import pygame as pg
from pygame.locals import *

pg.init()

# Criando a janela ----------------------------------------------------
largura = 700
altura = 500
tela_tamanho = (largura, altura)
tela = pg.display.set_mode(tela_tamanho)
pg.display.set_caption('PONG')

# Cores ----------------------------------------------------------------
preto = (0, 0, 0)
branco = (255, 255, 255)
amarelo = (255, 231, 0)
azul = (31, 77, 171)

# Loop do jogo ---------------------------------------------------------
relogio = pg.time.Clock()
fps = 60
rodando = True

# Linha do meio --------------------------------------------------------
linha_meio = ()

while rodando:
    relogio.tick(fps)
    
    for evento in pg.event.get():
        if evento.type == QUIT:
            rodando = False
    
    tela.fill(azul)
    pg.display.update()

pg.quit()