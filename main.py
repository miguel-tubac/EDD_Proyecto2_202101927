import os
from src.classes.Persona import Persona
from src.DataStructs.ArbolB.ArbolB import ArbolB

from src.classes.Cliente import Cliente
from src.classes.Vehiculo import Vehiculo
from src.DataStructs.ListaCircularDoble.CircularDoble import CircularDoble

from src.DataStructs.Grafo.ListaAdyacencia import ListaAdyacencia
from src.classes.Vertice import Vertice
from src.classes.Ruta import Ruta

import tkinter as tk
from tkinter import Tk, Label, Menu
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

from PIL import Image, ImageTk

global circular_doble
circular_doble = CircularDoble()

global arbolb_general
arbolb_general: ArbolB = ArbolB(5)#Este es el valor de orden

global lista_adyacencia_general
lista_adyacencia_general:ListaAdyacencia = ListaAdyacencia()


#--------------------------------------------------------------Esta es el menu principal----------------------------------------------------------------
def on_option_selected(option):
    print(f"Seleccionaste la opción: {option}")

def create_menu(root):
    menu_bar = Menu(root)

    # Menú de Clientes
    clientes_menu = Menu(menu_bar, tearoff=0)
    clientes_menu.add_command(label="Agregar", command=lambda: cargar_cliente())
    clientes_menu.add_command(label="Carga Masiva", command=lambda: cargar_archivo(circular_doble))
    clientes_menu.add_command(label="Modificar", command=lambda: modificar_cliente())
    clientes_menu.add_command(label="Eliminar", command=lambda: eliminar_cliente())
    clientes_menu.add_command(label="Mostrar Información", command=lambda: mostrar_informacion_cliente())
    clientes_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: generar_Grafico_CircularDoble())
    menu_bar.add_cascade(label="Clientes", menu=clientes_menu)

    # Menú de Vehículos
    vehiculos_menu = Menu(menu_bar, tearoff=0)
    vehiculos_menu.add_command(label="Agregar", command=lambda: cargar_vehiculo())
    vehiculos_menu.add_command(label="Carga Masiva", command=lambda: cargar_archivo_vehiculos())
    vehiculos_menu.add_command(label="Modificar", command=lambda: modificar_vehiculo())
    vehiculos_menu.add_command(label="Eliminar", command=lambda: eliminar_vehiculo())
    vehiculos_menu.add_command(label="Mostrar Información", command=lambda: mostrar_informacion_vehiculo())
    vehiculos_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: generar_Grafico_Arbolb())
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
    rutas_menu.add_command(label="Carga Masiva", command=lambda: cargar_archivo_rutas())
    rutas_menu.add_command(label="Modificar", command=lambda: on_option_selected("Rutas -> Modificar"))
    rutas_menu.add_command(label="Eliminar", command=lambda: on_option_selected("Rutas -> Eliminar"))
    rutas_menu.add_command(label="Mostrar Información", command=lambda: on_option_selected("Rutas -> Mostrar Información"))
    rutas_menu.add_command(label="Mostrar Estructura de Datos", command=lambda: generar_Grafico_ListaAdyacencia(root=root))
    menu_bar.add_cascade(label="Rutas", menu=rutas_menu)

    root.config(menu=menu_bar)
#--------------------------------------------------------Fin Menu Principal-----------------------------------------------------------------------------------



#--------------------------------------------------------------Esta es la parte de los CLientes---------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_archivo(circular_doble:CircularDoble):
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if not archivo:
        print("No se seleccionó ningún archivo.")
        messagebox.showinfo("Información", "No se seleccionó ningún archivo")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if linea.endswith(";"):
                    linea = linea[:-1]  # Eliminar el punto y coma final
                    datos = linea.split(",")
                    if len(datos) == 6:
                        cliente = Cliente(dpi=datos[0], nombres=datos[1], apellidos=datos[2], genero=datos[3], telefono=int(datos[4]), direccion=datos[5])
                        circular_doble.agregar(cliente)
        print("Carga masiva completada.")
        messagebox.showinfo("Información", "Carga masiva completada")
        circular_doble.ordenar_por_dpi()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


