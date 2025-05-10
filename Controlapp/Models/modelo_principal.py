import repositorio.cuentas_repository as cuentas_repo


def obtener_cuentas():
    """
    Esta función obtiene las cuentas de la base de datos y las devuelve como una lista de diccionarios.
    Cada diccionario contiene la información de una cuenta.
    """
    # Obtener todas las cuentas de la base de datos
    cuentas = cuentas_repo.get_cuentas()

    # Convertir las cuentas a una lista de diccionarios
    lista_cuentas = []
    for cuenta in cuentas:
        lista_cuentas.append({
            'id': cuenta.id,
            'nombre': cuenta.nombre,
            'saldo': cuenta.saldo,
            'tipo_id': cuenta.tipo_cuenta_id,
            'id_usuario': cuenta.usuario_id
        })

    return lista_cuentas