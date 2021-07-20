import InterfaceNavegador as n

class Navegador(n.InterfaceNavegador):
    def __init__(self, n=0):
        self.cod=n #codigo que sera exibido proximo ao robo
        self.sensores = [] #lista com os sensores (cada sensor possui o valor 1 caso identifique uma linha, 0 caso contrario)       
        self.me=1 #velocidade do motor esquerdo. Deve variar entre 0 e 1
        self.md=0 #velocidade do motor esquerdo. Deve variar entre 0 e 1       
        
        #Alterar a partir daqui
        self.cor = color(255,0,0,200) #defina a cor RGB do robo aqui 
        self.nome = "Ferrai"
        self.inicia_curva = 0
        self.max_curva = 2
        self.v_min = 0
        
    #Logica do navegador que e executada a cada iteracao do programa.
    #A partir da leitura dos sensores (lista sensores), definir a velocidade dos motores (variaveis me e md)
    def navegar(self):
        if self.sensores[0]==1:
            self.inicia_curva = self.max_curva
        elif self.sensores[-1]==1:
            self.inicia_curva = -self.max_curva
        elif self.sensores[1]==1:
            self.inicia_curva = 0
            
        if self.inicia_curva > 0:
            self.me = self.v_min + (1-self.v_min)*(self.max_curva - self.inicia_curva)/self.max_curva
            self.md = 1
            self.inicia_curva -= 1
        elif self.inicia_curva < 0:
            self.me = 1
            self.md =  self.v_min + (1-self.v_min)*(self.max_curva + self.inicia_curva)/self.max_curva
            self.inicia_curva += 1
        else:
            self.me = 1
            self.md = 1
     
    # def navegar(self):
    #     if self.sensores[0]==1:
    #         self.inicia_curva = self.max_curva
    #         self.me = 0
    #         self.md = 1
    #     elif self.sensores[-1]==1:
    #         self.inicia_curva = -self.max_curva
    #         self.me = 1
    #         self.md = 0
    #     elif self.sensores[1]==1:
    #         self.inicia_curva = 0
    #     elif self.inicia_curva != 0:
    #         if self.inicia_curva > 0:
    #             self.me = (self.max_curva - self.inicia_curva)/self.max_curva
    #             self.md = 1
    #             self.inicia_curva -= 1
    #         else:
    #             self.me = 1
    #             self.md =  (self.max_curva + self.inicia_curva)/self.max_curva
    #             self.inicia_curva += 1
    #     else:
    #         self.me = 1
    #         self.md = 1