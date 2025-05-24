from ..sqlite import get_connection

def get_cuentas():
    """
    Obtiene todas las cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de las cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cuentas c JOIN monedas m ON c.moneda_id = m.id JOIN tipos_cuentas t ON c.tipo_cuenta_id = t.id")
    cuentas = cursor.fetchall()
    conn.close()

    print("Cuentas obtenidas:", cuentas)

    return [dict(row) for row in cuentas]

def insert_cuenta(nombre, saldo, id_tipo_cuenta, id_moneda): 
    """
    Inserta una nueva cuenta en la base de datos.
    :param nombre: Nombre de la cuenta.
    :param saldo_inicial: Saldo inicial de la cuenta.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO cuentas (nombre_cuenta, saldo, tipo_cuenta_id, moneda_id, usuario_id) VALUES (?, ?, ?, ?, ?)",
            (nombre, saldo, id_tipo_cuenta, id_moneda, 1)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al insertar la cuenta: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def update_cuenta(cuenta_id, nombre, saldo):
    """
    Actualiza los datos de una cuenta en la base de datos.
    :param cuenta_id: ID de la cuenta a actualizar.
    :param nombre: Nuevo nombre de la cuenta.
    :param saldo: Nuevo saldo de la cuenta.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE cuentas SET nombre = ?, saldo_inicial = ? WHERE id = ?",
            (nombre, saldo, cuenta_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar la cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_cuenta(cuenta_id):
    """
    Elimina una cuenta de la base de datos.
    :param cuenta_id: ID de la cuenta a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM cuentas WHERE id = ?", (cuenta_id))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar la cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()

def get_tipos_cuentas():
    """
    Obtiene todos los tipos de cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de los tipos de cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipos_cuentas")
    tipos_cuentas = cursor.fetchall()
    conn.close()

    return [dict(row) for row in tipos_cuentas]

def get_monedas():
    """
    Obtiene todas las monedas de la base de datos.
    :return: Lista de diccionarios con los datos de las monedas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monedas")
    monedas = cursor.fetchall()
    conn.close()

    return [dict(row) for row in monedas]