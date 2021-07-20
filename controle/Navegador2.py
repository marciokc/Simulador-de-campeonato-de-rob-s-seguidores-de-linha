import InterfaceNavegador as n

class Navegador(n.InterfaceNavegador):
    def __init__(self, n=0):
        self.cod=n
        self.sensores = []
        self.me=1
        self.md=0
        self.cor = color(100,100,255,200) #defina a cor RGB do robo aqui 
        self.nome = "Robo legal" #defina o nome do robo. Usar no maximo 15 caracteres
        
    def navegar(self):
        if self.sensores[0]==1:
            self.me=0
            self.md=0.8
        elif self.sensores[-1]==1:
            self.me=0.8
            self.md=0
        else:
            self.me=0.9
            self.md=0.9
     
