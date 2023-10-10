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
        self.dx = 0
        self.dy = 0
        self.desenha_bola()
    
    def desenha_bola(self):
        pg.draw.circle(self.tela, self.cor, (self.posX, self.posY), self.raio)
        
    def iniciar_movimento(self):
        self.dx = 10
        self.dy = 5
    
    def movimento(self):
        self.posX += self.dx
        self.posY += self.dy
    
class Raquete:
    def __init__(self, tela, cor, posX, PosY, largura, altura):
        self.tela = tela
        self.cor = cor
        self.posX = posX
        self.posY = PosY
        self.largura = largura
        self.altura = altura
        self.estado = 'parar'
        self.desenha_raquete()
        
    def desenha_raquete(self):
        pg.draw.rect(self.tela, self.cor, (self.posX, self.posY, self.largura, self.altura))
        
    def mover(self):
        if self.estado == 'cima':
            self.posY -= 10
        elif self.estado == 'baixo':
            self.posY += 10

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

# Variaveis
jogando = False

# Loop do jogo
while True:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
        
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_SPACE and not jogando:
                bola.iniciar_movimento()
                jogando = True
                
            if evento.key == pg.K_w:
                raquete1.estado = 'cima'
            if evento.key == pg.K_s:
                raquete1.estado = 'baixo'
            if evento.key == pg.K_UP:
                raquete2.estado = 'cima'
            if evento.key == pg.K_DOWN:
                raquete2.estado = 'baixo'
                
        if evento.type == pg.KEYUP:
            raquete1.estado = 'parar'
            raquete2.estado = 'parar'
                
    if jogando:
        quadra()
        
        # Movimento da bola
        bola.movimento()
        bola.desenha_bola()
        
        # Raquete 1
        raquete1.mover()
        raquete1.desenha_raquete()
        
        # Raquete 2
        raquete2.mover()
        raquete2.desenha_raquete()
    
    pg.display.update()