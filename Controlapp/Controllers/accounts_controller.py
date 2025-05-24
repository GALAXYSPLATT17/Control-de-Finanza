from ..Models.accounts_model import *

from typing import List, Dict

def obtener_cuentas() -> List[Dict]:
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # print("Obteniendo cuentas desde el controlador")
    return get_all_users_accounts()

    # print("Cuentas obtenidas controller:", cuentas)
    # return cuentas

def crear_cuenta(nombre: str, saldo: float, tipo_cuenta_id: int, moneda_id: int):
    """
    Esta función crea una nueva cuenta en la base de datos.
    :param nombre: Nombre de la cuenta.
    :param saldo: Saldo inicial de la cuenta.
    :param tipo_cuenta_id: ID del tipo de cuenta.
    :param moneda_id: ID de la moneda.
    :return: Mensaje.
    """
    # print("Creando cuenta desde el controlador")

    mensaje = ""

    result = create_account(nombre, saldo, tipo_cuenta_id, moneda_id)
    if result:
        mensaje = "Cuenta creada con éxito"
        print("Cuenta creada con éxito")
    else:
        mensaje = "Error al crear la cuenta"
        print("Error al crear la cuenta")


    return mensaje, result




def obtener_tipos_cuentas() -> List[Dict]:
    """
    Esta función obtiene los tipos de cuentas de la base de datos y los devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de un tipo de cuenta.
    """
    # print("Obteniendo tipos de cuentas desde el controlador")
    return get_account_types()

def obtener_monedas() -> List[Dict]:
    """
    Esta función obtiene las monedas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una moneda.
    """
    # print("Obteniendo monedas desde el controlador")
    return get_currencies()