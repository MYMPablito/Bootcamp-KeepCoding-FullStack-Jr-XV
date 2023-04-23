import requests
from .utils import *

# Ejercicio 3, creo un input para cargar la moneda digital:

moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()

while moneda_cripto != "" and moneda_cripto.isalpha() == True:

    # Invocar al método get() con la url específica.
    r = requests.get(f'https://rest.coinapi.io/v1/exchangerate/{moneda_cripto}/EUR?apikey={APIKEY}')

    respuesta = r.json()#la respuesta http en formato diccionario

    if r.status_code == 200:
        # Ejercicio 1, como capturamos el rate
        print("{:,.2f}€".format( respuesta['rate']) )
        break
    else:
        # Ejercicio 2, cómo capturo el error:
        print(respuesta['error'])
    
    moneda_cripto = input("Ingrese una criptomoneda conocida: ").upper()










'''
print("Código http de respuesta: ", r.status_code)
print("Cabecera: ", r.headers['content-type'])
print("Encoding: ", r.encoding)
'utf-8'
print("Respuesta en string: ", r.text) # String
'{"type":"User"...'
print("Respuesta en json: ", r.json()) # Diccionario
'''



