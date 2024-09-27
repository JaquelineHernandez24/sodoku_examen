### Examen sobre la categoria de memoria el cual elegi sodoku
import tkinter as tk
import random

# Tableros de Sudoku de diferentes niveles
tableros_nivel = {
    "fácil": [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ],
    "medio": [
        [0, 0, 0, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 3, 9, 0],
        [3, 0, 9, 0, 4, 0, 0, 8, 0],
        [0, 5, 0, 0, 7, 0, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 0, 0, 0, 9, 0, 0, 6, 0],
        [0, 9, 0, 0, 8, 0, 5, 0, 1],
        [0, 2, 5, 0, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 6, 0, 0, 0]
    ]
}

# Puntaje del juego por nivel y total
puntaje_por_nivel = {}
total_puntaje = 0


# Ventana de bienvenida
def ventana_bienvenida():
    ventana = tk.Tk()
    ventana.title("Bienvenido al Juego de Sudoku")
    ventana.config(bg="#add8e6")  # Fondo azul pastel

    # Etiqueta de bienvenida con fuente personalizada
    label_bienvenida = tk.Label(ventana, text="¡Bienvenido al Juego de Sudoku!", font=("Comic Sans MS", 20, "bold"),
                                bg="#add8e6")
    label_bienvenida.pack(pady=20)

    # Botón con color nude y tipo de letra
    boton_entrar = tk.Button(ventana, text="Entrar", font=("Comic Sans MS", 12), bg="#f5c6a5",
                             command=lambda: [ventana.destroy(), ventana_menu()])
    boton_entrar.pack(pady=10)

    ventana.mainloop()


# Ventana principal del menú
def ventana_menu():
    ventana = tk.Tk()
    ventana.title("Menú Principal")
    ventana.config(bg="#add8e6")  # Fondo azul pastel

    label_menu = tk.Label(ventana, text="Menú Principal", font=("Helvetica", 16), bg="#add8e6")
    label_menu.pack(pady=20)

    boton_instrucciones = tk.Button(ventana, text="Instrucciones",
                                    command=lambda: [ventana.destroy(), ventana_instrucciones()], bg="lightgray",
                                    font=("Helvetica", 14))
    boton_instrucciones.pack(pady=10)

    boton_jugar = tk.Button(ventana, text="Jugar", command=lambda: [ventana.destroy(), ventana_juego()], bg="lightgray",
                            font=("Helvetica", 14))
    boton_jugar.pack(pady=10)

    boton_puntaje = tk.Button(ventana, text="Ver Puntajes", command=lambda: [ventana.destroy(), ventana_puntaje()],
                              bg="lightgray", font=("Helvetica", 14))
    boton_puntaje.pack(pady=10)

    boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, bg="lightgray", font=("Helvetica", 14))
    boton_salir.pack(pady=10)

    ventana.mainloop()


# Ventana de instrucciones
def ventana_instrucciones():
    ventana = tk.Tk()
    ventana.title("Instrucciones")
    ventana.config(bg="#add8e6")  # Fondo azul pastel

    instrucciones = """
    El objetivo del juego es llenar una cuadrícula de 9x9 con números del 1 al 9.
    Cada fila, columna y cuadrante 3x3 debe contener todos los números del 1 al 9 sin repetirse.
    Debes ingresar las coordenadas de la celda (fila, columna) y el número que deseas colocar.
    """

    label_instrucciones = tk.Label(ventana, text=instrucciones, font=("Helvetica", 12), justify="left", bg="#add8e6")
    label_instrucciones.pack(pady=20)

    boton_volver = tk.Button(ventana, text="Volver", command=lambda: [ventana.destroy(), ventana_menu()],
                             bg="lightgray", font=("Helvetica", 14))
    boton_volver.pack(pady=10)

    ventana.mainloop()


# Ventana de puntaje
def ventana_puntaje():
    ventana = tk.Tk()
    ventana.title("Puntaje")
    ventana.config(bg="#add8e6")  # Fondo azul pastel

    label_puntaje_total = tk.Label(ventana, text=f"Puntaje total: {total_puntaje}", font=("Helvetica", 14),
                                   bg="#add8e6")
    label_puntaje_total.pack(pady=10)

    for nivel, puntaje in puntaje_por_nivel.items():
        label_puntaje_nivel = tk.Label(ventana, text=f"Puntaje en nivel {nivel}: {puntaje}", font=("Helvetica", 12),
                                       bg="#add8e6")
        label_puntaje_nivel.pack()

    boton_volver = tk.Button(ventana, text="Volver", command=lambda: [ventana.destroy(), ventana_menu()],
                             bg="lightgray", font=("Helvetica", 14))
    boton_volver.pack(pady=10)

    ventana.mainloop()


# Ventana de juego
def ventana_juego():
    ventana = tk.Tk()
    ventana.title("Juego de Sudoku")
    ventana.config(bg="#add8e6")  # Fondo azul pastel

    tablero, nivel = seleccionar_tablero()
    puntaje = 0  # Puntaje inicial para este nivel

    label_nivel = tk.Label(ventana, text=f"Seleccionaste el Nivel {nivel.capitalize()}", font=("Helvetica", 14),
                           bg="#add8e6")
    label_nivel.pack(pady=20)

    # Mostrar tablero de Sudoku en la ventana
    frame_tablero = tk.Frame(ventana)
    frame_tablero.pack()

    entradas = []  # Almacenar las entradas del jugador para luego usarlas
    for i in range(9):
        fila = []
        for j in range(9):
            celda = tk.Entry(frame_tablero, width=2, font=("Helvetica", 18), justify="center")
            celda.grid(row=i, column=j, padx=5, pady=5)

            # Colorear celdas
            if tablero[i][j] != 0:
                celda.insert(0, tablero[i][j])
                celda.config(state="disabled", bg="lightblue")  # Color para celdas prellenadas
            else:
                celda.config(bg="lightyellow")  # Color para celdas vacías y editables

            fila.append(celda)
        entradas.append(fila)

    def verificar_jugada():
        global total_puntaje
        # Simular verificación de jugada correcta (aquí podrías implementar la lógica completa)
        movimiento_valido = random.choice([True, False])
        if movimiento_valido:
            puntaje_por_nivel[nivel] = puntaje + 1
            total_puntaje += 1
            resultado.set("Movimiento válido")
        else:
            resultado.set("Movimiento no válido")

    resultado = tk.StringVar()
    resultado.set("Realiza una jugada")

    label_resultado = tk.Label(ventana, textvariable=resultado, font=("Helvetica", 12), bg="#add8e6")
    label_resultado.pack(pady=10)

    boton_verificar = tk.Button(ventana, text="Verificar Jugada", command=verificar_jugada, bg="lightgray",
                                font=("Helvetica", 14))
    boton_verificar.pack(pady=10)

    boton_volver = tk.Button(ventana, text="Volver", command=lambda: [ventana.destroy(), ventana_menu()],
                             bg="lightgray", font=("Helvetica", 14))
    boton_volver.pack(pady=10)

    ventana.mainloop()


# Función para seleccionar tablero aleatoriamente
def seleccionar_tablero():
    nivel = random.choice(["fácil", "medio"])
    return tableros_nivel[nivel], nivel


# Iniciar el programa mostrando la ventana de bienvenida
ventana_bienvenida()
