from flask import Flask, render_template, request, jsonify, redirect
import formulario
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

mensajes = [
    {'usuario': 'Persona123', 'asunto': 'Hola',
        'mensaje': 'Hola, un saludo especial'},
    {'usuario': 'Usuario987', 'asunto': 'Chao',
        'mensaje': 'Chao, nos vemos luego'},
    {'usuario': 'Prueba', 'asunto': 'Chaolin',
        'mensaje': 'Chao, nos vemos luego!!'}
]


@app.route('/')
def main():
    formulario1 = formulario.formularioWTF()
    return render_template('index.html', formulario1=formulario1)


@app.route('/iniciar', methods=['POST'])
def iniciar():
    if request.form["nombre"] == "Prueba" and request.form["contraseña"] == "Prueba123":
        print("¡¡¡¡¡¡OK!!!!")
        return redirect('/salida')
    else:
        formulario1 = formulario.formularioWTF()
        return render_template('index.html', formulario1=formulario1)


@app.route('/usuario/<string:nombreUsuario>')
def usuario(nombreUsuario):
    encontrado = ""
    for usuario in mensajes:
        if nombreUsuario == usuario["usuario"]:
            encontrado = usuario
            break
    return jsonify(encontrado)


@app.route('/salida')
def salida():
    return jsonify(mensajes)
