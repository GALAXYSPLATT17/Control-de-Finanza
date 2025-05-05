import customtkinter as ctk

# Configuración de la aplicación principal
class VistaListaTransacciones(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Transacciones")
        self.geometry("800x600")
        self.configure(fg_color="#f5f5f5")

        # Título
        self.label_titulo = ctk.CTkLabel(self, text="Lista de Transacciones", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        # Tabla de transacciones
        self.frame_tabla = ctk.CTkFrame(self, corner_radius=10)
        self.frame_tabla.pack(padx=20, pady=10, fill="both", expand=True)

        self.tabla = ctk.CTkTextbox(self.frame_tabla, font=("Arial", 12), wrap="none")
        self.tabla.pack(padx=10, pady=10, fill="both", expand=True)
        self.tabla.insert("0.0", "ID\tFecha\tDescripción\tMonto\n")
        self.tabla.insert("end", "-"*50 + "\n")

        # Botón para agregar transacción
        self.boton_agregar = ctk.CTkButton(self, text="Agregar Transacción", command=self.agregar_transaccion)
        self.boton_agregar.pack(pady=10)

    def agregar_transaccion(self):
        # Lógica para agregar una nueva transacción
        print("Agregar nueva transacción")

# # Ejecución de la aplicación
# if __name__ == "__main__":
#     app = VistaListaTransacciones()
#     app.mainloop()

