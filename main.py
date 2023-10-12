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
        self.dx = 1
        self.dy = 1
    
    def movimento(self):
        self.posX += self.dx
        self.posY += self.dy
        
    def colisao_raquete(self):
        self.dx = -self.dx
    
    def colisao_parede(self):
        self.dy = -self.dy
    
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
            
    def limite(self):
        if self.posY <= 0:
            self.posY = 0
        elif self.posY + self.altura >= altura:
            self.posY = altura - self.altura

class Pontos:
    def __init__(self, tela, pontos, posX, posY):
        self.tela = tela
        self.pontos = pontos
        self.posX = posX
        self.posY = posY
        self.fonte = pg.font.SysFont("monospace", 80, bold=True)
        self.label = self.fonte.render(self.pontos, 0, branco)
        self.mostrar()
    
    def mostrar(self):
        self.tela.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))

class Controle_Colisao:
    def entre_bola_raquete1(self, bola, raquete1):
        if bola.posY + bola.raio > raquete1.posY and bola.posY - bola.raio < raquete1.posY + raquete1.altura:
            if bola.posX - bola.raio <= raquete1.posX + raquete1.altura:
                return True
        return False
    
    def entre_bola_raquete2(self, bola, raquete2):
        if bola.posY + bola.raio > raquete2.posY and bola.posY - bola.raio < raquete2.posY + raquete2.altura:
            if bola.posX + bola.raio <= raquete2.posX:
                return True
        return False
    
    def entre_bola_paredes(self, bola):
        # Topo
        if bola.posY - bola.raio <= 0:
            return True
        # Em baixo
        if bola.posY + bola.raio >= altura:
            return True
        
        return False

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
colisao = Controle_Colisao()
pontos1 = Pontos(tela, '0', largura//4, 15)
pontos2 = Pontos(tela, '0', largura-largura//4, 15)

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
        raquete1.limite()
        raquete1.desenha_raquete()
        
        # Raquete 2
        raquete2.mover()
        raquete2.limite()
        raquete2.desenha_raquete()
    
        # Checa colisões
        if colisao.entre_bola_raquete1(bola, raquete1):
            bola.colisao_raquete()
            
        if colisao.entre_bola_raquete2(bola, raquete2):
            bola.colisao_raquete()
        
        if colisao.entre_bola_paredes(bola):
            bola.colisao_parede()
        
    pg.display.update()