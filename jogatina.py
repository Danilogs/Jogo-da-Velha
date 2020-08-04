from jogador import Jogador
from jogovelha import Jogo
import turtle

nome  = raw_input("Nome do Primeiro Jogador: ")
marca = raw_input("Simbolo do Primeiro Jogador: ").upper()
player1 = Jogador(nome,marca)

nome  = raw_input("Nome do Segundo Jogador: ")
marca = raw_input("Simbolo do Segundo Jogador: ").upper()
player2 = Jogador(nome,marca)

print "START!\n"


jogoVelha = Jogo(player1,player2)

jogoVelha.desenhaTela()


numJogadas = 0

#sugerido

while numJogadas<9 :
    if numJogadas%2==0:
        escolha_1=player1.joga()
        if escolha_1 != False:
            valido= jogoVelha.validaJogada(escolha_1)
            if valido == True:
                jogoVelha.marcaJogada(escolha_1,1)
                numJogadas=numJogadas+1
    elif numJogadas%2!=0:
        escolha_2=player2.joga()
        if escolha_2 != False:
            valido= jogoVelha.validaJogada(escolha_2)
            if valido == True:
                jogoVelha.marcaJogada(escolha_2,2)
                numJogadas=numJogadas+1
    if numJogadas>=5:
        ganhou=jogoVelha.verificaGanhador()
        if ganhou==True:
            desejo= raw_input("Desenha continuar?[S/N]")
            if desejo=="S":
                jogoVelha.reinicia()
                numJogadas-=numJogadas
            elif desejo=="N":
                encerra()
                numJogadas+=5
            
        


