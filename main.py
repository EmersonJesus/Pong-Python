import pygame as pg
from pygame.locals import *
import sys

# Classe bola
class Bola:
    def __init__(self, tela, cor, posX, posY, raio):
        self.tela = tela
        self.cor = cor 
        self.posX = posX
        self.posY = posY
        self.raio = raio
        self.desenha_bola()
    
    def desenha_bola(self):
        pg.draw.circle(self.tela, self.cor, (self.posX, self.posY), self.raio)
        

pg.init()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)

# Configurações da tela
largura = 900
altura = 500
tamanho_tela = (largura, altura)
tela = pg.display.set_mode(tamanho_tela)
pg.display.set_caption('PONG')

def quadra():
    tela.fill(preto)
    pg.draw.line(tela, branco, (largura//2, 0), (largura//2, altura), 5)

quadra()

# Criando os objetos
bola = Bola(tela, branco, largura//2, altura//2, 15)

# Loop do jogo
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            
    pg.display.update()