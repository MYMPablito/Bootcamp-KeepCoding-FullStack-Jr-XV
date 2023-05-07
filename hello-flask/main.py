#importar la librería de flask
from flask import Flask, render_template

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
    list_fruta = ["Banana","Uva","Melón","Naranja","Pomelo"]
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

#Ejercicio 3, realizar una ruta, que dinámicamente pueda solicitar o realizar
#operaciones de suma,resta, multiplicación y división según los parámetros pasados en la ruta.

@app.route("/operaciones/<float:n1>/<float:n2>/<string:ope>")
def calculadora(n1,n2,ope):
    if ope == "suma":
        return f"La suma de {n1} y {n2} es: {n1+n2}"
    elif ope == "resta":
        return f"La resta de {n1} y {n2} es: {n1-n2}"
    elif ope == "multiplicación":
        return f"El producto de {n1} y {n2} es: {n1*n2}"
    elif ope == "división":
        return f"La división de {n1} y {n2} es: {n1/n2}"
    
@app.route("/<nombre>") #esta sería la ruta principal "/", va directo a http://127.0.0.1:5000/ (localhost:5000)
def llamarhtml(nombre):
    list_fruta = ["Platano","Fresa","Piña","Melon","Naranja"]
    return render_template("hola.html",name=nombre,fruts=list_fruta)
