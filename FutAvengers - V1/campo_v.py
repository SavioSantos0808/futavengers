import pyxel

def campo():
    pyxel.rect(5,45,235,195,12)#cor do campo
    pyxel.rect(0,40,5,200,7)#lateral do lado esquerdo
    pyxel.rect(5,40,240,45,7)#lateral de cima
    pyxel.rect(235,45,240,200,7)#lateral do lado direito
    pyxel.rect(5,195,235,200,7)#lateral de baixo
    pyxel.rect(118,45,122,195,7)#linha do centro
    pyxel.rect(0,90,5,150,9)#gol esquerdo
    pyxel.rect(235,90,240,150,9)#gol direito
    pyxel.rect(0,0,240,40,1)#tela de placar 
    pyxel.rect(0,0,5,40,6)#tela de placar - borda esquerda
    pyxel.rect(235,0,240,40,6)#tela de placar - borda direita
    pyxel.rect(5,35,235,40,6)#tela de placar - borda esquerda
    pyxel.rect(5,0,235,5,6)#tela de placar - borda esquerda
    pyxel.text(15, 17, "FutAvengers",7)#nome do jogo
    pyxel.text(80,13,"P l a y e r  1",3)#placar - jogador 1
    pyxel.text(170,13,"P l a y e r  2",8)#placar - jogador 2
    pyxel.circb(0,120, 30, 7)#círculo do lado esquerdo
    pyxel.circb(240,120, 30, 7)#círculo do lado esquerdo