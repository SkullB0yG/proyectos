from flask import Flask, request, make_response, redirect

app= Flask(__name__)

@app.route("/")
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

@app.route("/home")
def Home():
    return "hola soy el home"

@app.route("/login")
def Login():
    return"hola soy un login"

@app.route("/show_information_adress")
def Show_information():
    user_ip = request.cookies.get("user_ip_information")
    return f"hola que tal tu ip es {user_ip}"

app.run(host='0.0.0.0', port=5500, debug=True)
