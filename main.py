import os
from src.classes.Persona import Persona
from src.DataStructs.ArbolB.ArbolB import ArbolB

from src.classes.Cliente import Cliente
from src.DataStructs.ListaCircularDoble.CircularDoble import CircularDoble

from src.DataStructs.Grafo.ListaAdyacencia import ListaAdyacencia
from src.classes.Vertice import Vertice

import tkinter as tk
from tkinter import Menu
from tkinter import filedialog

global circular_doble
circular_doble = CircularDoble()


def on_option_selected(option):
    print(f"Seleccionaste la opción: {option}")

def create_menu(root):
    menu_bar = Menu(root)

    # Menú de Clientes
    clientes_menu = Menu(menu_bar, tearoff=0)
    clientes_menu.add_command(label="Agregar", command=lambda: on_option_selected("Clientes -> Agregar"))
    clientes_menu.add_command(label="Carga Masiva", command=lambda: cargar_archivo(circular_doble))
    clientes_menu.add_command(label="Modificar", command=lambda: on_option_selected("Clientes -> Modificar"))
    clientes_menu.add_command(label="Eliminar", command=lambda: on_option_selected("Clientes -> Eliminar"))
    clientes_menu.add_command(label="Mostrar Información", command=lambda: on_option_selected("Clientes -> Mostrar Información"))
    clientes_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: generar_Grafico_CircularDoble())
    menu_bar.add_cascade(label="Clientes", menu=clientes_menu)

    # Menú de Vehículos
    vehiculos_menu = Menu(menu_bar, tearoff=0)
    vehiculos_menu.add_command(label="Agregar", command=lambda: on_option_selected("Vehículos -> Agregar"))
    vehiculos_menu.add_command(label="Modificar", command=lambda: on_option_selected("Vehículos -> Modificar"))
    vehiculos_menu.add_command(label="Eliminar", command=lambda: on_option_selected("Vehículos -> Eliminar"))
    vehiculos_menu.add_command(label="Mostrar Información", command=lambda: on_option_selected("Vehículos -> Mostrar Información"))
    vehiculos_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: on_option_selected("Vehículos -> Mostrar Estructura de Datos"))
    menu_bar.add_cascade(label="Vehículos", menu=vehiculos_menu)

    # Menú de Viajes
    viajes_menu = Menu(menu_bar, tearoff=0)
    viajes_menu.add_command(label="Agregar", command=lambda: on_option_selected("Viajes -> Agregar"))
    viajes_menu.add_command(label="Modificar", command=lambda: on_option_selected("Viajes -> Modificar"))
    viajes_menu.add_command(label="Eliminar", command=lambda: on_option_selected("Viajes -> Eliminar"))
    viajes_menu.add_command(label="Mostrar Información", command=lambda: on_option_selected("Viajes -> Mostrar Información"))
    viajes_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: on_option_selected("Viajes -> Mostrar Estructura de Datos"))
    menu_bar.add_cascade(label="Viajes", menu=viajes_menu)

    # Menú de Rutas
    rutas_menu = Menu(menu_bar, tearoff=0)
    rutas_menu.add_command(label="Agregar", command=lambda: on_option_selected("Rutas -> Agregar"))
    rutas_menu.add_command(label="Modificar", command=lambda: on_option_selected("Rutas -> Modificar"))
    rutas_menu.add_command(label="Eliminar", command=lambda: on_option_selected("Rutas -> Eliminar"))
    rutas_menu.add_command(label="Mostrar Información", command=lambda: on_option_selected("Rutas -> Mostrar Información"))
    rutas_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: on_option_selected("Rutas -> Mostrar Estructura de Datos"))
    menu_bar.add_cascade(label="Rutas", menu=rutas_menu)

    root.config(menu=menu_bar)



def cargar_archivo(circular_doble:CircularDoble):
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if not archivo:
        print("No se seleccionó ningún archivo.")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if linea.endswith(";"):
                    linea = linea[:-1]  # Eliminar el punto y coma final
                    datos = linea.split(", ")
                    if len(datos) == 6:
                        cliente = Cliente(dpi=datos[0], nombres=datos[1], apellidos=datos[2], genero=datos[3], telefono=int(datos[4]), direccion=datos[5])
                        circular_doble.agregar(cliente)
        print("Carga masiva completada.")
        circular_doble.ordenar_por_dpi()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


def generar_Grafico_CircularDoble():
    dot:str = circular_doble.generar_imagen()

    # Guardar el texto en un archivo .dot
    with open("Reportes/Clientes.dot", "w") as file:
        file.write(dot)

    # Generar la imagen usando Graphviz
    os.system("dot -Tpng Reportes/Clientes.dot -o Reportes/Clientes.png")

    # Abrir la imagen generada con el programa predeterminado en Windows
    os.startfile("C:/Users/tubac/Downloads/Vacaciones Diciembre 2024/EDD Vacaciones Diciembre 2024/Laboratorio/Proyecto_2/Reportes/Clientes.png")
    
    


def main() -> None:

    root = tk.Tk()
    root.title("Interfaz de Gestión")
    root.geometry("900x600")

    create_menu(root)

    root.mainloop()




    '''
    #Esta parte corresponde al arbol B:
    nuevaPersona = Persona("Miguel", 25)
    #print(f"Nombre:  {nuevaPersona.get_nombre()}")
    #print(f"Edad: {nuevaPersona.get_edad()}")
    print(nuevaPersona)# Aca no me imprimira la direccion de memoria sino que el metodo __str__ de la clase persona

    nuevoArbol: ArbolB = ArbolB(5)#Este es el valor de orden
    nuevoArbol.insertar_valor(5)
    nuevoArbol.insertar_valor(6)
    nuevoArbol.insertar_valor(4)
    nuevoArbol.insertar_valor(2)
    nuevoArbol.insertar_valor(7)
    nuevoArbol.insertar_valor(9)
    nuevoArbol.insertar_valor(10)
    nuevoArbol.insertar_valor(3)
    nuevoArbol.insertar_valor(1)
    nuevoArbol.insertar_valor(12)
    nuevoArbol.insertar_valor(0)

    nuevoArbol.insertar_valor(-1)
    nuevoArbol.insertar_valor(13)
    nuevoArbol.insertar_valor(20)
    nuevoArbol.insertar_valor(23)

    print(nuevoArbol.imprimir_usuario())

    #os.system("dot -Tpng Reportes/arbol_b.dot -o Reportes/arbol_b.png")'''






    '''
    #Esta parte corresponde a la parte de los grafos
    lista_adyacencia:ListaAdyacencia = ListaAdyacencia()

    lista_adyacencia.insertar(Vertice(1), Vertice(2))
    lista_adyacencia.insertar(Vertice(1), Vertice(3))
    lista_adyacencia.insertar(Vertice(1), Vertice(4))
    lista_adyacencia.insertar(Vertice(2), Vertice(1))
    lista_adyacencia.insertar(Vertice(3), Vertice(2))
    lista_adyacencia.insertar(Vertice(4), Vertice(2))'''

if __name__ == '__main__':
    main()
