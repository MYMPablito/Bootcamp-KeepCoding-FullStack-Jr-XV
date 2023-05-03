#importar la librería de flask
from flask import Flask

#inicializar la variable app con flask
app = Flask(__name__)


#inicializar el servidor de flask
#en mac: export FLASK_APP=main.py
# en windows: set FLASK_APP=main.py

# Comando para ejecutar el servidor:
# flask --app main run

# Comando para ejecutar el servidor en otro puesto diferente; por default es siempre el 5000. 
# flask --app main run -p 5002 

# Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real.
# flask --app main --debug run

@app.route("/hola")
def hola_mundo():
    return " Hola mundo Flask, tengo hambre, comí, se me pasó "

# Ejercicio una ruta que devuelva una lista de frutas, el path sería /frutas:
@app.route("/frutas")
def lista_frutas():
    list_fruta = ["Banana","Uva","Melon","Naranja","Pomelo"]
    return list_fruta

# Ejemplo para enviar parámetros en las rutas:

@app.route("/nombre/<n>")
def tunombre(n):
    return f"hola {n} cómo estás"

# Ejercicio 2, realizar una ruta que devuelva el cuadrado de un número dado, /numero/<parámetro>

@app.route("/numero/<int:parametro>")
def cuadrado(parametro):
    #parametro = int(parametro)
    return f"El caudrado de {parametro} es {parametro * parametro}"