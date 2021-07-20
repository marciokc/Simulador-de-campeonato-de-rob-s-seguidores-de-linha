#Software desenvolvido por:
#Marcio Kassouf Crocomo
#Gustavo Voltani Atzingen
#Matheus Luis Oliveira Silva
#Thomas Taino

import robo, pista_tela, Teste, Navegador1, Navegador2, Navegador3, Navegador4, Placar

desenhar=1
nPista=1
nSensores=3
pista = []
p = Placar.Placar()

def setup():
    global nPista, pista, carros, carro1, carro2
    size(1200, 700)
    global  carro
    pista_tela.inicializa_pista(pista,nPista)
       
    #Adiciona todos os competidores
    carros=[]
    carros.append(robo.robo(100, 120, [[40,-15],[40,0],[40,15]],nSensores, Navegador1.Navegador1('A')))
    carros.append(robo.robo(100, 120, [[40,-15],[40,0],[40,15]],nSensores, Navegador2.Navegador2('B')))
    carros.append(robo.robo(100, 120, [[40,-30],[40,-15],[40,0],[40,15],[40,30]],5, Navegador3.Navegador3('C')))
    carros.append(robo.robo(100,120,[[40,-15],[40,0],[40,15]],nSensores, Navegador4.Navegador4('D')))
    
    
def draw():
    global  carro1, carro2, pista, nPista, desenhar,checkpoints, contador, desenhar, nSensores, p
    noFill()
        
    pista_tela.desenha(pista, nPista)
        
    for c in carros:
        c.navega()

    for c in carros:
        c.desenha()

    p.desenha(carros)
     
    
    
        
            
