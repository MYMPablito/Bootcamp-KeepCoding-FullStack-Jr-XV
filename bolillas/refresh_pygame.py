import pygame as pg

pg.init()

#definir pantalla
pantalla= pg.display.set_mode( (800,600) )#tamaño de ventana
pg.display.set_caption(" Bolillas ")#titulo de la ventana

game_over=False
cont=0

x=0
y=0
vx=1
vy=1

x2=20
y2=20
vx2=1
vy2=1
while not game_over:
    cont += 1
    print(cont)
    for eventos in pg.event.get():#capturar los eventos
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over=True
    #para que se mueva el objeto
    x +=vx
    y +=vy
    #para que rebote los objetos segun limite
    if x >= 800 or x<=0: #limite en x
        vx *= -1
    if y >= 600 or y<=0:#limite en y
        vy *= -1

     #para que se mueva el objeto
    x2 +=vx2
    y2 +=vy2
    #para que rebote los objetos segun limite
    if x2 >= 800 or x2<=0: #limite en x
        vx2 *= -1
    if y2 >= 600 or y2<=0:#limite en y
        vy2 *= -1            

    pantalla.fill( (12, 222, 243) )#pintar pantalla  
    pg.draw.rect(pantalla,(245, 242, 244), (x,y,20,20))#rectangulo
    pg.draw.rect(pantalla,( 241, 21, 141 ), (x2,y2,20,20))#rectangulo

    pg.display.flip()#ejecuta todas las caracteristicas definidas

pg.quit()