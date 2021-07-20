class InterfaceNavegador:
    
    def leitura(self, s):
        self.sensores=s
        pass
    
    def navegar(self):
        
        pass
        
    def getM1(self):
        if self.me>1:
            return 1
        elif self.me<0:
            return 0
        else:
            return self.me        

    def getM2(self):
        if self.md>1:
            return 1
        elif self.md<0:
            return 0
        else:
            return self.md
        
        
    def getCor(self):
        return self.cor
    
    def getCod(self):
        return self.cod
    
    def getNome(self):
        return self.nome
