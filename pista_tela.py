
import robo

def inicializa_pista(pista,nPista): 
    
    if(nPista==0):
        
        pista.append((100,150))
        pista.append((300,150))
        pista.append((300,300))
        pista.append((450,300))
        pista.append((450,150))
        pista.append((600,50))
        pista.append((750,150))
        pista.append((750,300))
        pista.append((900,300))
        pista.append((900,450))
        pista.append((750,450))
        pista.append((750,600))
        pista.append((550,600))
        pista.append((550,450))
        pista.append((400,450))
        pista.append((400,550))
        pista.append((300,650))
        pista.append((200,550))
        pista.append((200,300))
        pista.append((100,300))
        pista.append((100,150))
        
    if(nPista==1):
        p1 = (300,150)
        pista.append((100,150))
        pista.append((300,100))
        pista.append((400,200))
        pista.append((500,200))
        pista.append((600,50))
        pista.append((750,100))
        pista.append((800,200))
        pista.append((650,250))
        pista.append((700,350))
        pista.append((900,350))
        pista.append((950,450))
        pista.append((800,600))
        pista.append((550,600))
        pista.append((550,450))
        pista.append((400,450))
        pista.append((400,550))
        pista.append((300,650))
        pista.append((200,550))
        pista.append((300,400))
        pista.append((100,300))
        pista.append((100,150))
        p2 = (200,200)
        

        
        
    if(nPista==2):    
        p1 = (100,150)
        pista.append((100,150))
        pista.append((300,150))
        pista.append((300,300))
        pista.append((450,300))
        pista.append((450,150))
        pista.append((600,50))
        pista.append((750,150))
        pista.append((750,300))
        pista.append((900,300))
        pista.append((900,450))
        pista.append((750,450))
        pista.append((750,600))
        pista.append((550,600))
        pista.append((550,450))
        pista.append((400,450))
        pista.append((400,550))
        pista.append((300,650))
        pista.append((200,550))
        pista.append((200,300))
        pista.append((100,300))
        pista.append((100,150))
        p1 = (100,150)   
            
def desenha(pista, tipo):
    background(30, 125, 30)
    # desenha a pista
    stroke(0,0,0)
    strokeWeight(5)
    
    if(tipo==0):
        for i in range(len(pista) - 1):
            line(pista[i][0], pista[i][1], pista[i+1][0], pista[i+1][1])
        noStroke()
    if(tipo==1):
        beginShape()
        curveVertex(300,150)
        for i in range(len(pista)):
            curveVertex(pista[i][0],pista[i][1])
        curveVertex(200,200)
        endShape()
    if(tipo==2):
        beginShape()
        curveVertex(100,150)
        for i in range(len(pista)):
            curveVertex(pista[i][0],pista[i][1])
        curveVertex(100,150)
        endShape()

        

        
def aneis_percurso(pista):

    aneis=[]
    
    for i in pista:
        aneis.append((i[0],i[1]))

    return aneis



def preencher_checkpoints(aneis):

    checkpoints=[]
    
    for i in range(len(aneis)):
        checkpoints.append(0)
    return checkpoints
        
        
        
