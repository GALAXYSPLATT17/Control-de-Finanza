import customtkinter as ctk

class VistaDashboard(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.master = master
        # self.title("Dashboard")
        # self.geometry("800x600")
        # self.configure(fg_color="#f5f5f5")

        # Título
        self.label_titulo = ctk.CTkLabel(self.master, text="Overview", font=("Arial", 20, "bold"))
        self.label_titulo.grid(row=0, column=0, padx=20, pady=10)


        
        # Gráficos de rendimiento
        # self.frame_graficos = ctk.CTkFrame(self, corner_radius=10)
        # self.frame_graficos.pack(padx=20, pady=10, fill="both", expand=True)

        # Botón para ver detalles
        # self.boton_detalles = ctk.CTkButton(self, text="Ver Detalles", command=self.ver_detalles)
        # self.boton_detalles.pack(pady=10)

    # def ver_detalles(self):
    #     # Lógica para ver detalles del rendimiento
    #     print("Ver detalles del rendimiento")

