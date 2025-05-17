from ..sqlite import get_connection

def get_tipo_transaccion():
    """
    Obtiene todos los tipos de transacción de la base de datos.
    :return: Lista de diccionarios con los datos de los tipos de transacción.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipos_transacciones")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_tipo_transaccion(nombre):
    """
    Inserta un nuevo tipo de transacción en la base de datos.
    :param nombre: Nombre del tipo de trasacción.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO tipo de trasacción (nombre) VALUES (?, ?)",
            (nombre)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar tipo de transaccion: {e}")
        conn.rollback()
    finally:
        conn.close()

def update_cuenta(tipo_transaccion_id, nombre):
    """
    Actualiza los datos de un tipo de transacción en la base de datos.
    :param tipo_transaccion_id: ID del tipo de transacción a actualizar.
    :param nombre: Nuevo nombre del tipo de transacción.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE cuentas SET nombre = ? WHERE id = ?",
            (nombre, tipo_transaccion_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar el tipo de transacción: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_tipo_transaccion(tipo_transaccion_id):
    """
    Elimina un tipo de transacción de la base de datos.
    :param tipo_transaccion_id: ID del tipo de transacción a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tipos_transacciones WHERE id = ?", (tipo_transaccion_id))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar el tipo de transacción: {e}")
        conn.rollback()
    finally:
        conn.close()