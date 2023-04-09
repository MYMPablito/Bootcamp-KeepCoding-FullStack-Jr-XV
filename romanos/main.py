from romanos_class import NumeroRomano
from romanos_exception import RomanNumberError

continuar = True
seguir=""
operacion=""
valor=""
while continuar:

    operacion = input("Que desea realizar \n Romano_a_entero: presione 'r' \n Entero_a_romano: presione: 'e' ")

    if operacion=="r":
        try:
            valor = input("por favor ingrese el valor en romano: ") 
            obj1 = NumeroRomano(valor)
            print(f"El valor de {obj1.representacion_romano} es igual a  {obj1.valor}")
        except Exception as e:
            print(e)
            

    elif operacion == "e":
        try:
            valor = int(input("por favor ingrese el valor en numero entero: ")) 
            obj2 = NumeroRomano(valor)
            print(f"El valor de {obj2.valor} es igual a {obj2.representacion_romano}")
        except Exception as e:
            print(e)

    seguir=input("Si desea salir del programa presione 'n' :")
    if seguir == "n":
        continuar = False
        print("Fin del programa")
