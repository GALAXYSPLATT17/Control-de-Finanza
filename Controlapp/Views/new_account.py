from doctest import master
from unittest import result
import customtkinter as ctk
from ..Controllers.accounts_controller import *


class PopupNuevaCuenta(ctk.CTkToplevel):
    def __init__(self, master, dashboard):
        super().__init__(master)

        self.dashboard = dashboard

        self.title("Nueva Cuenta Bancaria")
        self.geometry("350x400")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="Nombre de la cuenta:").pack(pady=(8, 2))
        self.entry_nombre = ctk.CTkEntry(self)
        self.entry_nombre.pack(pady=2)

        ctk.CTkLabel(self, text="Saldo inicial:").pack(pady=2)
        self.entry_saldo = ctk.CTkEntry(self)
        self.entry_saldo.pack(pady=2)

        ctk.CTkLabel(self, text="Tipo de cuenta:").pack(pady=2)
        tipos_cuentas = obtener_tipos_cuentas()
        tipos_cuentas_List = [tipo['nombre'] for tipo in tipos_cuentas]
        self.entry_tipo = ctk.CTkOptionMenu(self, values=tipos_cuentas_List)
        self.entry_tipo.pack(pady=2)


        ctk.CTkLabel(self, text="Moneda:").pack(pady=2)
        monedas = obtener_monedas()
        monedas_list = [moneda['nombre'] for moneda in monedas]
        self.entry_moneda = ctk.CTkOptionMenu(self, values=monedas_list)
        self.entry_moneda.pack(pady=2)


        self.btn_crear = ctk.CTkButton(self, text="Crear", command=lambda: self.submit(tipos_cuentas, monedas))
        self.btn_crear.pack(pady=(8, 2))
        
        self.resultado = ctk.CTkLabel(self, text="")
        self.resultado.pack(pady=20)
        
    def submit(self, tipos_cuentas, monedas):
        
        nombre = self.entry_nombre.get()
        saldo_str = self.entry_saldo.get()
        tipo_nombre = self.entry_tipo.get()
        moneda_nombre = self.entry_moneda.get()

        if not saldo_str:
            self.resultado.configure(text="Error: Ingresa un saldo válido.")
            return

        try:
            saldo = float(saldo_str)
        except ValueError:
            self.resultado.configure(text="Error: Ingresa un saldo numérico.")
            return
       
        tipo_id = next((int(tipo['id']) for tipo in tipos_cuentas if tipo['nombre'] == tipo_nombre), None)
        moneda_id = next((int(moneda['id']) for moneda in monedas if moneda['nombre'] == moneda_nombre), None)

        if tipo_id is None or moneda_id is None:
            self.resultado.configure(text="Error: Selecciona un tipo de cuenta y moneda válidos.")
            return
       
        msg, result = crear_cuenta(nombre, saldo, tipo_id, moneda_id)

        self.resultado.configure(text=msg)
        
        if result:
            self.dashboard.overview()
            self.after(2000, self.destroy)

        
        