# from ..Models.modelo_principal import modelo_principal as modelo


def obtener_cuentas():
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # Obtener todas las cuentas de la base de datos
    cuentas = [
        {"Name": "Principal", "balance": 200}
    ]

    return cuentas