"""
    App.py Principal
"""
from flask import Flask, request, redirect, Response
from persistencia import guardar_pedido

app = Flask(__name__)

@app.route("/pizza",methods=['POST'])
def pizza():
    """
    Metodo Pizza para registrar pedido
    """
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    print("El solicitante del pedido es: "+nombre + " " + apellido)

    with open("archivos/pedidos.txt", "w", encoding="utf-8") as file:
        file.write("")
        file.close()

    guardar_pedido(nombre,apellido)

    return redirect("http://localhost/U1AF/solicita_pedido.html", code=302)

@app.route("/checksize",methods=['POST'])
def checksize():
    """
    Comprueba disponibilidad de un tamaño de pizza.
    """
    size = request.form.get("tamano")
    if(size=="S"):
        mensaje = "No Disponible"
    else:
        mensaje = "Disponible" 

    return Response(mensaje, 200, {'Access-Control-Allow-Origin': '*'})
