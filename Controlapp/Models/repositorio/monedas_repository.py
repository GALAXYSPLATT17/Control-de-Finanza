from ..sqlite import get_connection

def get_monedas():
    """
    Obtiene todas las cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de las cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM monedas")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_monedas(nombre, simbolo):
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
            "INSERT INTO monedas (monedas_id, nombre, simbolo) VALUES (?, ?)",
            (nombre, simbolo)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar la moneda: {e}")
        conn.rollback()
    finally:
        conn.close()    

def update_monedas(moneda_id, nombre, simbolo):
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
            (moneda_id, nombre, simbolo)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar la moneda: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_monedas(monedas_id):
    """
    Elimina una cuenta de la base de datos.
    :param cuenta_id: ID de la cuenta a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM monedas WHERE id = ?", (monedas_id))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar la moneda: {e}")
        conn.rollback()
    finally:
        conn.close()