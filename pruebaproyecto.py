import tkinter as tk

class TorresDeHanoi:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Torres de Hanoi")

        self.canvas = tk.Canvas(self.ventana, width=500, height=300)
        self.canvas.pack()

        # Variables para manejar los discos
        self.discos = []
        self.torres = [[], [], []]  # Tres torres vacías
        self.seleccionado = None

        self.crear_palos()
        self.crear_discos()

        self.canvas.bind("<Button-1>", self.click_handler)

    def crear_palos(self):
        # Dibujar los palos
        ancho_palo = 10
        alto_palo = 150
        self.palos = [
            self.canvas.create_rectangle(100 - ancho_palo // 2, 200 - alto_palo, 100 + ancho_palo // 2, 200, fill="brown"),
            self.canvas.create_rectangle(250 - ancho_palo // 2, 200 - alto_palo, 250 + ancho_palo // 2, 200, fill="brown"),
            self.canvas.create_rectangle(400 - ancho_palo // 2, 200 - alto_palo, 400 + ancho_palo // 2, 200, fill="brown")
        ]

    def crear_discos(self):
        # Lista de colores para los discos
        colores = ["blue", "green", "red"]
        # Crear discos de diferentes tamaños y colores, colocándolos en la primera torre
        for i, (width, color) in enumerate(zip([100, 80, 60], colores)):
            disco = self.canvas.create_rectangle(100 - width // 2, 180 - i * 20, 100 + width // 2, 200 - i * 20, fill=color)
            self.discos.append(disco)
            self.torres[0].append(disco)

    def click_handler(self, evento):
        x, y = evento.x, evento.y

        # Si ya hay un disco seleccionado, intenta moverlo a una torre
        if self.seleccionado:
            for i, palo in enumerate(self.palos):
                coords = self.canvas.coords(palo)
                if coords[0] < x < coords[2]:  # Si el clic está dentro del área del palo
                    torre_actual = self.obtener_torre_actual(self.seleccionado)

                    # Solo permite el movimiento si la torre de destino está vacía o el disco es más pequeño
                    if torre_actual is not None and (not self.torres[i] or self.seleccionado < self.torres[i][-1]):
                        self.torres[torre_actual].remove(self.seleccionado)
                        self.torres[i].append(self.seleccionado)
                        self.ajustar_posicion_disco(self.seleccionado, i)
                    # Deselecciona el disco
                    self.seleccionado = None
                    return

        # Si no hay un disco seleccionado, intenta seleccionar uno
        for torre in self.torres:
            if torre and self.canvas.coords(torre[-1])[0] < x < self.canvas.coords(torre[-1])[2] and self.canvas.coords(torre[-1])[1] < y < self.canvas.coords(torre[-1])[3]:
                self.seleccionado = torre[-1]
                break

    def obtener_torre_actual(self, disco):
        for i, torre in enumerate(self.torres):
            if disco in torre:
                return i
        return None

    def ajustar_posicion_disco(self, disco, torre):
        index = len(self.torres[torre]) - 1
        x_centro = 100 + torre * 150
        width = self.canvas.coords(disco)[2] - self.canvas.coords(disco)[0]
        self.canvas.coords(disco, x_centro - width // 2, 180 - index * 20, x_centro + width // 2, 200 - index * 20)

# Iniciar el juego
TorresDeHanoi()
tk.mainloop()