#Inicio Algoritmo
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

#Clase que visualiza el algoritmo de ordenamiento Merge Sort utilizando una interfaz gráfica de usuario (GUI) con Tkinter.
class VisualizadorMergeSort: 
    
    #Inicializa los componentes de la interfaz gráfica y la configuración inicial.
    def __init__(self, root): 

        self.root = root  # Guarda la ventana principal
        self.root.title("Algoritmo de Ordenamiento Merge Sort")  # Título de la ventana
        self.root.geometry("1280x750")  # Tamaño de la ventana
        self.datos = []  # Lista que almacenará los datos introducidos por el usuario

        # Crear el marco del título
        self.marco_titulo = tk.Frame(self.root, bg="SkyBlue", pady=10)  # Marco para el título con fondo azul claro
        self.marco_titulo.pack(fill=tk.X)  # Empaqueta el marco para que ocupe toda la anchura
        logo_python = Image.open("poco_prime.jpg").resize((300, 250), Image.LANCZOS)  # Carga y redimensiona la imagen
        self.imagen_python = ImageTk.PhotoImage(logo_python)  # Convierte la imagen para usarla en Tkinter
        tk.Label(self.marco_titulo, image=self.imagen_python, bg="Blue").pack(side=tk.LEFT, padx=10)  # Muestra la imagen en el marco 
        # Muestra el título en el marco
        tk.Label(self.marco_titulo, text="Algoritmo de Ordenamiento Merge Sort", font=("Montserrat", 30, "bold"), bg="SkyBlue").pack(side=tk.LEFT) 

        # Crear el marco de entrada
        self.marco_entrada = tk.Frame(self.root, bg="black", pady=10)  # Marco para los controles de entrada del usuario
        self.marco_entrada.pack(fill=tk.X)  # Empaqueta el marco para que ocupe toda la anchura
        # Etiqueta para indicar lo que debe ingresar el usuario
        tk.Label(self.marco_entrada, text="Ingrese valores (8-10) separados por comas (,):", font=("Arial", 14), bg="SkyBlue").pack(side=tk.LEFT, padx=10)  
        self.entrada_usuario = tk.Entry(self.marco_entrada, font=("Arial", 14), width=40)  # Caja de texto donde el usuario ingresa los datos
        self.entrada_usuario.pack(side=tk.LEFT, padx=10)  # Empaqueta la caja de texto
        self.boton_iniciar = tk.Button(self.marco_entrada, text="Iniciar", font=("Arial", 14), command=self.comenzar_ordenamiento)  # Botón para iniciar el ordenamiento
        self.boton_iniciar.pack(side=tk.LEFT, padx=10)  # Empaqueta el botón

        # Crear el canvas para mostrar las carpetas
        self.lienzo = tk.Canvas(self.root, bg="white", height=500)  # Área de dibujo donde se mostrarán los valores como carpetas
        self.lienzo.pack(fill=tk.BOTH, expand=True)  # Empaqueta el lienzo para que ocupe todo el espacio disponible

        # Actualizar valores al escribir
        self.entrada_usuario.bind("<KeyRelease>", self.cargar_vista_previa)  # Evento que se activa cuando se suelta una tecla en la caja de texto

        # Cargar y redimensionar la imagen de carpeta
        imagen_original = Image.open("folder.png").resize((80, 60), Image.LANCZOS)  # Carga y redimensiona la imagen de la carpeta
        self.imagen_carpeta = ImageTk.PhotoImage(imagen_original)  # Convierte la imagen para usarla en Tkinter
    #Muestra los valores ingresados en el lienzo como una vista previa.
    def cargar_vista_previa(self, event=None):
        entrada_usuario = self.entrada_usuario.get()  # Obtiene el texto ingresado por el usuario
        try:
            datos = [int(valor.strip()) for valor in entrada_usuario.split(",") if valor.strip()]  # Convierte la entrada en una lista de enteros
            self.dibujar_carpetas(datos, "Vista previa: Carpetas ingresadas")  # Llama a la función para dibujar las carpetas
        except ValueError:  # Si ocurre un error de conversión, muestra un mensaje de error
            self.dibujar_carpetas([], "Entrada no válida: Corregir valores")  # Muestra mensaje de error en el lienzo
            
    #Dibuja las carpetas (valores) en el lienzo. Permitiendo resaltar ciertos índices.
    def dibujar_carpetas(self, datos, titulo="", resaltar_indices=None, color_resaltar="green"):
        self.lienzo.delete("all")  # Elimina cualquier contenido previo del lienzo
        self.lienzo.create_text(500, 20, text=titulo, font=("Arial", 16, "bold"))  # Muestra el título en el lienzo
        if not datos:
            self.lienzo.create_text(500, 250, text="Estimado usuario, ingrese valores para comenzar", font=("Arial", 18, "italic"), fill="grey") 
            return # Muestra un mensaje si no hay datos

        # Cálculo de posiciones para dibujar las carpetas
        ancho_lienzo = self.lienzo.winfo_width()  # Obtiene el ancho disponible del lienzo
        ancho_carpeta = self.imagen_carpeta.width()  # Ancho de la imagen de la carpeta
        altura_carpeta = self.imagen_carpeta.height()  # Altura de la imagen de la carpeta
        espacio_carpeta = 20  # Espacio entre cada carpeta
        ancho_total = len(datos) * ancho_carpeta + (len(datos) - 1) * espacio_carpeta  # Calcula el ancho total necesario para todas las carpetas
        inicio_x = (ancho_lienzo - ancho_total) // 2  # Calcula la posición X inicial para centrar las carpetas
        y = 300 - altura_carpeta // 2  # Calcula la posición Y para centrar las carpetas verticalmente

        self.posiciones_carpetas = []  # Lista que almacenará las posiciones de las carpetas para usarlas durante la animación

        # Dibuja cada carpeta en el lienzo
        for i, valor in enumerate(datos):
            x = inicio_x + i * (ancho_carpeta + espacio_carpeta)  # Calcula la posición X de cada carpeta

            # Dibuja la imagen de la carpeta
            id_imagen = self.lienzo.create_image(x + ancho_carpeta // 2, y, anchor=tk.CENTER, image=self.imagen_carpeta)
            
            # Resalta los índices especificados
            if resaltar_indices and i in resaltar_indices:
                self.lienzo.create_rectangle(
                    x, y, x + ancho_carpeta, y + altura_carpeta,
                    outline=color_resaltar, width=3  # Dibuja un rectángulo alrededor de la carpeta si se va a resaltar
                )

            # Dibuja el número dentro de la carpeta
            id_texto = self.lienzo.create_text(
                x + ancho_carpeta // 2, y + altura_carpeta // 2, 
                text=str(valor), font=("Arial", 14, "bold"), fill="black"
            )
            self.posiciones_carpetas.append((id_imagen, id_texto, x, y))  # Guarda la posición de la carpeta para futuras animaciones
        self.root.update()  # Actualiza la interfaz gráfica

    #Implementación recursiva del algoritmo Merge Sort.
    def merge_sort(self, datos, izquierda, derecha):
        if izquierda < derecha:
            medio = (izquierda + derecha) // 2  # Calcula el índice medio para dividir los datos

            # Resalta la parte izquierda que se está dividiendo
            self.dibujar_carpetas(datos, "Dividiendo - Lado izquierdo", resaltar_indices=range(izquierda, medio + 1), color_resaltar="blue")
            self.root.update()  # Actualiza la interfaz gráfica
            time.sleep(2.5)  # Pausa para mostrar la animación

            self.merge_sort(datos, izquierda, medio)  # Llama recursivamente para ordenar la mitad izquierda

            # Resalta la parte derecha que se está dividiendo
            self.dibujar_carpetas(datos, "Dividiendo - Lado derecho", resaltar_indices=range(medio + 1, derecha + 1), color_resaltar="orange")
            self.root.update()  # Actualiza la interfaz gráfica
            time.sleep(2.5)  # Pausa para mostrar la animación

            self.merge_sort(datos, medio + 1, derecha)  # Llama recursivamente para ordenar la mitad derecha

            # Fusiona las dos mitades ordenadas
            self.fusionar(datos, izquierda, medio, derecha)

    #Función para fusionar dos sublistas ordenadas en una sola lista ordenada.
    def fusionar(self, datos, izquierda, medio, derecha):
        # Crea copias de las sublistas
        copia_izquierda = datos[izquierda:medio + 1]
        copia_derecha = datos[medio + 1:derecha + 1]
        indice_izquierda, indice_derecha = 0, 0
        indice_ordenado = izquierda

        # Resalta el proceso de fusión
        self.dibujar_carpetas(datos, "Combinando y ordenando", resaltar_indices=range(izquierda, derecha + 1), color_resaltar="green")
        self.root.update()  # Actualiza la interfaz gráfica
        time.sleep(2.5)  # Pausa para mostrar la animación

        # Fusiona las dos sublistas ordenadas
        while indice_izquierda < len(copia_izquierda) and indice_derecha < len(copia_derecha):
            if copia_izquierda[indice_izquierda] <= copia_derecha[indice_derecha]:
                datos[indice_ordenado] = copia_izquierda[indice_izquierda]
                indice_izquierda += 1
            else:
                datos[indice_ordenado] = copia_derecha[indice_derecha]
                indice_derecha += 1
            indice_ordenado += 1

        # Si quedan elementos en la copia izquierda, se agregan a la lista
        while indice_izquierda < len(copia_izquierda):
            datos[indice_ordenado] = copia_izquierda[indice_izquierda]
            indice_izquierda += 1
            indice_ordenado += 1

        # Si quedan elementos en la copia derecha, se agregan a la lista
        while indice_derecha < len(copia_derecha):
            datos[indice_ordenado] = copia_derecha[indice_derecha]
            indice_derecha += 1
            indice_ordenado += 1

        # Muestra el estado después de la fusión
        self.dibujar_carpetas(datos, "Resultado después de combinar", resaltar_indices=range(izquierda, derecha + 1), color_resaltar="green")
        self.root.update()  # Actualiza la interfaz gráfica
        time.sleep(2.5)  # Pausa para mostrar la animación
    
    #Valida la entrada del usuario para asegurarse de que los valores sean números enteros y que la lista tenga entre 8 y 10 elementos.
    def validar_entrada(self): 
        entrada_usuario = self.entrada_usuario.get()  # Obtiene el texto ingresado por el usuario
        try:
            datos = [int(valor.strip()) for valor in entrada_usuario.split(",")]  # Convierte la entrada en una lista de enteros
            if len(datos) < 8 or len(datos) > 10:  # Verifica que haya entre 8 y 10 elementos
                raise ValueError
            return datos
        except ValueError:  # Si ocurre un error de conversión, muestra un mensaje de error
            messagebox.showerror("Error", "Entrada inválida. Ingrese entre 8 y 10 valores numéricos separados por comas.")
            return None

    #Si los datos de entradas son válidos comienza el proceso de ordenamiento
    def comenzar_ordenamiento(self):
        datos = self.validar_entrada()  # Valida la entrada del usuario
        if datos:  # Si los datos son válidos, empieza el ordenamiento
            self.datos = datos
            self.dibujar_carpetas(self.datos, "Estado inicial: Carpetas desordenadas")  # Muestra el estado inicial
            self.merge_sort(self.datos, 0, len(self.datos) - 1)  # Ejecuta el algoritmo Merge Sort
            self.dibujar_carpetas(self.datos, "Estado final: Carpetas ordenadas")  # Muestra el estado final

# Configurar la ventana principal
root = tk.Tk()
app = VisualizadorMergeSort(root)  # Crea la instancia del visualizador
root.mainloop()  # Ejecuta el ciclo principal de la interfaz gráfica
#Fin Algoritmo