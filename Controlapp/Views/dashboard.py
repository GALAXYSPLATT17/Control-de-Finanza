from pydoc import text
import customtkinter as ctk
from PIL import Image, ImageTk
from sqlalchemy import column
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


        icon_home = ctk.CTkImage(light_image=Image.open(f"{ASSETS}plugin.png"), size=ICON_SIZE_V)
        btn_home = ctk.CTkButton(menuLateralFrame, text="",image=icon_home,  fg_color="transparent", width=48, height=48, command=self.overview)
        btn_home.pack(pady=(30, 10), padx=10, fill="x")


        icon_accounts = ctk.CTkImage(light_image=Image.open(f"{ASSETS}accounts.png"), size=ICON_SIZE_H)
        btn_accounts = ctk.CTkButton(menuLateralFrame, text="", image=icon_accounts, fg_color="transparent", width=48, height=48, command=self.adminAccounts)
        btn_accounts.pack(pady=(30, 10), padx=10, fill="x")


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

                account_item = ctk.CTkFrame(self.dashBody, fg_color=ACCOUNT_1ST_ITEM, width=200, height=150)
                account_item.grid(row=1, column=index, padx=10, pady=10)

                account_balance = ctk.CTkLabel(account_item, text=f"${acc['balance']}", font=("Arial", 24, "bold"), text_color = PRIMARY_TEXT)
                account_balance.grid(row=0, column=0)

                account_name = ctk.CTkLabel(account_item, text=acc["Name"], font=("Arial", 16, "bold"), text_color = PRIMARY_TEXT)
                account_name.grid(row=1, column=0, padx=10, pady=10)
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


    def getAccounts(self):
        pass

