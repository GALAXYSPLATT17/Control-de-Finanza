from ..sqlite import get_connection

def get_transaccion():
    """
    Obtiene todas las transacciones de la base de datos.
    :return: Lista de diccionarios con los datos de las transacciones.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transacciones")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_transaccion(cantidad, descripcion, fecha):
    """
    Inserta una nueva transacción en la base de datos.
    :param cantidad: La cantidad de la transacción.
    :param descripcion: Descripción de la transacción.
    :param fecha: Fecha de la transacción.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO transacciones (cantidad, descripcion, fecha) VALUES (?, ?, ?, ?)",
            (cantidad, descripcion, fecha)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar la transacción: {e}")
        conn.rollback()
    finally:
        conn.close()

def update_transaccion(cantidad, descripcion, fecha):
    """
    Actualiza los datos de una transacción en la base de datos.
    :param cantidad: Nueva cantidad de la transacción.
    :param descripcion: Nueva descripción de la transacción.
    :param fecha: Nueva fecha de la transacción.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE transacciones
            SET cuenta_id = ?, monto = ?, descripcion = ?, fecha = ?
            WHERE id = ?
            """,
            (cantidad, descripcion, fecha)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar la transacción: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_transaccion(transaccion_id):
    """
    Elimina una transacción de la base de datos.
    :param transaccion_id: ID de la transacción a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM transacciones WHERE id = ?", (transaccion_id,))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar la transacción: {e}")
        conn.rollback()
    finally:
        conn.close()