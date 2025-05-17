from ..Models.accounts_model import *

from typing import List, Dict

def obtener_cuentas() -> List[Dict]:
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    print("Obteniendo cuentas desde el controlador")
    cuentas = get_all_users_accounts()

    print("Cuentas obtenidas controller:", cuentas)
    return cuentas