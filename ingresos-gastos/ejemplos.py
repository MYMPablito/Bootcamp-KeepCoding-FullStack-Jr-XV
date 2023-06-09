# Lectura de archivos:
'''
with open('data/movimientos.csv','r') as resultado:
    leer = resultado.read()  #muestra todo, guarda como str
    print(leer)
'''
# Otro ejemplo
'''
resultado = open('data/movimientos.csv','r')
lectura = resultado.readline() #Lee sólo una línea.
print(lectura)

resultado = open('data/movimientos.csv','r')
lectura = resultado.readlines() #lee todas las líneas, guarda como lista.
print(lectura)
'''

'''
import csv

mi_dato = []
mi_fichero = open('data/movimientos.csv','r')
lectura = csv.reader(mi_fichero, delimiter=",",quotechar='"')

for item in lectura:
    print(item)
    mi_dato.append(item)

print("Mi lista: ", mi_dato[0][0]) #puedo darle posiciones mi_dato[0,1,2,etc...]
'''

# Ejemplo de registro de datos en csv:
'''
import csv
mifichero = open('data/movimientos.csv','a',newline='')
lectura = csv.writer(mifichero,delimiter=',',quotechar='"')
lectura.writerow(['08/12/2023','Nuevo y mejor empleo','15000000'])

mifichero.close()
'''

#Para obtener la fecha actual:

from datetime import date
print("fecha de hoy: ", date.today())


