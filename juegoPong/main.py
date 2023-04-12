# Aquí se ejecuta todo:
import pygame as pg
from figura_class import Pelota,Raqueta

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Pong")
#definir tasa de refresco de nuestro bucle de fotogramas, fps = fotograma por segundo.
tasa_refresco = pg.time.Clock()


pelota = Pelota(400,300)
raqueta1 = Raqueta( 15 , 300 )
raqueta2 = Raqueta( 786  , 300 )

game_over = False
while not game_over:
    #obtener la tasa de refresco en milisegundos.
    valor_tasa = tasa_refresco.tick()#variables para controlar la velocidad entre fotogramas.


    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    pantalla_principal.fill( (0,128,94) )
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), 15 ) #line (surface, color, start_pos, end_pos, width->ancho)

    pelota.dibujar(pantalla_principal)
    raqueta1.dibujar(pantalla_principal)
    raqueta2.dibujar(pantalla_principal)

    pg.display.flip()




pg.quit()