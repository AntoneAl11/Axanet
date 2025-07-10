import os
import json

clientes = {}

def cargar_clientes():
    if os.path.exists("clientes.json"):
        with open("clientes.json", "r") as f:
            return json.load(f)
    return {}

def guardar_clientes():
    with open("clientes.json", "w") as f:
        json.dump(clientes, f, indent=4)

def crear_cliente(nombre, descripcion):
    if nombre in clientes:
        print("Cliente ya existe.")
    else:
        clientes[nombre] = [descripcion]
        guardar_clientes()
        print(f"Cliente {nombre} creado.")

def actualizar_cliente(nombre, descripcion):
    if nombre in clientes:
        clientes[nombre].append(descripcion)
        guardar_clientes()
        print(f"Cliente {nombre} actualizado.")
    else:
        print("Cliente no encontrado.")

def consultar_cliente(nombre):
    if nombre in clientes:
        print(f"{nombre}: {clientes[nombre]}")
    else:
        print("Cliente no encontrado.")

def eliminar_cliente(nombre):
    if nombre in clientes:
        del clientes[nombre]
        guardar_clientes()
        print(f"Cliente {nombre} eliminado.")
    else:
        print("Cliente no encontrado.")

clientes = cargar_clientes()
