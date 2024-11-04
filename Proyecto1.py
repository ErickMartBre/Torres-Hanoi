import tkinter as tk

def __init__(self):
    self.n = 0

def Easy(self):
    self.n = 3
    
    VentanaEasy = tk.Tk()
    VentanaEasy.geometry("800x600")
    VentanaDificultad.destroy()
    
    canvas = tk.Canvas(VentanaEasy, width=500, height=300)
    canvas.place(x=150, y=300)
    
    crearTorres(canvas)
    
def Medium(self):
    self.n = 5
    
    VentanaMedium = tk.Tk()
    VentanaMedium.geometry("800x600")
    VentanaDificultad.destroy()
    
    canvas = tk.Canvas(VentanaMedium, width=500, height=300)
    canvas.place(x=150, y=300)
    
    crearTorres(canvas)
    
def Hard(self):
    self.n = 8
    
    VentanaHard = tk.Tk()
    VentanaHard.geometry("800x600")
    VentanaDificultad.destroy() 
    
    canvas = tk.Canvas(VentanaHard, width=500, height=300)
    canvas.place(x=150, y=300)
    
    crearTorres(canvas)

def crearTorres(canvas,self):
    
    anchoTorre= 10
    altoTorre = 150
    
    canvas.create_rectangle(100 - anchoTorre//2, 200 - altoTorre, 100 + anchoTorre//2, 200, fill="brown")
    
    canvas.create_rectangle(250 - anchoTorre//2, 200 - altoTorre, 250 + anchoTorre//2, 200, fill="brown")
    
    canvas.create_rectangle(400 - anchoTorre//2, 200 - altoTorre, 400 + anchoTorre//2, 200, fill="brown")
    

VentanaDificultad = tk.Tk()
VentanaDificultad.geometry("200x150")

VDLabel = tk.Label(VentanaDificultad, text="Seleccione la dificultad del juego")
VDLabel.pack()

BotonEasy = tk.Button(VentanaDificultad, text="Fácil", command=Easy)
BotonEasy.pack(pady=8)
BotonMedium = tk.Button(VentanaDificultad, text="Medio", command=Medium)
BotonMedium.pack(pady=8)
BotonHard = tk.Button(VentanaDificultad, text="Dificil", command=Hard)
BotonHard.pack(pady=8)
VentanaDificultad.mainloop()