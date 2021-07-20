import InterfaceNavegador as n

class Navegador4(n.InterfaceNavegador):
    def __init__(self, n=0):
        self.cod=n #codigo que sera exibido proximo ao robo
        self.sensores = [] #lista com os sensores (cada sensor possui o valor 1 caso identifique uma linha, 0 caso contrario)       
        self.me=1 #velocidade do motor esquerdo. Deve variar entre 0 e 1
        self.md=0 #velocidade do motor esquerdo. Deve variar entre 0 e 1       
        
        #Alterar a partir daqui
        self.cor = color(0,0,0,200) #defina a cor RGB do robo aqui 
        self.nome = "FSM do Marcio"
        self.estado=1
        
    #Logica do navegador que e executada a cada iteracao do programa.
    #A partir da leitura dos sensores (lista sensores), definir a velocidade dos motores (variaveis me e md)
    def navegar(self):
        
        #troca estados
        if self.estado==1:
            if self.sensores[0]==1:
                self.estado=2
            elif self.sensores[2]==1:
                self.estado=3
        else:
            if self.sensores[1]==1:
                self.estado=1
       
                      
        if self.estado==1:
            self.me=1
            self.md=1
        elif self.estado==2:
            self.me=0.2;
            self.md=1
        else:
            self.me=1
            self.md=0.2
                                          
                
     
