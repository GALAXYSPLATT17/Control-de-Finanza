from ..sqlite import get_connection

def get_cuentas():
    """
    Obtiene todas las cuentas de la base de datos.
    :return: Lista de diccionarios con los datos de las cuentas.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cuentas")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]