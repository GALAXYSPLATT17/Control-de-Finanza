import customtkinter as ctk
# from Controlapp.Views import vista_lista_transacciones as LT
from Controlapp.Views import dashboard as VD


class App ():
    def __init__ (self):
        super().__init__ ()
        self.ventana = ctk.CTk ()
        self.ventana.geometry ("800x600")
        self.ventana.title ("Control de Finanzas")

        # self.label = ctk.CTkLabel (self.ventana, text="Overview", font=("Arial", 20, "bold"))
        # self.label.grid (row=0, column=0, padx=20, pady=10)
        dash = VD.VistaDashboard(self.ventana)

        self.ventana.mainloop ()




app = App ()
# app.ventana.mainloop()