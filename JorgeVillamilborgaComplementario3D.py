import numpy as np
import matplotlib.pyplot as plt
#Importamos las funciones de la clase tools 3d creada en clase previamente
import tools3d as Tools
from math import ceil


import sys
#necesario instalar pynput con pip install pynput
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        if(key == 'esc'):
            print("se presiono esc")
            sys.exit()
with Listener(
on_press=on_press) as listener:
    listener.join()
 

   



#   Arreglos de las coordenadas
xg=[]
yg=[]
zg=[]

#   Puntos del centro
xc = 80    
yc = 40    
zc = 40

def LineaPlano(xg,yg,zg):
    plt.axis([80,250,120,20])
    plt.axis()
    plt.grid()


    #Ploteamos el plano
    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='b')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='b')
    plt.plot([xg[2],xg[0]],[yg[2],yg[0]],color='b')


    #Dibujamos el punto numero 3
    plt.scatter(xg[3],yg[3],s=20,color='r')


    #Ploteamos la interseccion de los triangulos
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],color='r',linestyle='--')
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],color='r',linestyle='--')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],color='r',linestyle='--')

    plt.show()

#Metodo para el Hitpointx

def hitPoint(x,y,z):
    
    #Distancia del punto(0,1)
    a=x[1]-x[0]
    b=y[1]-y[0]
    c=z[1]-z[0]
    Q01=np.sqrt(a*a+b*b+c*c)
    """
   Componentes del punto(4,5)
    lx = a/Q45
    ly = b/Q45
    lz = c/Q45
    """

    #Distancia del punto(1,2)
    a=x[2]-x[1]
    b=y[2]-y[1]
    c=z[2]-z[1]
    Q12=np.sqrt(a*a+b*b+c*c)
    """
    Componentes del punto(0,3)
    ux = a/Q03
    uy = b/Q03
    uz = c/Q03
    """

    #Distancia del punto(0,2)
    a=x[2]-x[0]
    b=y[2]-y[0]
    c=z[2]-z[0]
    Q02=np.sqrt(a*a+b*b+c*c)
    
    #Tercer punto del triangulo
    #Distancia del punto(1,3)
    a=x[3]-x[1]
    b=y[3]-y[1]
    c=z[3]-z[1]
    Q13=np.sqrt(a*a+b*b+c*c)


    #Distancia del punto(2,3)
    a=x[2]-x[3]
    b=y[2]-y[3]
    c=z[2]-z[3]
    Q23=np.sqrt(a*a+b*b+c*c)


    #Distancia del punto(0,3)
    a=x[0]-x[3]
    b=y[0]-y[3]
    c=z[0]-z[3]
    Q03=np.sqrt(a*a+b*b+c*c)

    
    #Area A
    s=(Q01+Q12+Q02)/2
    A=np.sqrt(s*(s-Q01)*(s-Q12)*(s-Q02))
    #Area A1
    s1=(Q01+Q03+Q13)/2
    A1=np.sqrt(s1*(s1-Q01)*(s1-Q03)*(s1-Q13))
    #Area A2
    s2=(Q02+Q23+Q03)/2
    A2=np.sqrt(s2*(s2-Q02)*(s2-Q23)*(s2-Q03))


    return A,A1,A2
    
#Metodo para dibujar la linea del triangulo
def plotTriangleLine(xc,yc,zc):
    

    [A,A1,A2]=hitPoint(x,y,z)

    
    #Text A,A1,A2,A1+A2,In,Out
    if((A1+A2)>A):
        plt.text(180,80,'Fuera')
        plt.text(180,85,'Fuera del limite')
    elif((A1+A2)<A):
        plt.text(180,80,'Dentro')
        plt.text(180,85,'Dentro del limite')
    A=ceil(A)
    A1=ceil(A1)
    A2=ceil(A2)
    A3=ceil(A1+A2)
    plt.text(180,60,'A=',color='k')
    plt.text(190,60,A,color='k')
    plt.text(180,65,'A1=',color='r')
    plt.text(190,65,A1,color='r')
    plt.text(180,70,'A2=',color='r')
    plt.text(190,70,A2,color='r')
    if((A1+A2)>A):
        plt.text(180,75,'A1+A2=',color=(.5,.2,.8))
        plt.text(200,75,A3,color=(.5,.2,.8))
    elif((A1+A2)<A):
        plt.text(180,75,'A1+A2=',color='g')
        plt.text(200,75,A3,color='g')

    LineaPlano(xg,yg,zg)

#plotSquareLinex(xc,yc,zc)
#Plot figure

#   Coordenadas locales
x=[40,30,80,0]
y=[60,10,60,0]
z=[0,0,0,0]



while True:
      
    Hitpointx=input("Coordenada x del Hitpointx:  (Pulse ESC para salir)")
   
    x[3]=int(Hitpointx)

    
    Hitpointy=input("Coordenada y del Hitpointy: (Pulse ESC para salir)") 
    y[3]=int(Hitpointy)

    for i in range(len(x)):
        xg.append( x[i]+xc )
        yg.append( y[i]+yc )
        zg.append( z[i]+zc )

    plotTriangleLine(xc,yc,zc)
  