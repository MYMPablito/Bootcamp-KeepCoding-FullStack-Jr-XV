# Aplicación de Web Ingresos - Gastos

Programa hecho en python con el framework flask, App Web de Ingresos y Gastos.

# Instalación:
- Crear un entorno en python y ejecutar el comando 
```
pip install -r requirements.txt
```

La librería utilizada Flask:
```
https://flask.palletsprojects.com/en/2.3.x/
```

# Ejecución del programa:

- Inicializar el servidor de flask:
- en mac: ```export FLASK_APP=main.py```
- en windows: ```set FLASK_APP=main.py```

# Otra opción de ejecución:
- Crear un archivo .env y dentro agregar lo siguiente:

```
FLASK_APP=main.py
FLASK_DEBUG=True
```

- Luego para lanzarlo en la terminal, introducir el comando:

- ``` flask run ```

## Comando para ejecutar el servidor:
- ```flask --app main run```

## Comando para ejecutar el servidor en otro puesto diferente; por default es siempre el 5000. 
- ```flask --app main run -p 5002``` 

## Comando para ejecutar el servidor en modo debug, para realizar cambios en tiempo real.
- ```flask --app main --debug run```