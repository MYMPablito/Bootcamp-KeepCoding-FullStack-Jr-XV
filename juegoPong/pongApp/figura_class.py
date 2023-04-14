import pygame as pg
from .utils import *


class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=120,color= BLANCO,vx=1,vy=1 ):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla, self.color, (self.pos_x - (self.w//2) ,self.pos_y - (self.h//2),self.w,self.h))
    
    def mover(self,tecla_arriba,tecla_abajo,y_max=Y_MAX,y_min=Y_MIN):
        estado_teclado = pg.key.get_pressed()

        if estado_teclado[tecla_arriba] == True and self.pos_y >= y_min + (self.h//2):
            self.pos_y -= 1
        elif estado_teclado[tecla_abajo] == True and self.pos_y < y_max - (self.h//2):
            self.pos_y += 1

    @property
    def derecha(self):
        return self.pos_x + (self.w//2)
    @property
    def izquierda(self):
        return self.pos_x - (self.w//2)
    @property
    def arriba(self):
        return self.pos_y - (self.h//2)
    @property
    def abajo(self):
        return self.pos_y + (self.h//2)

class Pelota:
    def __init__(self,pos_x,pos_y,color=BLANCO,radio=20,vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.contadorDerecho = 0
        self.contadorIzquierdo = 0

    def dibujar(self,pantalla):
        pg.draw.circle( pantalla,self.color,(self.pos_x ,self.pos_y), self.radio )

    def mover(self,x_max=X_MAX,y_max=Y_MAX, y_min=Y_MIN, x_min=X_MIN):
        self.pos_x += self.vx
        self.pos_y += self.vy
        if (self.pos_y >= y_max - self.radio) or (self.pos_y < y_min + self.radio): #Rebote en eje y.
            self.vy *= -1
        
        if self.pos_x >= x_max + self.radio*5: #límite derecho x.
            self.contadorIzquierdo += 1
            self.pos_x = x_max //2
            self.pos_y = y_max //2
            self.vx *= -1
            self.vy *= -1
            

        if self.pos_x < x_min - self.radio*5: #límite izquierdo x.
            self.contadorDerecho += 1
            self.pos_x = x_max //2
            self.pos_y = y_max //2
            self.vx *= -1
            self.vy *= -1
             

    def mostrar_marcador(self,pantalla):
        fuente = pg.font.Font(None, 50)
        jugador1 = fuente.render(str(self.contadorIzquierdo),0,BLANCO)
        jugador2 = fuente.render(str(self.contadorDerecho),0,BLANCO)
        textoj1 = fuente.render("Jugador 1",0,BLANCO)
        textoj2 = fuente.render("Jugador 2",0,BLANCO)
        pantalla.blit(textoj1,(135,15))
        pantalla.blit(textoj2,(540,15))
        pantalla.blit(jugador1,(200,70))
        pantalla.blit(jugador2,(600,70))
    @property
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio
    
    def comprobar_choque(self,raqueta1,raqueta2):
        #Lógica de choque:
        if self.derecha >= raqueta2.izquierda and\
            self.izquierda <= raqueta2.derecha and\
            self.abajo >= raqueta2.arriba and\
            self.arriba <= raqueta2.abajo:
            self.vx *= -1
    
        if self.derecha >= raqueta1.izquierda and\
            self.izquierda <= raqueta1.derecha and\
            self.abajo >= raqueta1.arriba and\
            self.arriba <= raqueta1.abajo:
            self.vx *= -1

    def comprobar_choqueV2(self,*raquetas):
        for r in raquetas:
            if self.derecha >= r.izquierda and\
                self.izquierda <= r.derecha and\
                self.abajo >= r.arriba and\
                self.arriba <= r.abajo:
                self.vx *= -1 

         
