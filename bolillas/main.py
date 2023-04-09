import pygame as pg

# Inicializar todos los módulos de pygame: pantallas, objetos, sonidos, teclados, etc.
pg.init()

# Crear la pantalla o sourface.
pantalla = pg.display.set_mode( (800,600) ) #definición de tamaño de pantalla.
pg.display.set_caption( "Bolillas" ) #agregar un título a mi ventana.

game_over = False

x = 0
vx = 1
y = 300
vy = 1

x2 = 0
vx2 = 1
y2 = 0
vy2 = 1

while not game_over:

    for eventos in pg.event.get(): #capturar todos los eventos mientras el bucle se ejecuta.
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True

    pantalla.fill( (12, 222, 243) ) #asignar un color a la pantalla
    
    x += vx
    y += vy    
    if x >= 800 or x == 0: #los límites de x.
        vx *= -1
    if y >= 600 or y == 0: #los límites de y.
        vy *= -1

    
    x2 += vx2
    y2 += vy2    
    if x2 >= 800 or x2 == 0: #los límites de x.
        vx2 *= -1
    if y2 >= 600 or y2 == 0: #los límites de y.
        vy2 *= -1

     

    # la pantalla o sourface, color en rgb, posiciones (posiciónAncho, posiciónLargo, tamaño del rectángulo largo, tamaño de rect ancho )
    #pg.draw.rect(pantalla, (243, 96, 12), (400,300,30,30)) #dibujar un rectángulo.
    #pg.draw.rect(pantalla, (243, 96, 12), (770,570,30,30))
    pg.draw.rect(pantalla, (243, 96, 12), (x,y,30,30))
    pg.draw.rect(pantalla, (243, 12, 138), (x2,y2,30,30))

    pg.display.flip()#función para cargar toda la configuración que va dentro de la pantalla.


pg.quit()
