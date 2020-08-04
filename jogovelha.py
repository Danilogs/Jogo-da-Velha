import turtle
from time import sleep

class Jogo:

    jogadas     = []
    posMarca    = {1:(-90,90),2:(0,90),3:(90,90),4:(-90,0),5:(0,0),6:(90,0),7:(-90,-90),8:(0,-90),9:(90,-90)}
    
    def __init__(self,p1,p2):
        self.jogador1 = p1
        self.jogador2 = p2
        self.tela   = turtle.Screen()
        self.caneta = turtle.Turtle()
        self.tela.bgcolor("yellow")               
                               
    def desenhaTela(self):
             
        self.caneta.color("blue")               # caneta fica azul
        self.caneta.pensize(3)                  # define a espessura da caneta
        self.caneta.hideturtle()                # esconde a tartaruga
        self.caneta.speed(10)                   # define a velocidade de desenho
        
        #linha 1 horizontal
        self.caneta.penup()
        self.caneta.backward(135)
        self.caneta.left(90)
        self.caneta.forward(45)
        self.caneta.right(90)
        self.caneta.pendown()
        self.caneta.forward(270)
        #linha 2 horizontal
        self.caneta.penup()
        self.caneta.right(90)
        self.caneta.forward(90)
        self.caneta.right(90)
        self.caneta.pendown()
        self.caneta.forward(270)
        #linha 1 vertical
        self.caneta.penup()
        self.caneta.right(90)
        self.caneta.forward(180)
        self.caneta.right(90)
        self.caneta.forward(90)
        self.caneta.right(90)
        self.caneta.pendown()
        self.caneta.forward(270)
        #linha 2 vertical
        self.caneta.penup()
        self.caneta.left(90)
        self.caneta.forward(90)
        self.caneta.left(90)
        self.caneta.pendown()
        self.caneta.forward(270)
        self.tela.listen()    

    def validaJogada(self,pos):
        if (len(self.jogadas)>0 and pos in self.jogadas[0]) or (len(self.jogadas)>1 and pos in self.jogadas[1]):   
            #corrigido. undo nao serve para texto
            aviso = turtle.Turtle()
            aviso.hideturtle()
            aviso.penup()
            aviso.goto(0,160)
            aviso.pendown()
            aviso.color("red")
            aviso.write('JOGADA INVALIDA!!!!',align="center",font=('Arial', 28, 'bold'))
            sleep(1.5)
            aviso.clear()
            self.tela.listen()
            return False
        else:
            return True

    def marcaJogada(self,pos,numJogador):

        self.caneta.penup()
        self.caneta.goto(self.posMarca[pos][0],self.posMarca[pos][1]) #corrigido
        self.caneta.pendown()

        if numJogador == 1:
            marca = self.jogador1.getMarca()
            if len(self.jogadas)==0:
                self.jogadas.append([pos])
            else:
                self.jogadas[0].append(pos)
                self.jogadas[0].sort()
        else:
            marca = self.jogador2.getMarca()
            if len(self.jogadas)==1:
                self.jogadas.append([pos])
            else:
                self.jogadas[1].append(pos)
                self.jogadas[1].sort()

        self.caneta.write(marca,align="center",font=('Arial', 20, 'bold'))
        self.tela.listen()

    def verificaGanhador(self):
        if len(self.jogadas)== 2:
            posGanha = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
            ganhador = ""
            print self.jogadas[0],self.jogadas[1]

            #corrigido:
            
            if len(self.jogadas[0])>=3:
                for lista in posGanha:
                    cont = 0
                    for p in lista:
                        if p in self.jogadas[0]:
                            cont +=1
                    if cont==3 :
                        ganhador = self.jogador1.getNome().upper()
                        break

            if ganhador == "" and len(self.jogadas[1])>=3:
                for lista in posGanha:
                    cont = 0
                    for p in lista:
                        if p in self.jogadas[1]:
                            cont +=1
                    if cont==3 :
                        ganhador = self.jogador2.getNome().upper()
                        break

            if ganhador <> "":
                self.caneta.penup()
                self.caneta.goto(0,160)
                self.caneta.pendown()
                self.caneta.color("red")
                self.caneta.write(ganhador+' VENCEU!!!!',align="center",font=('Arial', 28, 'bold'))
                self.tela.listen()
                return True
            else:
                return False
        else:
            return False
                                                                
        
    def reinicia(self):
        self.caneta.clear()
        self.caneta.penup()#corrigido
        self.caneta.goto(0,0)
        self.desenhaTela()
        self.jogadas = [] #corrigido
        self.tela.listen()

    def encerra():
        #self.tela.exitonclick()
        return "oi"
    
