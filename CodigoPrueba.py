#Inicio Algoritmo
#importamos las librerias
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
from PIL import Image, ImageTk

# Función para dividir recursivamente el arreglo
def orden_merge(arreglo, inicio, fin):
    # Si el índice de inicio es mayor o igual que el índice de fin, no hay nada que ordenar
    if fin <= inicio:
        return

    # Calcular el índice medio para dividir el arreglo
    medio = inicio + ((fin - inicio + 1) // 2) - 1

    # Llamar recursivamente a la función para dividir la mitad izquierda
    yield from orden_merge(arreglo, inicio, medio)
    # Llamar recursivamente a la función para dividir la mitad derecha
    yield from orden_merge(arreglo, medio + 1, fin)
    # Mezclar las dos mitades ordenadas
    yield from mezclar(arreglo, inicio, medio, fin)

# Función para mezclar el arreglo
def mezclar(arreglo, inicio, medio, fin):
    # Crear una lista temporal para almacenar los elementos mezclados
    mezclado = []
    # Inicializar los índices para las dos mitades
    indiceIzquierdo = inicio
    indiceDerecho = medio + 1

    # Comparar y mezclar los elementos de las dos mitades
    while indiceIzquierdo <= medio and indiceDerecho <= fin:
        if arreglo[indiceIzquierdo] < arreglo[indiceDerecho]:
            mezclado.append(arreglo[indiceIzquierdo])  # Agregar el elemento menor a la lista mezclada
            indiceIzquierdo += 1  # Mover el índice izquierdo hacia la derecha
        else:
            mezclado.append(arreglo[indiceDerecho])  # Agregar el elemento menor a la lista mezclada
            indiceDerecho += 1  # Mover el índice derecho hacia la derecha

    # Agregar los elementos restantes de la mitad izquierda (si los hay)
    while indiceIzquierdo <= medio:
        mezclado.append(arreglo[indiceIzquierdo])
        indiceIzquierdo += 1

    # Agregar los elementos restantes de la mitad derecha (si los hay)
    while indiceDerecho <= fin:
        mezclado.append(arreglo[indiceDerecho])
        indiceDerecho += 1

    # Copiar los elementos mezclados de nuevo al arreglo original
    for i in range(len(mezclado)):
        arreglo[inicio + i] = mezclado[i]
        yield arreglo  # Generar el estado del arreglo después de cada mezcla

anim = None #Inicializamos la variable anim

# Función para graficar las barras
def mostrar_grafico(valores):
    global anim  # Declarar la variable anim como global para poder accederla fuera de la función
    plt.close('all')  # Cierra todas las figuras abiertas para evitar superposiciones

    n = len(valores)  # Obtener la longitud del arreglo de valores
    generador = orden_merge(valores, 0, len(valores) - 1)  # Crear un generador para el algoritmo Merge Sort
    nombre_algo = 'Algoritmo Merge Sort'  # Nombre del algoritmo para el título del gráfico

    plt.style.use('fivethirtyeight')  # Establecer el estilo del gráfico
    normalizador_datos = mp.colors.Normalize()  # Normalizar los datos para la escala de colores
    mapa_colores = plt.get_cmap("viridis")  # Obtener un mapa de colores

    # Crear la figura y los ejes para el gráfico
    figura, ejes = plt.subplots()
    # Crear las barras rectangulares del gráfico
    barras_rectangulares = ejes.bar(range(len(valores)), valores, align="edge", color=mapa_colores(normalizador_datos(range(n))))

    # Configurar el título del gráfico
    ejes.set_title(nombre_algo, fontdict={'fontsize': 14, 'fontweight': 'bold', 'color': '#E4365D'}, pad=30)

    # Mostrar los valores ingresados en el gráfico
    iniciales_texto = "Valores ingresados: " + ", ".join(map(str, valores))
    figura.text(0.5, 0.88, iniciales_texto, ha='center', va='center', fontsize=11, color="#E4365D")

    # Texto para mostrar el número de iteraciones
    texto_iteraciones = ejes.text(-0.05, 1.1, "Iteraciones: 0", transform=ejes.transAxes, 
                                   color="#E4365D", fontsize=10, ha='left', va='center')

    iteracion = [0]  # Inicializar un contador de iteraciones en forma de lista para ser mutable

    # Ocultar los valores del eje y
    ejes.set_yticks([])

    # Función para actualizar la animación
    def animar(arreglo, rectangulos, iteracion):
        # Actualizar la altura de cada barra en el gráfico según los valores actuales
        for rect, val in zip(rectangulos, arreglo):
            rect.set_height(val)
        ejes.set_xticks(range(len(arreglo)))  # Actualizar las marcas en el eje x
        ejes.set_xticklabels(arreglo)  # Establecer las etiquetas del eje x a los valores actuales
        iteracion[0] += 1  # Incrementar el contador de iteraciones
        texto_iteraciones.set_text("Iteraciones: {}".format(iteracion[0]))  # Actualizar el texto de iteraciones

    # Asignar la animación a una variable
    anim = FuncAnimation(figura, func=animar,
                         fargs=(barras_rectangulares, iteracion), frames=generador, 
                         interval=50, repeat=False, cache_frame_data=False)

    # Mostrar la animación
    plt.show()
    
def Presentacion():
    # Crear una ventana de presentación
    ventana_presentacion = tk.Toplevel()  # Usar Toplevel para abrir una nueva ventana
    ventana_presentacion.title("Presentación del Proyecto")

    # Crear el texto de presentación
    texto_presentacion = (
        "\n{:^70}\n"
        "{:^70}\n"
        "{:^70}\n\n"
        "{:^70}\n\n"
        "{:^70}\n"
        "{:^78}\n"
        "{:^80}\n"
        "{:^76}\n"
        "{:^76}\n\n"
        "{:^70}\n\n"
        "{:^70}\n\n"
    ).format(
        "UNIVERSIDAD TECNOLÓGICA DE PANAMÁ",
        "FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES",
        "DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS",
        "PROYECTO SEMESTRAL",
        "Integrantes: Miguel Arosemana 8-1016-2330",
        "Edward Camaño 8-1010-515",
        "Diego Corrales 8-1001-1890",
        "Edwin Hou 8-1021-1916",
        "Josue Pino 8-1012-688",
        "Profesor: Ing. Samuel Jimenez",
        "SEMESTRE II, 2024"
    )
    
    # Crear una etiqueta (label) en la ventana de presentación
    label = tk.Label(ventana_presentacion, text=texto_presentacion, justify="center", padx=10, pady=10)
    label.pack()  # Añadir la etiqueta a la ventana y permitir que se ajuste automáticamente

    # Crear un botón que cierra la ventana de presentación cuando se hace clic en él
    exit_button = tk.Button(ventana_presentacion, text="REGRESAR", command=ventana_presentacion.destroy)
    exit_button.pack(pady=20)  # Añadir el botón a la ventana con un margen vertical de 20 píxeles
    
def crear_entradas():
    # Crear una nueva ventana para las entradas del usuario
    ventana_entradas = tk.Toplevel()  # Toplevel crea una nueva ventana independiente
    ventana_entradas.title("Entradas algoritmo merge sort")  # Establecer el título de la ventana
    ventana_entradas.geometry("500x400")  # Establecer el tamaño de la ventana

    # Etiqueta que indica al usuario que introduzca 8 elementos
    tk.Label(ventana_entradas, text="Introduzca 8 elementos:").pack(pady=10)
    
    # Crear una lista para almacenar los campos de entrada
    entradas = []
    for i in range(8):  # Crear 8 campos de entrada
        entrada = tk.Entry(ventana_entradas)  # Crear un campo de entrada
        entrada.pack(pady=5)  # Añadir el campo a la ventana con un margen vertical
        entradas.append(entrada)  # Añadir el campo a la lista de entradas

    # Crear un botón para enviar la entrada del usuario
    boton_enviar = tk.Button(ventana_entradas, text="Ordenar", command=lambda: obtener_entrada(entradas))
    boton_enviar.pack(pady=20)  # Añadir el botón a la ventana con un margen vertical

    # Crear un botón para regresar a la ventana principal
    boton_regresar = tk.Button(ventana_entradas, text="Regresar", command=lambda: [ventana_entradas.destroy(), ventana.deiconify()])
    boton_regresar.pack(pady=20)  # Añadir el botón a la ventana con un margen vertical
    
# Función para obtener la entrada del usuario y comenzar el ordenamiento
def obtener_entrada(entradas):
    try:
        valores = []  # Lista para almacenar los valores ingresados
        for entry in entradas:  # Iterar sobre cada campo de entrada
            valor = entry.get()  # Obtener el texto del campo de entrada
            if valor.strip() == "":  # Verificar si la entrada está vacía
                raise ValueError("Por favor, no deje campos vacíos.")  # Lanzar un error si está vacío
            try:
                valores.append(int(valor))  # Intentar convertir el valor a un entero
            except ValueError:
                raise ValueError(f"La entrada '{valor}' no es un número válido.")  # Manejar la conversión fallida

        # Verificar que se hayan ingresado exactamente 8 números
        if len(valores) != 8:
            raise ValueError("Por favor, ingrese exactamente 8 números.")

        mostrar_grafico(valores)  # Llamar a la función para mostrar el gráfico con los valores ingresados
    except ValueError as e:
        messagebox.showerror("Error de Entrada", str(e))  # Mostrar un mensaje de error si hay problemas con la entrada

# Crear la ventana principal
ventana = tk.Tk()  # Inicializar la ventana principal
ventana.title("ALGORITMO DE ORDENACION MERGE SORT")  # Establecer el título de la ventana
ventana.geometry("500x300")  # Establecer el tamaño de la ventana

frame = tk.Frame(ventana)  # Crear un marco para organizar los widgets
frame.pack(pady=10)  # Añadir el marco a la ventana con un margen vertical

try:
    # Intentar cargar y mostrar una imagen
    image_path = "imagen.jpg"  # Ruta de la imagen
    image = Image.open(image_path)  # Abrir la imagen
    image = image.resize((450, 250), Image.LANCZOS)  # Redimensionar la imagen
    photo = ImageTk.PhotoImage(image)  # Convertir la imagen a un formato que tkinter puede usar
    image_label = tk.Label(frame, image=photo)  # Crear una etiqueta para mostrar la imagen
    image_label.image = photo  # Mantener una referencia a la imagen
    image_label.pack(pady=10)  # Añadir la etiqueta a la ventana con un margen vertical
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")  # Mostrar un mensaje de error si la imagen no se carga

# Crear la barra de menú
menu_bar = tk.Menu(ventana)  # Crear una barra de menú

# Crear un menú desplegable
menu_prin = tk.Menu(menu_bar, tearoff=0)  # Crear un menú sin separación
menu_prin.add_command(label="Presentación", command=Presentacion)  # Opción para mostrar la presentación
# Opción para abrir la ventana de entradas del algoritmo Merge Sort
menu_prin.add_command(label="Algoritmo Merge Sort", command=crear_entradas)  
menu_prin.add_separator()  # Añadir un separador en el menú
menu_prin.add_command(label="Salir", command=ventana.quit)  # Opción para salir de la aplicación

# Añadir el menú principal a la barra de menú
menu_bar.add_cascade(label="Menu", menu=menu_prin)  

# Configurar la ventana principal para usar la barra de menú
ventana.config(menu=menu_bar)  

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()  # Mantener la ventana abierta y esperar a que el usuario interactúe
#Fin Algoritmo