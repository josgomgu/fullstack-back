#Estudiante     : 	José Andrés Gómez
#Módulo         :	1
#Actividad Final :  Flask

def guardar_pedido(nombres, apellidos):
    """
    Metodo Para Guardar Pedido
    """
    with open("archivos/pedidos.txt", "a", encoding="utf-8") as file:
        file.write("Pedido Almacenado para: " + nombres + " " + apellidos + "\n")
        file.close()
