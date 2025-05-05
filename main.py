import customtkinter as ctk
from Controlapp.Views import vista_lista_transacciones as LT

class App (ctk.CTk):
    def __init__ (self):
        super().__init__ ()
        self.ventana = ctk.CTk ()
        self.ventana.geometry ("800x600")
        self.ventana.title ("Control de Finanzas")
        self.ventana.mainloop ()

        transactionList = LT.VistaListaTransacciones (self) 



app = App ()
app.ventana.mainloop ()