import pygame as pg
from pygame.locals import *

pg.init()

# Criando a janela ----------------------------------------------------
largura = 700
altura = 500
tela_tamanho = (largura, altura)
tela = pg.display.set_mode(tela_tamanho)
pg.display.set_caption('Pong')
icone = pg.image.load("imagens/icon.png")
pg.display.set_icon(icone)

# Configurações jogador ------------------------------------------------
jogador_imagem = pg.image.load("imagens/raquete.png")
jogador_x = 10
jogador_y = altura/2 - 100
jogador_y_dif = 0

# Configurações bola ---------------------------------------------------
bola_imagem = pg.image.load("imagens/bola.png")
bola_x = largura / 2 - 15
bola_y = altura / 2 - 15
bola_dir_x = -3
bola_dir_y = 3

# CPU Configurações ----------------------------------------------------
cpu_imagem = pg.image.load("imagens/raquete.png")
cpu_x = largura - 10 - 27
cpu_y = altura / 2 - 100

def jogador(y):
    tela.blit(jogador_imagem, (jogador_x, y))

def bola():
    tela.blit(bola_imagem, (bola_dir_x, bola_dir_y))

def cpu():
    tela.blit(cpu_imagem, (cpu_x, cpu_y))

def calcula_cpu():
    global cpu_y, bola_y
    if cpu_y+100-bola_y-15 > 0:
        cpu_y -= 3
    elif cpu_y+100-bola_y-15 < 0:
        cpu_y += 3
    
    cpu_y = min(cpu_y, altura-10-200)
    cpu_y = max(cpu_y, 10)
    
def calcula_bola():
    global bola_dir_x, bola_dir_y, bola_x, bola_y
    

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