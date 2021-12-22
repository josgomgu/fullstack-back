"""
    App.py Principal
"""
from flask import Flask, request, redirect
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
