from pydoc import text
from turtle import color
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from narwhals import col
from sqlalchemy import over
# from sqlalchemy import column
from .theme import *
from ..Controllers.accounts_controller import *
from ..Views.new_account import PopupNuevaCuenta


class VistaDashboard(ctk.CTkFrame):
    def __init__(self, master=None):
        super().__init__(master)

        self.configure(fg_color = PRIMARY_BG)
        
        if master is not None:
            master.grid_rowconfigure(0, weight=1)
            master.columnconfigure(0, weight=1)


            # Barra de menú
            menuBar = tk.Menu(master, tearoff=0)

            # Configuración del menu de la barra de menú
            menu = tk.Menu(menuBar, tearoff=0)
            menu.add_command(label="Inicio", command=self.overview)
            # menu.add_command(label="Cuentas", command=self.adminAccounts)
            menu.add_command(label="Configuración", command=self.config)
            menu.add_separator()
            # Configuración del menu de la barra de menú
            menu.add_command(label="Salir", command=master.quit)
            menuBar.add_cascade(label="Menu", menu=menu)

            menu_cuentas = tk.Menu(menuBar, tearoff=0)
            menu_cuentas.add_command(label="Ver Cuentas", command=self.adminAccounts)
            menu_cuentas.add_command(label="Agregar Cuenta", command=self.abrir_popup_nueva_cuenta)
            # menu_1.add_command(label="Configuración", command=self.config)
            # menu_1.add_separator()
           
            menuBar.add_cascade(label="Cuentas", menu=menu_cuentas)

           
            master.config(menu=menuBar)




        self.grid(row=0, column=0, sticky="nsew")


        # Menu lateral
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
        self.btn_nueva_cuenta = ctk.CTkButton(
            self.dashBody, 
            text="Nueva Cuenta", 
            command=self.abrir_popup_nueva_cuenta
        )

    def abrir_popup_nueva_cuenta(self):
        
        PopupNuevaCuenta(self)

    def lista_cuentas(self):
        self.header_title.configure(text="Cuentas")
        self.bodyTitle.configure(text="Administrar Cuentas")
        pass