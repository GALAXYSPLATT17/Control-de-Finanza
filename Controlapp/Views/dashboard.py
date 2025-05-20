from pydoc import text
from turtle import color
import customtkinter as ctk
from PIL import Image, ImageTk
from narwhals import col
# from sqlalchemy import column
from .theme import *
from ..Controllers.accounts_controller import *


class VistaDashboard(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(fg_color = PRIMARY_BG)
        
        if master is not None:
            master.grid_rowconfigure(0, weight=1)
            master.columnconfigure(0, weight=1)


        self.grid(row=0, column=0, sticky="nsew")


        # Menu
        menuLateralFrame = ctk.CTkFrame(self, fg_color = SIDEBAR_BG, width=100)
        menuLateralFrame.grid(row=0, column=0, sticky="nsew")
        menuLateralFrame.grid_propagate(False)


        # icon_home = ctk.CTkImage(light_image=Image.open(f"{ASSETS}plugin.png"), size=ICON_SIZE_V)
        btn_home = ctk.CTkButton(menuLateralFrame, text="HOME",  fg_color="transparent", width=48, height=48, command=self.overview)
        btn_home.pack(pady=(30, 10), padx=10, fill="x")


        # icon_accounts = ctk.CTkImage(light_image=Image.open(f"{ASSETS}accounts.png"), size=ICON_SIZE_H)
        btn_accounts = ctk.CTkButton(menuLateralFrame, text="CUENTAS",  fg_color="transparent", width=48, height=48, command=self.adminAccounts)
        btn_accounts.pack(pady=(30, 10), padx=10, fill="x")

        btn_settings = ctk.CTkButton(menuLateralFrame, text="Configurar",  fg_color="transparent", width=48, height=48, command=self.config)
        btn_settings.pack(pady=(30, 10), padx=10, fill="x")
        

        # Dashboard
        self.dashFrame = ctk.CTkFrame(self, fg_color = PRIMARY_BG)
        self.dashFrame.grid(row=0, column=1, sticky="nsew", padx=20, pady=30)


        # DashHeader
        self.dashHeader = ctk.CTkFrame(self.dashFrame, fg_color = PRIMARY_BG)
        self.dashHeader.grid(row=0, column=0, sticky="nsew")

        # Título
        self.header_title = ctk.CTkLabel(self.dashHeader, text="Overview", font=("Arial", 20, "bold"), text_color = PRIMARY_TEXT)
        self.header_title.grid(row=0, column=0)


        # Dashbody
        self.dashBody = ctk.CTkFrame(self.dashFrame, fg_color = PRIMARY_BG)
        self.dashBody.grid(row=1, column=0, sticky="nsew")

        self.bodyTitle = ctk.CTkLabel(self.dashBody, text="Mis Cuentas", font=("Arial", 16, "bold"), text_color = PRIMARY_TEXT)
        self.bodyTitle.grid(row=0, column=0)
        
        self.bodyTitle = ctk.CTkLabel(self.dashBody, text="Crear Cuentas", font=("Arial", 16, "bold"), text_color = SECUNDARY_TEXT)
        self.bodyTitle.grid(row=0, column=2)
        
        self.btn_nueva_cuenta = ctk.CTkButton(
        self.dashBody,
        text="Nueva Cuenta",
        command=self.abrir_popup_nueva_cuenta
        )
        self.btn_nueva_cuenta.grid(row=0, column=1, padx=10, pady=10)
        
        
        # btn_settings = ctk.CTkButton(self.dashBody, text="Crear CuentaS",  fg_color="transparent", width=48, height=48, command=self.config)
        # btn_settings.pack(pady=(30, 10), padx=10, fill="x")


        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)


        self.overview()

    def overview(self):
        self.header_title.configure(text="Overview")
        self.bodyTitle.configure(text="Mis Cuentas")

        accounts = obtener_cuentas()


        if accounts:
            print("Hay cuentas")
            for index, acc in enumerate(accounts):

                simbol = ""
                color = ""

                if acc["simbolo"] == "USD":
                    simbol = "$ "

                if acc["simbolo"] == "VES":
                    simbol = "Bs "

                if acc["simbolo"] == "EUR":
                    simbol = "€ "

                if index == 0:
                    color = "#94ffbd"
                else:
                    color = ACCOUNT_1ST_ITEM

                account_item = ctk.CTkFrame(self.dashBody, fg_color=color, width=200, height=150)
                account_item.grid(row=1, column=index, padx=10, pady=10)

                account_balance = ctk.CTkLabel(account_item, text=f"{simbol}{acc['saldo']}", font=("Arial", 24, "bold"), text_color = PRIMARY_TEXT)
                account_balance.grid(row=0, column=0, pady=30)

                account_name = ctk.CTkLabel(account_item, text=acc["nombre"], font=("Arial", 16, "bold"), text_color = PRIMARY_TEXT)
                account_name.grid(row=1, column=0, padx=10, pady=10)

                account_type = ctk.CTkLabel(account_item, text=acc["tipo_cuenta"], font=("Arial", 12), text_color = SECUNDARY_TEXT)
                account_type.grid(row=2, column=0, padx=10, pady=10)


                # account_item.grid_rowconfigure(0, weight=1)
                # account_item.grid_columnconfigure(0, weight=1)
                # account_item.grid_columnconfigure(1, weight=1)
                # account_item.grid_propagate(False)
                # account_item.configure(width=200, height=50)
                # account_item.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
                # account_item.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

                print(acc)
        else:
            pass

    def adminAccounts(self):

        self.header_title.configure(text="Cuentas")
        self.bodyTitle.configure(text="Administrar Cuentas")
        pass

    def config(self):
        self.header_title.configure(text="Configuración")
        self.bodyTitle.configure(text="Configurar")
        pass

    def getAccounts(self):
        pass
        self.btn_nueva_cuenta = ctk.CTkButton(
            self.dashBody, 
            text="Nueva Cuenta", 
            command=self.abrir_popup_nueva_cuenta
        )

    def abrir_popup_nueva_cuenta(self):
        def on_submit(nombre, saldo):
            print(f"Cuenta creada: {nombre}, Saldo inicial: {saldo}")
            # Aquí puedes agregar la lógica para guardar la cuenta

        PopupNuevaCuenta(self, on_submit=on_submit)
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
    
    
    
    # def abrir_popup_nueva_cuenta(self):
    #     def on_submit(nombre, saldo):
    #         print(f"Cuenta creada: {nombre}, Saldo inicial: {saldo}")
            
        # PopupNuevaCuenta(self.ventana, on_submit=on_submit)
    
        # btn_nueva_cuenta = ctk.CTkButton(self.ventana, text="Nueva Cuenta", command=self.abrir_popup_nueva_cuenta)
        # btn_nueva_cuenta.pack(pady=10)

