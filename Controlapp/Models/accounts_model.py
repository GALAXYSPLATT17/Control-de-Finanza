from .repositorio.cuentas_repository import *


def get_all_users_accounts():
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # Obtener todas las cuentas de la base de datos
    cuentas = get_cuentas()

    # Convertir las cuentas a una lista de diccionarios
    lista_cuentas = []
    for cuenta in cuentas:
        lista_cuentas.append({
            'id': cuenta['id'],
            'nombre': cuenta['nombre_cuenta'],
            'saldo': cuenta['saldo'],
            'tipo_id': cuenta['tipo_cuenta_id'],
            'id_usuario': cuenta['usuario_id'],
            'tipo_cuenta': cuenta['nombre_tipo'],
            'moneda': cuenta['nombre_moneda'],
            'simbolo': cuenta['simbolo'],
        })

    return lista_cuentas

def create_account(nombre, saldo, tipo_cuenta_id, moneda_id):
    """
    Esta función crea una nueva cuenta en la base de datos.
    :param nombre: Nombre de la cuenta.
    :param saldo: Saldo inicial de la cuenta.
    :param tipo_cuenta_id: ID del tipo de cuenta.
    :param moneda_id: ID de la moneda.
    :return: None
    """
    # insert_cuenta(nombre, saldo, tipo_cuenta_id, moneda_id)