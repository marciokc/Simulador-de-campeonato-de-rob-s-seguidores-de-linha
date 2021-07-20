#-*- coding:latin1 -*-
import pista_tela
errouPercurso=0
id=0
completou=0


centroCarroX = 0
centroCarroY = 0

#Variáveis PID
kP = 0.456
kI = 0.1
kD = 0


class robo(object):
    """
    Guarda as propriedades, regras e estados do robo    
    """
    def __init__(self, x, y, sensores, col, nav , v=5, theta = (PI*2)):
        self.x = x
        self.y = y
        self.v = v
        self.theta = theta
        self.dt = 0.5
        self.sensores = sensores
        self.comprimento = 38
        self.largura = 20
        self.estado = 5
        self.vmax = 5
        self.dtheta = PI/72.0
        #self.if1_atual, self.if2_atual, self.if3_atual = [0, 0], [0, 0], [0, 0]
        self.sensores_atuais = []
        self.sensor_rgb = []
        self.leitura = []
        self.nSensores = col
        self.s1, self.s2, self.s3 = 0, 0, 0
        self.carroP1, self.carroP2, self.carroP3 = [0, 0], [0, 0], [0, 0]
        self.dimensao = 70
        self.pidMode = 1
        self.ultimoValor = (self.nSensores-1)*100/2
        self.velBase = 0.5
        self.setPoint = (self.nSensores - 1)*100/2
        self.kP, self.kI, self.kD = 0, 0, 0        
        self.sobreLinha = 0
        self.iniSensores()
        self.nav=nav
        
        

    def iniSensores(self):
        for i in range(self.nSensores):
            self.sensores_atuais = self.sensores_atuais + [[0,0]]
            self.leitura = self.leitura + [0]

             
    def AtualizaLeitura(self):
        
        p1 = int(4*len(self.sensor_rgb)/10)
        
        self.s1, self.s2, self.s3 = 0, 0, 0
            
            
        for i in range(len(self.leitura)):
            self.leitura[i] = 0
        
        if (self.pidMode == 0):
            
            for i in range(p1):
                if self.sensor_rgb[i]==(0,0,0):
                    self.s1=1
                    self.leitura[i]=1
                    #print(self.leitura[i])
                #print(self.leitura[i])
            
            for i in range(p1, len(self.sensor_rgb) - p1):
                if self.sensor_rgb[i]==(0,0,0):
                    self.s2=1
                    self.leitura[i]=1
                    #print(self.leitura[i])
            
            for i in range(len(self.sensor_rgb) - p1, len(self.sensor_rgb)):
                if self.sensor_rgb[i]==(0,0,0):
                    self.s3=1
                    self.leitura[i]=1

        else :
            for i in range (self.nSensores):
                if self.sensor_rgb[i] == (0,0,0):
                    self.leitura[i] = 1
            #print(self.leitura)
                

    #Função que retorna um valor de acordo com a posição do robô em relação a linha.
    
    
    def desenha(self):
        #fill(0, 0, 255)
        noFill()
        stroke(5,5,5)
        strokeWeight(1)
        self.sensor_rgb = self.le_sensorIF()
        self.atualizaPontoCarro()
        self.atualizaPosSensores()
        fill(self.nav.getCor());
        triangle(self.carroP1[0], self.carroP1[1],
                 self.carroP2[0], self.carroP2[1],
                 self.carroP3[0], self.carroP3[1])
        self.AtualizaLeitura()        
        textSize(18);
        fill(255);
        text(self.nav.getCod(),(self.carroP1[0]+self.carroP2[0]+self.carroP3[0])/3.0,(self.carroP1[1]+self.carroP2[1]+self.carroP3[1])/3.0-20);
         
        for i in range(self.nSensores):
            if self.leitura[i]==1:
                fill(255, 0, 0)
            else:
                fill(255, 255, 0)
            ellipse(self.sensores_atuais[i][0], self.sensores_atuais[i][1], 3, 3)
        noStroke()
     



    def anda(self):
        vx = self.v*cos(self.theta)
        vy = self.v*sin(self.theta)
        self.x = self.x + vx*self.dt
        self.y = self.y + vy*self.dt
        return self.x, self.y
    
    def move(self,velE,velD):
        
        self.theta = self.theta + self.dtheta*(velE-velD)
        vx = self.v*cos(self.theta)*(velE+velD)/2
        vy = self.v*sin(self.theta)*(velE+velD)/2
        self.x = self.x + vx*self.dt
        self.y = self.y + vy*self.dt
        return self.x, self.y
    
    def navega(self):
        self.sensor_rgb = self.le_sensorIF()
        self.AtualizaLeitura()
        self.nav.leitura(self.leitura)
        self.nav.navegar()
        self.move(self.nav.getM1(),self.nav.getM2())
        pass
        
    
    
    def atualizaPontoCarro(self):
        self.carroP1[0] = self.largura*cos(float(self.theta) + PI/2.0) + self.x
        self.carroP1[1] = self.largura*sin(float(self.theta) + PI/2.0) + self.y
        self.carroP2[0] = self.largura*cos(float(self.theta - PI/2.0)) + self.x
        self.carroP2[1] = self.largura*sin(float(self.theta - PI/2.0)) + self.y
        self.carroP3[0] = self.comprimento*cos(self.theta) + self.x
        self.carroP3[1] = self.comprimento*sin(self.theta) + self.y
        
        return self.x,self.y
    

    def atualizaPosSensores(self):
         for i in range(self.nSensores):
            for j in range(2):
                if (j==0):
                    self.sensores_atuais[i][j] = self.sensores[i][0]*cos(self.theta) - self.sensores[i][1]*sin(self.theta) + self.x
                elif (j==1):
                    self.sensores_atuais[i][j] = self.sensores[i][0]*sin(self.theta) + self.sensores[i][1]*cos(self.theta) + self.y

    def le_sensorIF(self):
        self.atualizaPosSensores() 
        cor_if = []
        for i in range(self.nSensores):
            cor_if = cor_if + [[0,0]]            
            cor_if[i] = get(int(self.sensores_atuais[i][0]), int(self.sensores_atuais[i][1]))
            if(self.sensores_atuais[i][0]<0 or self.sensores_atuais[i][0]>=width or self.sensores_atuais[i][1]<0 or self.sensores_atuais[i][1]>=height):
                cor_if[i] = get(0,0)            
        rgb = []
        
        for i in range(self.nSensores):
            rgb = rgb + [[0,0,0]]
            rgb[i] = (red(cor_if[i]), green(cor_if[i]), blue(cor_if[i]))            
        
        return rgb
        
               
