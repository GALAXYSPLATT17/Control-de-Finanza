from ..sqlite import get_connection

def get_tipo_cuentas():
    """
    Obtiene todas los tipos de cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de los tipos de cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tipo_cuentas")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_tipo_cuenta(nombre):
    """
    Inserta un nuevo tipo de cuenta en la base de datos.
    :param nombre: Nombre del tipo de cuenta.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO tipo_cuentas (nombre) VALUES (?, ?)",
            (nombre)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar el tipo de cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()

def update_cuenta(tipo_cuenta_id, nombre):
    """
    Actualiza los datos de un tipo de cuenta en la base de datos.
    :param tipo_cuenta_id: ID del tipo de cuenta a actualizar.
    :param nombre: Nuevo nombre del tipo de cuenta.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE tipo de cuentas SET nombre = ? WHERE id = ?",
            (nombre, tipo_cuenta_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar tipo de cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_tipo_cuenta(tipo_cuenta_id):
    """
    Elimina un tipo de cuenta de la base de datos.
    :param tipo_cuenta_id: ID del tipo de cuenta a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM tipo_cuentas WHERE id = ?", (tipo_cuenta_id))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar el tipo de cuenta: {e}")
        conn.rollback()
    finally:
        conn.close()