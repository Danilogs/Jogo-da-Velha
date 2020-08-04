class Jogador:

    def __init__(self, nome, caracter):

        self.nome    = nome
        self.simbolo = caracter

    def getNome(self):
        return self.nome

    def getMarca(self):
        return self.simbolo

    def joga(self):
        pos = ""
        desiste = False
        valores = ('1','2','3','4','5','6','7','8','9') #corrigido

        while pos not in valores and not desiste:
            pos = raw_input(self.nome+", escolha a posicao: ") #melhoria: mostra o nome do jogador
            if pos not in valores:
                print "\nValor invalido!!\n"
                escolha = raw_input("Digite S para tentar de novo ou qq outra tecla para desistir: ").upper()
                if escolha <> "S":
                    desiste = True

        if desiste:
            return False
        else:
            return int(pos) #corrigido