#retorna true se esta proximo da pista e false cc               
def proximoPista(carro,pista):
    global centroCarroX, centroCarroY
    centroCarroX = (carro.carroP1[0] + carro.carroP2[0] + carro.carroP3[0]) / 3 
    centroCarroY = (carro.carroP1[1] + carro.carroP2[1] + carro.carroP3[1]) / 3 
    for i in range (int(centroCarroX-carro.dimensao/2),int( centroCarroX+carro.dimensao/2)):
        for j in range(int(centroCarroY-carro.dimensao/2), int(centroCarroY+carro.dimensao/2)):
            if((((i - centroCarroX)**2) + ((j - centroCarroY)**2)) <= (carro.dimensao/2)**2):
                #stroke(0,0,0)
                #ellipse(i,j, 3, 3)
                corgeral = get(int(i),int(j))
                #print(green(corgeral))
                if ((red(corgeral),green(corgeral),blue(corgeral))==(0,0,0)):
                    
                    return True
            
    return False
        

        
def atualizar_checkpoints(aneis,carro,checkpoints,nextCheck_completou):
    

    global errouPercurso,completou,id,missCheckpoint, centroCarroX, centroCarroY
    centroCarroX = (carro.carroP1[0] + carro.carroP2[0] + carro.carroP3[0]) / 3 
    centroCarroY = (carro.carroP1[1] + carro.carroP2[1] + carro.carroP3[1]) / 3 
    
    missCheckpoint = 0;
    errouPercurso = 0
    completou = 0
    id = nextCheck_completou[0]
    
    for i in range(len(aneis)):
        if((((aneis[i][0] - centroCarroX)**2) + ((aneis[i][1] - centroCarroY)**2)) <= ((carro.dimensao/2)+10)**2 and checkpoints[i] == 0):    
            checkpoints[i]=1                 
            completou=1
            
            for k in range(len(checkpoints)):
                if (checkpoints[k] == 0):
                    missCheckpoint = missCheckpoint +1;
            if(missCheckpoint>2):
                completou = 0
                                
            if(completou==1):
                id = 0
                for i in range(len(checkpoints)):
                    checkpoints[i] = 0
                nextCheck_completou = [id, completou, errouPercurso]
                return nextCheck_completou
            
            id = i
            nextCheck_completou = [id, completou, errouPercurso]
            return nextCheck_completou
    

        else:        
            if((((aneis[i][0] - centroCarroX)**2) + ((aneis[i][1] - centroCarroY)**2)) <= (carro.dimensao/2)**2 and checkpoints[i] == 1 and i!=id and (i>1 or checkpoints[i+1]==1)):
                errouPercurso = 1
                nextCheck_completou = [id, completou, errouPercurso]
                return nextCheck_completou

    nextCheck_completou = [id, completou, errouPercurso]
    return nextCheck_completou
    
