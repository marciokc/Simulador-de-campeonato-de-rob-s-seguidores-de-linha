class Placar:
    def __init__(self):
        self.d=30
        self.espaco = 5
        
    def desenha(self,carros):
        y=20
        x=1000
        for c in carros:
            fill(c.nav.getCor())
            stroke(0)
            strokeWeight(1)
            ellipse(x, y, self.d,self.d)
            #Sombra
            fill(0)            
            textSize(24)
            text(c.nav.getCod(),x-7,y+7)
            #Numero
            fill(255)
            textSize(22)          
            text(c.nav.getCod(),x-7,y+6)
            text(c.nav.getNome(),x+self.d/2+self.espaco,y+5)
            y+=self.d+self.espaco
    
