from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Crear tabla si no existe
def init_db():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL,
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    usuario = request.form['usuario']
    password = request.form['password']

    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, password) VALUES (?, ?)", (usuario, password))
    conn.commit()
    conn.close()

    return f"Usuario {usuario} guardado correctamente"

if __name__ == '__main__':
    app.run(debug=True)
