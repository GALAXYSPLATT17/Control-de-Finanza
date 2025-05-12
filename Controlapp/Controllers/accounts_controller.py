# from ..Models.modelo_principal import modelo_principal as modelo


def obtener_cuentas():
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # Obtener todas las cuentas de la base de datos
    cuentas = [
        {"Name": "Principal", "balance": 200, "currency": "USD", "id": 1},
        {"Name": "Ahorros", "balance": 500, "currency": "USD", "id": 2},
        {"Name": "Gastos", "balance": 100, "currency": "USD", "id": 3},
        {"Name": "Inversiones", "balance": 1000, "currency": "USD", "id": 4},
        {"Name": "Tarjeta de Credito", "balance": -200, "currency": "USD", "id": 5},
        {"Name": "Tarjeta de Debito", "balance": 300, "currency": "USD", "id": 6},
        {"Name": "Efectivo", "balance": 50, "currency": "USD", "id": 7},
        {"Name": "Otros", "balance": 0, "currency": "USD", "id": 8},
    ]

    return cuentas