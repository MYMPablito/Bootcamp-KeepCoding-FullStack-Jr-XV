import requests

# Invocar al método get() con la url específica.
r = requests.get('https://rest.coinapi.io/v1/exchangerate/EUR/BTC?apikey=0F4E06D8-5A69-4B70-9E6D-F582AC31F688')

print("Código http de respuesta: ", r.status_code)

print("Cabecera: ", r.headers['content-type'])

print("Encoding: ", r.encoding)
'utf-8'
print("Respuesta en string: ", r.text) # String
'{"type":"User"...'
print("Respuesta en json: ", r.json()) # Diccionario

