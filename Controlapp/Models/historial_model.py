from .repositorio.transacciones_repository import *

def get_all_transaccion() -> list[dict]:
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # Obtener todas las cuentas de la base de datos
    transacciones = get_transaccion()

    # Convertir las cuentas a una lista de diccionarios
    lista_transaccion = []
    for transaccion in transacciones:
        lista_transaccion.append({
            'id': transaccion['id'],
            'cuenta_id': transaccion['cuenta_id'],
            'tipo_id': transaccion['tipo_transaccion_id'],
            'moneda_id': transaccion['moneda_id'],
            'cantidad': transaccion['cantidad'],
            'fecha': transaccion['fecha'],
            'descripcion': transaccion['descripcion'],
            'tasa_cambio': transaccion['tasa_cambio'],
        })

    return lista_transaccion

# def create_account(nombre, saldo, tipo_cuenta_id, moneda_id) -> bool:
#     """
#     Esta función crea una nueva cuenta en la base de datos.
#     :param nombre: Nombre de la cuenta.
#     :param saldo: Saldo inicial de la cuenta.
#     :param tipo_cuenta_id: ID del tipo de cuenta.
#     :param moneda_id: ID de la moneda.
#     :return: None
#     """

#     result = insert_cuenta(nombre, saldo, tipo_cuenta_id, moneda_id)

#     return result
#     # insert_cuenta(nombre, saldo, tipo_cuenta_id, moneda_id)

# def get_account_types():
#     """
#     Esta función obtiene los tipos de cuentas de la base de datos y los devuelve como una lista de diccionarios.
#     Cada diccionario contiene la información de un tipo de cuenta.
#     """
#     # Obtener los tipos de cuentas de la base de datos
#     tipos_cuentas = get_tipos_cuentas()

#     # Convertir los tipos de cuentas a una lista de diccionarios
#     lista_tipos_cuentas = []
#     for tipo in tipos_cuentas:
#         lista_tipos_cuentas.append({
#             'id': tipo['id'],
#             'nombre': tipo['nombre_tipo'],
#         })

#     return lista_tipos_cuentas
# def get_currencies():
#     """
#     Esta función obtiene las monedas de la base de datos y las devuelve como una lista de diccionarios.
#     Cada diccionario contiene la información de una moneda.
#     """
#     # Obtener las monedas de la base de datos
#     monedas = get_monedas()

#     # Convertir las monedas a una lista de diccionarios
#     lista_monedas = []
#     for moneda in monedas:
#         lista_monedas.append({
#             'id': moneda['id'],
#             'nombre': moneda['nombre_moneda'],
#             'simbolo': moneda['simbolo'],
#             'tasa': moneda['tasa_cambio'],
#         })

#     return lista_monedas