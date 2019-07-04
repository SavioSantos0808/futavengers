import pyxel

def campo(x):
    # desenho do campo
    pyxel.bltm(0, 0, x, 0, 0, 30, 30)
    pyxel.text(15, 17, "FutAvengers",7)#nome do jogo
    pyxel.text(80,13,"P l a y e r  1",3)#placar - jogador 1
    pyxel.text(170,13,"P l a y e r  2",8)#placar - jogador 2
    pyxel.circb(0,120, 30, 7)#círculo do lado esquerdo
    pyxel.circb(240,120, 30, 7)#círculo do lado esquerdo