def generar_Grafico_CircularDoble():
    dot:str = circular_doble.generar_imagen()

    # Guardar el texto en un archivo .dot
    with open("Reportes/Clientes.dot", "w") as file:
        file.write(dot)

    # Generar la imagen usando Graphviz
    os.system("dot -Tpng -Gdpi=300 Reportes/Clientes.dot -o Reportes/Clientes.png")

    # Abrir la imagen generada con el programa predeterminado en Windows
    os.startfile("C:/Users/tubac/Downloads/Vacaciones Diciembre 2024/EDD Vacaciones Diciembre 2024/Laboratorio/Proyecto_2/Reportes/Clientes.png")
    

def cargar_cliente():
    # Crear ventana emergente
    ventana = tk.Toplevel()
    ventana.title("Ingreso de Cliente")
    ventana.geometry("250x250") #largo x ancho

    # Variables para almacenar los datos
    dpi_var = tk.StringVar()
    nombres_var = tk.StringVar()
    apellidos_var = tk.StringVar()
    genero_var = tk.StringVar()
    telefono_var = tk.StringVar()
    direccion_var = tk.StringVar()

    # Etiquetas y entradas para cada campo
    tk.Label(ventana, text="DPI:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=dpi_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Nombres:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=nombres_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Apellidos:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=apellidos_var).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Género:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=genero_var).grid(row=3, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Teléfono:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=telefono_var).grid(row=4, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Dirección:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=direccion_var).grid(row=5, column=1, padx=10, pady=5)

    def guardar_datos(): 
        cliente = Cliente(dpi=dpi_var.get(), nombres=nombres_var.get(), apellidos=apellidos_var.get(), genero=genero_var.get(), telefono=int(telefono_var.get()), direccion=direccion_var.get())
        circular_doble.agregar(cliente)
        print("¡¡¡ Cliente ingresado Correctamente !!!") 
        circular_doble.ordenar_por_dpi() # Se ordena despues de ingresar a un nuevo cliente
        ventana.destroy()
        messagebox.showinfo("Información", "¡¡¡ Cliente ingresado Correctamente !!!")

    # Botón para guardar datos
    tk.Button(ventana, text="Guardar", command=guardar_datos).grid(row=6, column=0, columnspan=2, pady=10)

    # Hacer modal la ventana
    ventana.transient()  # Hacer que sea hija de la ventana principal
    ventana.grab_set()  # Bloquear interacción con la ventana principal hasta que esta se cierre
    ventana.mainloop()


def modificar_cliente():
    # Mostrar el cuadro de diálogo para ingresar DPI
    dpi = simpledialog.askstring("Ingreso de DPI", "Ingrese el DPI del cliente:")
    if dpi:
        cliente = circular_doble.buscar(dpi=dpi)
        
        if cliente:
            # Crear ventana emergente
            ventana = tk.Toplevel()
            ventana.title("Modificar Cliente")
            ventana.geometry("250x250")

            # Variables para almacenar los datos
            dpi_var = tk.StringVar()
            nombres_var = tk.StringVar()
            apellidos_var = tk.StringVar()
            genero_var = tk.StringVar()
            telefono_var = tk.StringVar()
            direccion_var = tk.StringVar()

            # Asignar valores a las variables
            dpi_var.set(cliente.get_dpi())
            nombres_var.set(cliente.get_nombres())
            apellidos_var.set(cliente.get_apellidos())
            genero_var.set(cliente.get_genero())
            telefono_var.set(str(cliente.get_telefono()))
            direccion_var.set(cliente.get_direccion())

            # Etiquetas y entradas para cada campo
            tk.Label(ventana, text="DPI:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=dpi_var, state="readonly").grid(row=0, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Nombres:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=nombres_var).grid(row=1, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Apellidos:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=apellidos_var).grid(row=2, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Género:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=genero_var).grid(row=3, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Teléfono:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=telefono_var).grid(row=4, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Dirección:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=direccion_var).grid(row=5, column=1, padx=10, pady=5)

            # Botón para guardar cambios
            def guardar_cambios():
                cliente.set_nombres(nombres_var.get())
                cliente.set_apellidos(apellidos_var.get())
                cliente.set_genero(genero_var.get())
                cliente.set_telefono(int(telefono_var.get()))
                cliente.set_direccion(direccion_var.get())
                ventana.destroy()
                messagebox.showinfo("Éxito", "Cliente actualizado correctamente.")

            tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=6, columnspan=2, pady=10)

        else:
            messagebox.showerror("Error", f"No se encontró un cliente con DPI: {dpi}")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")



def eliminar_cliente():
    dpi = simpledialog.askstring("Ingreso de DPI", "Ingrese el DPI del cliente:")
    if dpi:
        validacion:bool = circular_doble.eliminar(dpi=dpi)
        if validacion:
            messagebox.showinfo("Información", f"Se elimino al cliente con el DPI: {dpi}")
        else:
            messagebox.showinfo("Error", f"El DPI: {dpi} no existe o la Lista esta vacia.")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")


def mostrar_informacion_cliente():
    # Mostrar el cuadro de diálogo para ingresar DPI
    dpi = simpledialog.askstring("Ingreso de DPI", "Ingrese el DPI del cliente:")
    if dpi:
        cliente = circular_doble.buscar(dpi=dpi)
        if cliente:
            mostrar:str = f"DPI: {cliente.get_dpi()}\n{cliente.get_nombres()} {cliente.get_apellidos()}\nGenero: {cliente.get_genero()}"
            mostrar += f"\nTelefono: {str(cliente.get_telefono())}\nDireccion: {cliente.get_direccion()}"
            messagebox.showinfo("Información", mostrar)

        else:
            messagebox.showerror("Error", f"No se encontró un cliente con DPI: {dpi}")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")


#--------------------------------------------------------------Fin de los Clientes----------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------------Esta es la parte de los Vehiculos---------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_archivo_vehiculos():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if not archivo:
        print("No se seleccionó ningún archivo.")
        messagebox.showinfo("Información", "No se seleccionó ningún archivo")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if linea.endswith(";"):
                    linea = linea[:-1]  # Eliminar el punto y coma final
                    datos = linea.split(":")
                    if len(datos) == 4:
                        vehiculo = Vehiculo(placa=datos[0], marca=datos[1], modelo=int(datos[2]), precio=float(datos[3]))
                        arbolb_general.insertar_valor(vehiculo)
        print("Carga masiva completada.")
        messagebox.showinfo("Información", "Carga masiva completada")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")



def generar_Grafico_Arbolb():
    dot:str = arbolb_general.imprimir_usuario()

    # Guardar el texto en un archivo .dot
    with open("Reportes/Vehiculos.dot", "w") as file:
        file.write(dot)

    # Generar la imagen usando Graphviz
    os.system("dot -Tpng -Gdpi=300 Reportes/Vehiculos.dot -o Reportes/Vehiculos.png")

    # Abrir la imagen generada con el programa predeterminado en Windows
    os.startfile("C:/Users/tubac/Downloads/Vacaciones Diciembre 2024/EDD Vacaciones Diciembre 2024/Laboratorio/Proyecto_2/Reportes/Vehiculos.png")




def cargar_vehiculo():
    # Crear ventana emergente
    ventana = tk.Toplevel()
    ventana.title("Ingreso de Vehículo")
    ventana.geometry("300x200") #largo x ancho

    # Variables para almacenar los datos
    placa_var = tk.StringVar()
    marca_var = tk.StringVar()
    modelo_var = tk.StringVar()
    precio_var = tk.StringVar()

    # Etiquetas y entradas para cada campo
    tk.Label(ventana, text="Placa:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=placa_var).grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Marca:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=marca_var).grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=modelo_var).grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Precio (Q):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    tk.Entry(ventana, textvariable=precio_var).grid(row=3, column=1, padx=10, pady=5)


    def guardar_datos(): 
        vehiculo = Vehiculo(placa=placa_var.get(), marca=marca_var.get(),modelo=int(modelo_var.get()),precio=float(precio_var.get()))
        arbolb_general.insertar_valor(vehiculo)
        print("¡¡¡ Vehículo ingresado Correctamente !!!") 
        ventana.destroy()
        messagebox.showinfo("Información", "¡¡¡ Vehículo ingresado Correctamente !!!")

    # Botón para guardar datos
    tk.Button(ventana, text="Guardar", command=guardar_datos).grid(row=6, column=0, columnspan=2, pady=10)

    # Hacer modal la ventana
    ventana.transient()  # Hacer que sea hija de la ventana principal
    ventana.grab_set()  # Bloquear interacción con la ventana principal hasta que esta se cierre
    ventana.mainloop()




def modificar_vehiculo():
    # Mostrar el cuadro de diálogo para ingresar DPI
    placa = simpledialog.askstring("Ingreso la Placa", "Ingrese la Placa del Vehículo:")
    if placa:
        vhiculo:Vehiculo = arbolb_general.buscar(placa=placa)

        if vhiculo:
            # Crear ventana emergente
            ventana = tk.Toplevel()
            ventana.title("Modificar Vehículo")
            ventana.geometry("300x200")

            # Variables para almacenar los datos
            placa_var = tk.StringVar()
            marca_var = tk.StringVar()
            modelo_var = tk.StringVar()
            precio_var = tk.StringVar()

            # Asignar valores a las variables
            placa_var.set(vhiculo.get_placa())
            marca_var.set(vhiculo.get_marca())
            modelo_var.set(str(vhiculo.get_modelo()))
            precio_var.set(str(vhiculo.get_precio()))
            

            # Etiquetas y entradas para cada campo
            tk.Label(ventana, text="Placa:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=placa_var, state="readonly").grid(row=0, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Marca:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=marca_var).grid(row=1, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Modelo:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=modelo_var).grid(row=2, column=1, padx=10, pady=5)

            tk.Label(ventana, text="Precio:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
            tk.Entry(ventana, textvariable=precio_var).grid(row=3, column=1, padx=10, pady=5)

            # Botón para guardar cambios
            def guardar_cambios():
                vhiculo.set_placa(placa_var.get())
                vhiculo.set_marca(marca_var.get())
                vhiculo.set_modelo(int(modelo_var.get()))
                vhiculo.set_precio(float(precio_var.get()))
                ventana.destroy()
                messagebox.showinfo("Éxito", "Vehículo actualizado correctamente.")

            tk.Button(ventana, text="Guardar Cambios", command=guardar_cambios).grid(row=6, columnspan=2, pady=10)

        else:
            messagebox.showerror("Error", f"No se encontró un Vehículo con Placa: {placa}")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")



def eliminar_vehiculo():
    placa = simpledialog.askstring("Ingreso la Placa", "Ingrese la Placa del Vehículo:")
    if placa:
        validacion:bool = arbolb_general.eliminar(placa=placa)
        if validacion:
            messagebox.showinfo("Información", f"Se elimino al Vehículo con la Placa: {placa}")
        else:
            messagebox.showinfo("Error", f"La placa: {placa} no existe o el Arbol esta vacio.")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")



def mostrar_informacion_vehiculo():
    placa = simpledialog.askstring("Ingreso la Placa", "Ingrese la Placa del Vehículo:")
    if placa:
        vehiculo:Vehiculo = arbolb_general.buscar(placa=placa)
        if vehiculo:
            mostrar:str = f"Placa: {vehiculo.get_placa()}\nMarca: {vehiculo.get_marca()}\nModelo: {str(vehiculo.get_modelo())}"
            mostrar += f"\nPrecio (Q.): {str(vehiculo.get_precio())}"
            messagebox.showinfo("Información", mostrar)
        else:
            messagebox.showinfo("Error", f"La placa: {placa} no existe o el Arbol esta vacio.")
    else:
        messagebox.showinfo("Información", "No se ingresó ningún valor válido.")


#----------------------------------------------------------------------Fin de los Vehiculos-------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------------------





#--------------------------------------------------------------Esta es la parte de las Rutas---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def cargar_archivo_rutas():
    archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
    if not archivo:
        print("No se seleccionó ningún archivo.")
        messagebox.showinfo("Información", "No se seleccionó ningún archivo")
        return

    try:
        with open(archivo, "r", encoding="utf-8") as file:
            for linea in file:
                linea = linea.strip()
                if linea.endswith("%"):
                    linea = linea[:-1]  # Eliminar el punto y coma final
                    datos = linea.split("/")
                    if len(datos) == 3:
                        ruta:Ruta = Ruta(origen=datos[0], destino=datos[1], tiempo=int(datos[2]))
                        lista_adyacencia_general.insertar(ruta=ruta)
        print("Carga masiva completada.")
        messagebox.showinfo("Información", "Carga masiva completada")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")




def generar_Grafico_ListaAdyacencia(root):
    try:
        # Generar el texto en formato DOT
        dot: str = lista_adyacencia_general.imprimir()

        # Guardar el texto en un archivo .dot
        with open("Reportes/Rutas.dot", "w") as file:
            file.write(dot)

        # Generar la imagen usando Graphviz
        resultado = os.system("neato -Tpng -Gdpi=300 Reportes/Rutas.dot -o Reportes/Rutas.png")

        # Verificar si el comando se ejecutó correctamente
        if resultado != 0:
            raise RuntimeError("Error al generar la imagen con Graphviz")
        else:
            # Actualizar imagen al cambiar tamaño de ventana
            root.update_idletasks()
            colocar_imagen_VentanaPrincipal(root)
            # Actualizar imagen al redimensionar
            root.bind("<Configure>", lambda event: colocar_imagen_VentanaPrincipal(root))
            messagebox.showinfo("Información", "¡¡¡ Mapa General creado con Exito !!!")
    except Exception as e:
        print(f"Error al generar el gráfico de la lista de adyacencia: {e}")

    #os.startfile("C:/Users/tubac/Downloads/Vacaciones Diciembre 2024/EDD Vacaciones Diciembre 2024/Laboratorio/Proyecto_2/Reportes/Rutas.png")




#---------------------------------------------------------------------------Fin de las Rutas---------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------------------------------------------






def colocar_imagen_VentanaPrincipal(root):
    # Obtener tamaño actual de la ventana
    ancho = root.winfo_width()
    alto = root.winfo_height()

    # Cargar y redimensionar la imagen
    ruta_imagen = "C:/Users/tubac/Downloads/Vacaciones Diciembre 2024/EDD Vacaciones Diciembre 2024/Laboratorio/Proyecto_2/Reportes/Rutas.png"
    try:
        image = Image.open(ruta_imagen)
        image = image.resize((ancho, alto), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image)

        # Crear o actualizar Label
        if hasattr(root, "image_label") and root.image_label is not None:
            root.image_label.config(image=image_tk)
            root.image_label.image = image_tk  # Actualizar referencia
        else:
            root.image_label = Label(root, image=image_tk)
            root.image_label.image = image_tk
            root.image_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")





def main() -> None:

    root = tk.Tk()
    root.title("Interfaz de Gestión")
    root.geometry("900x600")

    # Maximizar la ventana
    root.state("zoomed")  # Maximiza la ventana en Windows y Linux

    create_menu(root)


    root.mainloop()



if __name__ == '__main__':
    main()
