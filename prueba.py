import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp
from PIL import Image, ImageTk

# función para dividir recursivamente el arreglo
def orden_merge(arreglo, inicio, fin):
    if fin <= inicio:
        return

    medio = inicio + ((fin - inicio + 1) // 2) - 1

    yield from orden_merge(arreglo, inicio, medio)
    yield from orden_merge(arreglo, medio + 1, fin)
    yield from mezclar(arreglo, inicio, medio, fin)

# función para mezclar el arreglo
def mezclar(arreglo, inicio, medio, fin):
    mezclado = []
    indiceIzquierdo = inicio
    indiceDerecho = medio + 1

    while indiceIzquierdo <= medio and indiceDerecho <= fin:
        if arreglo[indiceIzquierdo] < arreglo[indiceDerecho]:
            mezclado.append(arreglo[indiceIzquierdo])
            indiceIzquierdo += 1
        else:
            mezclado.append(arreglo[indiceDerecho])
            indiceDerecho += 1

    while indiceIzquierdo <= medio:
        mezclado.append(arreglo[indiceIzquierdo])
        indiceIzquierdo += 1

    while indiceDerecho <= fin:
        mezclado.append(arreglo[indiceDerecho])
        indiceDerecho += 1

    for i in range(len(mezclado)):
        arreglo[inicio + i] = mezclado[i]
        yield arreglo

# función para graficar las barras
def mostrar_grafico(valores):
    n = len(valores)
    nombre_dataset = 'Entrada del Usuario'
    generador = orden_merge(valores, 0, len(valores) - 1)
    nombre_algo = 'Algoritmo Merge Sort'

    plt.style.use('fivethirtyeight')

    # Usar un colormap estándar
    normalizador_datos = mp.colors.Normalize()
    mapa_colores = plt.get_cmap("viridis")  # Usar un colormap predefinido

    figura, ejes = plt.subplots()

    barras_rectangulares = ejes.bar(range(len(valores)), valores, align="edge",color=mapa_colores(normalizador_datos(range(n))))

    ejes.set_xlim(0, len(valores))
    ejes.set_ylim(0, int(1.1 * max(valores)))  # Cambiar a max(valores) para un rango dinámico
    ejes.set_title("ALGORITMO : " + nombre_algo + "\n" + "CONJUNTO DE DATOS : " + nombre_dataset,
                   fontdict={'fontsize': 13, 'fontweight': 'medium','color': '#E4365D'})

    texto = ejes.text(0.01, 0.95, "", transform=ejes.transAxes, color="#E4365D")
    iteracion = [0]

    def animar(arreglo, rectangulos, iteracion):
        for rect, val in zip(rectangulos, arreglo):
            rect.set_height(val)
        iteracion[0] += 1
        texto.set_text("iteraciones : {}".format(iteracion[0]))

    anim = FuncAnimation(figura, func=animar,
                        fargs=(barras_rectangulares, iteracion), frames=generador, 
                        interval=50, repeat=False, cache_frame_data=False)
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

    label = tk.Label(ventana_presentacion, text=texto_presentacion, justify="center", padx=10, pady=10)
    label.pack()

    exit_button = tk.Button(ventana_presentacion, text="REGRESAR", command=ventana_presentacion.destroy)
    exit_button.pack(pady=20)

def crear_entradas():
    # Crear una nueva ventana para las entradas
    ventana_entradas = tk.Toplevel()
    ventana_entradas.title("Entradas algoritmo merge sort")
    ventana_entradas.geometry("500x400")

    tk.Label(ventana_entradas, text="Introduzca 8 elementos:").pack(pady=10)
    
    # Crear campos de entrada para la entrada del usuario
    entradas = []
    for i in range(8):
        entrada = tk.Entry(ventana_entradas)
        entrada.pack(pady=5)
        entradas.append(entrada)

    # Crear un botón para enviar la entrada
    boton_enviar = tk.Button(ventana_entradas, text="Ordenar", command=lambda: obtener_entrada(entradas))
    boton_enviar.pack(pady=20)
    boton_regresar = tk.Button(ventana_entradas, text="Regresar", command=lambda: [ventana_entradas.destroy(), ventana.deiconify()])
    boton_regresar.pack(pady=20)
# función para obtener la entrada del usuario y comenzar el ordenamiento
def obtener_entrada(entradas):
    try:
        valores = [int(entry.get()) for entry in entradas]
        if len(valores) != 8:
            raise ValueError("Por favor, ingrese exactamente 8 números.")

        mostrar_grafico(valores)
    except ValueError as e:
        messagebox.showerror("Error de Entrada", str(e))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("ALGORITMO DE ORDENACION MERGE SORT")
ventana.geometry("500x300")

frame = tk.Frame(ventana)
frame.pack(pady=10)
"""
try:
    image_path = "imagenes/empresas_hou_oficial.jpg"
    image = Image.open(image_path)
    image = image.resize((450, 250), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(frame, image=photo)
    image_label.image = photo
    image_label.pack(pady=10)
except Exception as e:
    messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")
"""
    
# Crear la barra de menú
menu_bar = tk.Menu(ventana)

menu_prin = tk.Menu(menu_bar, tearoff=0)
menu_prin.add_command(label="Presentación", command=Presentacion)
menu_prin.add_command(label="Algoritmo Merge Sort", command=crear_entradas)
menu_prin.add_separator()
menu_prin.add_command(label="Salir", command=ventana.quit)

menu_bar.add_cascade(label="Menu", menu=menu_prin)

ventana.config(menu=menu_bar)

# Ejecutar el bucle principal
ventana.mainloop()