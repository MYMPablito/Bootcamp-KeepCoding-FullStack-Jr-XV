import pygame as pg
from figura_class import Raqueta,Pelota
from utils import *

ANCHO = 800
ALTO = 600

class Partida:
    pg.init()
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode( (ANCHO,ALTO) )
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()

        self.pelota = Pelota(ANCHO//2,ALTO//2)
        self.raqueta1 = Raqueta( 15 , ALTO//2 )
        self.raqueta2 = Raqueta( ANCHO - 14  , ALTO//2 )

    def bucle_fotograma(self):
        game_over = False
        while not game_over:
            self.tasa_refresco.tick(500)

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True

            self.raqueta1.mover(pg.K_w, pg.K_s) #raqueta izquierda.
            self.raqueta2.mover(pg.K_UP, pg.K_DOWN) #raqueta derecha.
            self.pelota.mover()
     
            self.pantalla_principal.fill( (0,128,94) )
            pg.draw.line(self.pantalla_principal, BLANCO, (400,0), (400,600), 15 )

            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)

    #Lógica de choque:
            self.pelota.comprobar_choque(raqueta1=self.raqueta1, raqueta2=self.raqueta2)

            self.pelota.mostrar_marcador(self.pantalla_principal)
    



            pg.display.flip()
        
        pg.quit()