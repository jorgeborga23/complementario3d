"""

Este programa contiene las funciones de rotacion en los ejes X,Y and Z

junto a sus respectivas matrices de rotacion definidas en las clases anteriores

"""

import numpy as np

from math import cos,sin,radians #0 usar lo que ya trae numpy



#_____________Definir las funciones

def rotRx(xc,yc,zc,xp,yp,zp,Rx):

    a=[xp,yp,zp]

    b=[1,0,0]

    xpp=np.inner(a,b)# Producto escalar de a,b=xp*Rx12+zp*Rx13

    b=[0,cos(Rx),-sin(Rx)]#--------Rx21,Rx22,Rx23

    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rx21+yp*Rx22+zp*Rx23

    b=[0,sin(Rx),cos(Rx)]#------Rx31,Rx32,Rx33

    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rx31+yp*Rx32+zp*Rx33

    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]

    return [xg,yg,zg]



def rotRy(xc,yc,zc,xp,yp,zp,Ry):

    a=[xp,yp,zp]

    b=[cos(Ry),0,sin(Ry)]

    xpp=np.inner(a,b)# Producto escalar de a,b=xp*Rx12+zp*Rx13

    b=[0,1,0]#--------Ry21,Ry22,Ry23

    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Ry21+yp*Ry22+zp*Ry23

    b=[-sin(Ry),0,cos(Ry),]#------Ry31,Ry32,Ry33

    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Ry31+yp*Ry32+zp*Ry33

    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]

    return [xg,yg,zg]

    

def rotRz(xc,yc,zc,xp,yp,zp,Rz): 

    a=[xp,yp,zp]

    b=[cos(Rz),-sin(Rz),0]

    xpp=np.inner(a,b)# Producto escalar de a,b=xp*Rz12+zp*Rz13

    b=[sin(Rz),cos(Rz),0]#--------Rz21,Rz22,Rz23

    ypp=np.inner(a,b)#Producto escalar de a,b=xp*Rz21+yp*Rz22+zp*Rz23

    b=[0,0,1]#------Rz31,Rz32,Rz33

    zpp=np.inner(a,b)#Producto escalar de a,b=xp*Rz31+yp*Rz32+zp*Rz33

    [xg,yg,zg]=[xpp+xc,ypp+yc,zpp+zc]

    return [xg,yg,zg]



def fillStartCircleValues(phi1,phi2,dphi,x,y,z,r,xg,yg,zg):

    for phi in np.arange(phi1,phi2+dphi,dphi):

        xp = r*cos(phi)

        yp = r*sin(phi)

        zp = 0

        x.append(xp)

        y.append(yp)

        z.append(zp)

        xg.append(xp)

        yg.append(yp)

        zg.append(zp)

    return [x,y,z,xg,yg,zg]