from ..Models.historial_model import *

from typing import List, Dict

def obtener_transaccion() -> List[Dict]:
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # print("Obteniendo cuentas desde el controlador")
    return get_all_transaccion()

    # print("Cuentas obtenidas controller:", cuentas)
    # return cuentas
