import InterfaceNavegador as n

class Navegador(n.InterfaceNavegador):
    def __init__(self, n=0):
        self.cod=n #codigo que sera exibido proximo ao robo
        self.sensores = [] #lista com os sensores (cada sensor possui o valor 1 caso identifique uma linha, 0 caso contrario)       
        self.me=1 #velocidade do motor esquerdo. Deve variar entre 0 e 1
        self.md=0 #velocidade do motor esquerdo. Deve variar entre 0 e 1       
        
        #Alterar a partir daqui
        self.cor = color(255,255,0,200) #defina a cor RGB do robo aqui 
        self.nome = "Robo do mal"
        
    #Logica do navegador que e executada a cada iteracao do programa.
    #A partir da leitura dos sensores (lista sensores), definir a velocidade dos motores (variaveis me e md)
    def navegar(self):
        if self.sensores[0]==1:
            self.me=0
            self.md=0.6
        elif self.sensores[-1]==1:
            self.me=0.6
            self.md=0
        else:
            self.me=1
            self.md=1
     
