from flask import Flask, render_template    #Importa flask para permitirnos crear nuestra aplicación
app = Flask(__name__)                       #Crea una instancia de la clase Flask llamada "app"


@app.route('/')                              #el @ asocia esta ruta con la función que vayamos a colocarle
def hola_mundo():
    return 'Hola Mundo!'                     #Devolvemos la cadena 'Hola Mundo' como respuesta

@app.route('/hola/<nombre>')
def hola(nombre):
    return "Hola, "+nombre

@app.route('/hello/<nombre_url>/<int:cantidad>')
def hello(nombre_url, cantidad):
    return render_template('index.html', nombre=nombre_url, num=cantidad)




if __name__=="__main__":                    #Asegurarnos que este archivo que nosotros tenemos se está ejecutando directamente y no es un módulo
    app.run(debug=True)                     #Se ejecuta nuestra aplicación
