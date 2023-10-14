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
        self.dx = 7
        self.dy = 7
    
    def movimento(self):
        self.posX += self.dx
        self.posY += self.dy
        
    def colisao_raquete(self):
        self.dx = -self.dx
    
    def colisao_parede(self):
        self.dy = -self.dy
        
    def reinicia_pos(self):
        self.posX = largura//2
        self.posY = altura//2
        self.dx = 7
        self.dy = 7
        self.desenha_bola()
    
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
            
    def reinicia_pos(self):
        self.posY = altura//2 - self.altura//2
        self.estado = 'parar'
        self.desenha_raquete()

class Pontos:
    def __init__(self, tela, pontos, posX, posY):
        self.tela = tela
        self.pontos = pontos
        self.posX = posX
        self.posY = posY
        self.fonte = pg.font.SysFont("monospace", 80, bold=True)
        self.label = self.fonte.render(self.pontos, 0, branco)
        
        
    def mostrar(self):
        self.tela.blit(self.label, (self.posX - self.label.get_rect().width//2, self.posY))
        
    def marcar(self):
        pontos = int(self.pontos) + 1
        self.pontos = str(pontos)
        self.label = self.fonte.render(self.pontos, 0, branco)
        
    def resetar(self):
        self.pontos = '0'
        self.label = self.fonte.render(self.pontos, 0, branco)

class Controle_Colisao:
    def entre_bola_raquete1(self, bola, raquete1):
        if bola.posY + bola.raio > raquete1.posY and bola.posY - bola.raio < raquete1.posY + raquete1.altura:
            if bola.posX - bola.raio <= raquete1.posX + raquete1.largura:
                return True
        return False
    
    def entre_bola_raquete2(self, bola, raquete2):
        if bola.posY + bola.raio > raquete2.posY and bola.posY - bola.raio < raquete2.posY + raquete2.altura:
            if bola.posX + bola.raio >= raquete2.posX:
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

    def checa_gol_jogador1(self, bola):
        return bola.posX - bola.raio >= largura
    
    def checa_gol_jogador2(self, bola):
        return bola.posX + bola.raio <= 0
    
pg.init()

# Cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (13, 95, 148)

# Configurações da tela
largura = 900
altura = 500
tamanho_tela = (largura, altura)
tela = pg.display.set_mode(tamanho_tela)
pg.display.set_caption('PONG')
relogio = pg.time.Clock()

def quadra():
    tela.fill(azul)
    pg.draw.line(tela, branco, (largura//2, 0), (largura//2, altura), 5)

def tela_inicio():
    pg.draw.rect(tela, preto, (0, 110, largura, 200))
    fonte = pg.font.Font(pg.font.get_default_font(), 30)
    texto = fonte.render('Aperte ESPAÇO para começar a partida!', True, branco)
    texto_rect = texto.get_rect()
    texto_rect.center = (largura//2, 200)
    tela.blit(texto, texto_rect)

def resetar():
    quadra()
    pontos1.resetar()
    pontos2.resetar()
    bola.reinicia_pos()
    raquete1.reinicia_pos()
    raquete2.reinicia_pos()
    tela_inicio()

def checa_vencedor(pontos):
    if pontos >= 10:
        return True
    else:
        return False

def mensagem_vitoria(pos):
    fonte_win = pg.font.SysFont("monospace", 200, bold=True)
    texto = fonte_win.render('WIN', True, branco)
    texto_rect = texto.get_rect()
    texto_rect.center = (pos, 200)
    tela.blit(texto, texto_rect)
    fonte_repetir = pg.font.SysFont('monospace', 25, bold=True)
    texto2 = fonte_repetir.render('[R] para jogar novamente', True, branco)
    texto2_rect = texto2.get_rect()
    texto2_rect.center = (pos, 300)
    tela.blit(texto2, texto2_rect)
    
quadra()

# Criando os objetos
bola = Bola(tela, branco, largura//2, altura//2, 15)
raquete1 = Raquete(tela, preto, 5, altura//2-60, 20, 120)
raquete2 = Raquete(tela, preto, largura-20-5, altura//2-60, 20, 120)
colisao = Controle_Colisao()
pontos1 = Pontos(tela, '0', largura//4, 15)
pontos2 = Pontos(tela, '0', largura-largura//4, 15)

# Variaveis
jogando = False

tela_inicio()
    
# Loop do jogo
while True:
    relogio.tick(60)
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            sys.exit()
        
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_SPACE and not jogando:
                bola.iniciar_movimento()
                jogando = True
            
            if evento.key == pg.K_r:
                resetar()
                jogando = False
                
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
        
        if colisao.checa_gol_jogador1(bola):
            quadra()
            pontos1.marcar()
            bola.reinicia_pos()
            raquete1.reinicia_pos()
            raquete2.reinicia_pos()
            
        if colisao.checa_gol_jogador2(bola):
            quadra()
            pontos2.marcar()
            bola.reinicia_pos()
            raquete1.reinicia_pos()
            raquete2.reinicia_pos()

        if checa_vencedor(int(pontos1.pontos)):
            jogando = False
            mensagem_vitoria(largura//4)
            
        if checa_vencedor(int(pontos2.pontos)):
            jogando = False
            mensagem_vitoria(largura-250)
            
            
        pontos1.mostrar()
        pontos2.mostrar()
    pg.display.update()