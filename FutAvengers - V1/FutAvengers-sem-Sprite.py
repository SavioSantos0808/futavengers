import pyxel
import random
import campo_v
from pygame import mixer

mixer.init()
mixer.music.load('8bit.mp3')
mixer.music.play()

#Telas do jogo
inicio = 0
jogando = 1
fim = 2

class Bola:
  def __init__(self,posicao_x, posicao_y,raio, cor):
    self.posicao_x = posicao_x
    self.posicao_y = posicao_y
    self.raio = raio
    self.cor = cor

class Jogador:
  def __init__(self,posicao_x1, posicao_y1,posicao_x2, posicao_y2, cor, gol):
    self.posicao_x1 = posicao_x1
    self.posicao_y1 = posicao_y1
    self.posicao_x2 = posicao_x2
    self.posicao_y2 = posicao_y2
    self.cor = cor
    self.gol = gol

class App:
  def __init__(self):
      pyxel.init(240, 240, caption="FutAvengers")
      self.bola = Bola(120,120,4,0)
      self.jogador1 = Jogador(20,110,30,130,0,0)
      self.jogador2 = Jogador(220,110,230,130,0,0)
      self.x = 1
      self.y = 1
      self.inicio = False
      self.teladojogo = inicio
      self.selecaojogadores = [45,75,45,75]
      self.avenger1 = []
      self.avenger2 = []
      self.vezdeescolher = 1
      self.animar_frame = True
      pyxel.run(self.update, self.draw)

  def update(self):
    if self.teladojogo == inicio:
      #Botões de escolha dos avengers
      if self.selecaojogadores[0] >= 60:
        if pyxel.btnp(pyxel.KEY_LEFT):
          self.selecaojogadores[0] -= 40
          self.selecaojogadores[1] -= 40

      if self.selecaojogadores[1] <= 180:
        if pyxel.btnp(pyxel.KEY_RIGHT):
          self.selecaojogadores[0] += 40
          self.selecaojogadores[1] += 40
      
      if self.selecaojogadores[2] >= 60:
        if pyxel.btnp(pyxel.KEY_UP):
          self.selecaojogadores[2] -= 30
          self.selecaojogadores[3] -= 30

      if self.selecaojogadores[3] <= 120:
        if pyxel.btnp(pyxel.KEY_DOWN):
          self.selecaojogadores[2] += 30
          self.selecaojogadores[3] += 30

      if self.vezdeescolher == 1:
        if pyxel.btnp(pyxel.KEY_1):
          self.avenger1 = list(self.selecaojogadores)
          self.vezdeescolher = 2
      
      if self.vezdeescolher == 2:
        if pyxel.btnp(pyxel.KEY_2):
          if self.selecaojogadores == self.avenger1:
            pass
          else:
            self.avenger2 = list(self.selecaojogadores)
            self.vezdeescolher = 0

      if self.vezdeescolher == 0:
        if pyxel.btnp(pyxel.KEY_ENTER):
          self.teladojogo = jogando

    if self.teladojogo == jogando:
      self.inicio = True
      #movimentos do jogador 1  
      if pyxel.btn(pyxel.KEY_A):
        if self.jogador1.posicao_x1 > 10:
          self.jogador1.posicao_x1 -= 5
          self.jogador1.posicao_x2 -= 5
      if pyxel.btn(pyxel.KEY_D):
        if self.jogador1.posicao_x2 < 230:
          self.jogador1.posicao_x1 += 5
          self.jogador1.posicao_x2 += 5
      if pyxel.btn(pyxel.KEY_W):
        if self.jogador1.posicao_y1 > 50:
          self.jogador1.posicao_y1 -= 5
          self.jogador1.posicao_y2 -= 5
      if pyxel.btn(pyxel.KEY_S):
        if self.jogador1.posicao_y2 < 190:
          self.jogador1.posicao_y1 += 5
          self.jogador1.posicao_y2 += 5
        
      #movimentos do jogador 2
      if pyxel.btn(pyxel.KEY_LEFT):
        if self.jogador2.posicao_x1 > 10:
          self.jogador2.posicao_x1 -= 5
          self.jogador2.posicao_x2 -= 5
      if pyxel.btn(pyxel.KEY_RIGHT):
        if self.jogador2.posicao_x2 < 230:
          self.jogador2.posicao_x1 += 5
          self.jogador2.posicao_x2 += 5
      if pyxel.btn(pyxel.KEY_UP):
        if self.jogador2.posicao_y1 > 50:
          self.jogador2.posicao_y1 -= 5
          self.jogador2.posicao_y2 -= 5
      if pyxel.btn(pyxel.KEY_DOWN):
        if self.jogador2.posicao_y2 < 190:
          self.jogador2.posicao_y1 += 5
          self.jogador2.posicao_y2 += 5

      #velocidade da bola
      if self.inicio == True:
        self.bola.posicao_x += self.x
        self.bola.posicao_y += self.y 

      #Colisão das quinas
      if self.bola.posicao_x - self.bola.raio <= 5:
        self.x = -self.x
      if self.bola.posicao_x + self.bola.raio >= 235:
        self.x = -self.x 
      if self.bola.posicao_y - self.bola.raio <= 45:
        self.y = -self.y
      if self.bola.posicao_y + self.bola.raio >= 195:
        self.y = -self.y

      #Colisão da bola com o jogador
      #jogador 1
      if ((self.jogador1.posicao_x2 == self.bola.posicao_x - self.bola.raio) or (self.jogador1.posicao_x1 == self.bola.posicao_x + self.bola.raio)) and (self.jogador1.posicao_y1 <= self.bola.posicao_y + self.bola.raio) and (self.jogador1.posicao_y2 >= self.bola.posicao_y - self.bola.raio):
        self.x = -self.x
      if ((self.jogador1.posicao_y2 == self.bola.posicao_y - self.bola.raio) or (self.jogador1.posicao_y1 == self.bola.posicao_y + self.bola.raio)) and (self.jogador1.posicao_x1 <= self.bola.posicao_x + self.bola.raio) and (self.jogador1.posicao_x2 >= self.bola.posicao_x - self.bola.raio):
        self.y = -self.y
      
      #jogador 2
      if ((self.jogador2.posicao_x2 == self.bola.posicao_x - self.bola.raio) or (self.jogador2.posicao_x1 == self.bola.posicao_x + self.bola.raio)) and (self.jogador2.posicao_y1 <= self.bola.posicao_y + self.bola.raio) and (self.jogador2.posicao_y2 >= self.bola.posicao_y - self.bola.raio):
        self.x = -self.x
      if ((self.jogador2.posicao_y2 == self.bola.posicao_y - self.bola.raio) or (self.jogador2.posicao_y1 == self.bola.posicao_y + self.bola.raio)) and (self.jogador2.posicao_x1 <= self.bola.posicao_x + self.bola.raio) and (self.jogador2.posicao_x2 >= self.bola.posicao_x - self.bola.raio):
        self.y = -self.y

      #Detecção de gols
      if self.bola.posicao_x - self.bola.raio <= 5 and self.bola.posicao_y >= 90 and self.bola.posicao_y <= 150:
        self.jogador2.gol += 1
        self.bola.posicao_x = 120
        self.bola.posicao_y = 120

      if self.bola.posicao_x + self.bola.raio >= 235 and self.bola.posicao_y >= 90 and self.bola.posicao_y <= 150:
        self.jogador1.gol += 1
        self.bola.posicao_x = 120
        self.bola.posicao_y = 120

      #Fim da partida
      if self.jogador1.gol + self.jogador2.gol == 5:
        self.teladojogo = fim

    if self.teladojogo == fim:
      #Jogador vencedor
      if self.jogador1.gol > self.jogador2.gol:
        self.jogador1.cor = 9
        self.bola = Bola(120,120,4,0)
      else:
        self.jogador2.cor = 9
        self.bola = Bola(120,120,4,0)

      #Reiniciar o jogo
      if pyxel.btn(pyxel.KEY_ENTER):
        self.inicio = False
        self.jogador1 = Jogador(20,110,30,130,0,0)
        self.jogador2 = Jogador(220,110,230,130,0,0)
        self.teladojogo = inicio
        self.vezdeescolher = 1
        

      #Encerrar o jogo 
      elif pyxel.btn(pyxel.KEY_BACKSPACE):
        mixer.music.stop()
        pyxel.quit()

  def draw(self):
    if self.teladojogo == inicio:
      pyxel.cls(12)   
      pyxel.rect(10,10,230,230,1)

      #Fundo com jogadores já escolhidos
      if len(self.avenger1) == 4:
        pyxel.rectb(self.avenger1[0],self.avenger1[2],self.avenger1[1],self.avenger1[3],random.randint(12,13))
      if len(self.avenger2) == 4:
        pyxel.rectb(self.avenger2[0],self.avenger2[2],self.avenger2[1],self.avenger2[3],random.randint(14,15))

      pyxel.text(25,25,"FUT",random.randint(12,14))
      pyxel.text(35,35,"AVENGERS",random.randint(12,14))

      #botao de escolha
      pyxel.rectb(self.selecaojogadores[0],self.selecaojogadores[2],self.selecaojogadores[1],self.selecaojogadores[3],13)

      #botoes a escolher
      pyxel.circ(60,60,10,8)
      pyxel.circ(100,60,10,8)
      pyxel.circ(140,60,10,8)
      pyxel.circ(180,60,10,8)
      pyxel.circ(60,90,10,8)
      pyxel.circ(100,90,10,8)
      pyxel.circ(140,90,10,8)
      pyxel.circ(180,90,10,8)
      pyxel.circ(60,120,10,8)
      pyxel.circ(100,120,10,8)
      pyxel.circ(140,120,10,8)
      pyxel.circ(180,120,10,8)

      if self.vezdeescolher == 1:
        pyxel.text(40,180,"JOGADOR 1, ESCOLHA SEU AVENGER E APERTE 1.",random.randint(9,10))
      if self.vezdeescolher == 2:
        pyxel.text(40,180,"JOGADOR 2, ESCOLHA SEU AVENGER E APERTE 2.",random.randint(9,10))
      if self.vezdeescolher == 0:
        pyxel.text(55,180,"DIGITE ENTER PARA INICIAR O JOGO",random.randint(9,10))
    
    if self.teladojogo == jogando:
      #arquivo que desenha o campo
      campo_v.campo()

      #avengers escolhidos
      #avenger 1
      if self.avenger1 == [45,75,45,75]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [85,115,45,75]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [125,155,45,75]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [165,195,45,75]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [45,75,75,105]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [85,115,75,105]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [125,155,75,105]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [165,195,75,105]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [45,75,105,135]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [85,115,105,135]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [125,155,105,135]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)
      if self.avenger1 == [165,195,105,135]:
        pyxel.rect(self.jogador1.posicao_x1,self.jogador1.posicao_y1,self.jogador1.posicao_x2,self.jogador1.posicao_y2,self.jogador1.cor)

      #avenger 2
      if self.avenger2 == [45,75,45,75]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador1.cor)
      if self.avenger2 == [85,115,45,75]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [125,155,45,75]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [165,195,45,75]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [45,75,75,105]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [85,115,75,105]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [125,155,75,105]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [165,195,75,105]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [45,75,105,135]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [85,115,105,135]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [125,155,105,135]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)
      if self.avenger2 == [165,195,105,135]:
        pyxel.rect(self.jogador2.posicao_x1,self.jogador2.posicao_y1,self.jogador2.posicao_x2,self.jogador2.posicao_y2,self.jogador2.cor)

      #placares do jogador 1 e jogador 2
      pyxel.text(100,25,str(self.jogador1.gol), 3)
      pyxel.text(190,25,str(self.jogador2.gol), 8)

      #Bola do jogo
      pyxel.circ(self.bola.posicao_x, self.bola.posicao_y, self.bola.raio, self.bola.cor)

      #Torcida
      pyxel.rect(0,200,240,240,12)

    if self.teladojogo == fim:
      pyxel.rect(0,0,240,240,1)
      pyxel.text(90,20,"F I M  D E  J O G O", 8)
      pyxel.circb(120,80,20,8)
      pyxel.text(107,80,str(self.jogador1.gol) + "  X  " + str(self.jogador2.gol), 8)
      pyxel.text(40,160,"APERTE  A TECLA BACKSPACE  \n\nPARA  FINALIZAR O JOGO", 12)
      pyxel.text(40,200,"APERTE  A TECLA ENTER  \n\nPARA  INICIAR OUTRO JOGO", 11)

App()
