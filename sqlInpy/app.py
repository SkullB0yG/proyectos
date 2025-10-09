from flask import Flask, request, make_response, redirect, render_template, url_for

app= Flask(__name__)

@app.route("/ip")
def Obt_ip():
    """
    NOS PERMITE VER LA INFORMACION VER LA 
    INFORMACION DEL CLIENTE COMO LA IP 
    DESDE DONDE SE HACE LA CONSULYA
    """
    usr_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_adress"))
    response.set_cookie("user_ip_information", usr_ip_information)
    return response

@app.route("/")
def Init():
    response = make_response(redirect("/home"))
    return response

@app.route("/home")
def Home():
    return render_template("home.html")

@app.route("/login")
def Login():
    client_ip = request.cookies.get("user_ip_information")
    return render_template("login.html", user_ip=client_ip)

@app.route("/login.html")
def Loginhtml():
    response = make_response(redirect("/login"))
    return response

@app.route("/registro")
def Registro():
    return render_template("registro.html")

@app.route("/registro.html")
def Registrohtml():
    response = make_response(redirect("/registro"))
    return response

@app.route("/procesar_registro", methods=['POST'])
def Procesar():
    nombre=request.form['nombre']
    apellido=request.form['apellido']
    email=request.form['email']
    usuario=request.form['usuario']
    password=request.form['password']
    data=[nombre, apellido, email, usuario, password]
    with open("file", "+w") as file:
        for i in data:
            file.write(f"{i}\n")
        file.close
    return "Well done"

@app.route("/show_information_adress")
def Show_information():
    user_ip = request.cookies.get("user_ip_information")
    return f"hola que tal tu ip es {user_ip}"

app.run(host='0.0.0.0', port=5500, debug=True)
