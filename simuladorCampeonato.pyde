#Software desenvolvido por:
#Marcio Kassouf Crocomo
#Gustavo Voltani Atzingen
#Matheus Luis Oliveira Silva
#Thomas Taino

import os
from importlib import import_module
import robo, pista_tela, Placar

desenhar=1
nPista=1
nSensores=3
pista = []
p = Placar.Placar()

def setup():
    global nPista, pista, carro, carros, carro1, carro2

    size(1200, 700)
    pista_tela.inicializa_pista(pista, nPista)
       
    #Adiciona todos os competidores
    modules = [module for module in os.listdir(sketchPath()+'/controle')\
                if '.py' in module and not '__init__' in module]
    carros=[]
    for i, module in enumerate(modules):
        m = import_module('controle.'+ module.strip('.py'))
        carros.append(robo.robo(100, 120, 
                      [[40,-15],[40,0],[40,15]],
                      nSensores, m.Navegador(chr(i+65))))
    
    
def draw():
    global  carro1, carro2, pista, nPista, desenhar,checkpoints, contador, desenhar, nSensores, p
    noFill()
        
    pista_tela.desenha(pista, nPista)
        
    for c in carros:
        c.navega()

    for c in carros:
        c.desenha()

    p.desenha(carros)
     
    
    
        
            
