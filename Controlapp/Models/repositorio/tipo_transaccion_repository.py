from ..sqlite import get_connection

def get_tipo_transaccion():
    """
    Obtiene todas las cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de las cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipo_transaccion")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_tipo_transaccion(nombre):
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
            "INSERT INTO cuentas (nombre) VALUES (?, ?)",
            (nombre)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar tipo de transaccion: {e}")
        conn.rollback()

def update_cuenta(tipo_transaccion_id, nombre):
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
            (nombre, tipo_transaccion_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar la cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_tipo_transaccion(tipo_transaccion_id):
    """
    Elimina una cuenta de la base de datos.
    :param cuenta_id: ID de la cuenta a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tipos_transacciones WHERE id = ?", (tipo_transaccion_id))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar el tipo de transaccion: {e}")
        conn.rollback()
    finally:
        conn.close()