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
        
class Raquete:
    def __init__(self, tela, cor, posX, PosY, largura, altura):
        self.tela = tela
        self.cor = cor
        self.posX = posX
        self.PosY = PosY
        self.largura = largura
        self.altura = altura
        self.desenha_raquete()
        
    def desenha_raquete(self):
        pg.draw.rect(self.tela, self.cor, (self.posX, self.PosY, self.largura, self.altura))

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
raquete1 = Raquete(tela, branco, 15, altura//2-60, 20, 120)
raquete2 = Raquete(tela, branco, largura-20-15, altura//2-60, 20, 120)

# Loop do jogo
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
            
    pg.display.update()