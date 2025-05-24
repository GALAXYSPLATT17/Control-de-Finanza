import customtkinter as ctk


class PopupNuevaCuenta(ctk.CTkToplevel):
    def __init__(self, master, on_submit=None):
        super().__init__(master)
        self.title("Nueva Cuenta Bancaria")
        self.geometry("350x200")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Nombre de la cuenta:").pack(pady=(8, 2))
        self.entry_nombre = ctk.CTkEntry(self)
        self.entry_nombre.pack(pady=2)

        ctk.CTkLabel(self, text="Saldo inicial:").pack(pady=2)
        self.entry_saldo = ctk.CTkEntry(self)
        self.entry_saldo.pack(pady=2)

        self.btn_crear = ctk.CTkButton(self, text="Crear", command=self.submit)
        self.btn_crear.pack(pady=(8, 2))

        self.on_submit = on_submit
        
    def submit(self):
        nombre = self.entry_nombre.get()
        saldo = self.entry_saldo.get()
        if self.on_submit:
            self.on_submit(nombre, saldo)
        self.destroy()