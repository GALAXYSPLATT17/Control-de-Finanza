from ..sqlite import get_connection

def get_usuarios():
    """
    Obtiene todos los usuarios de la base de datos.
    :return: Lista de diccionarios con los datos de los usuarios.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def insert_usuario(usuario_nombre, usuario_id, email, fecha_registro):
    """
    Inserta un nuevo usuario en la base de datos.
    :param usuario_nombre: Nombre del usuario.
    :param usuario_id: ID único del usuario.
    :param email: Correo electrónico del usuario.
    :param fecha_registro: Fecha de registro del usuario.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO usuarios (usuario_nombre, usuario_id, email, fecha_registro) VALUES (?, ?, ?, ?)",
            (usuario_nombre, usuario_id, email, fecha_registro)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al insertar el usuario: {e}")
        conn.rollback()
    finally:
        conn.close()

def update_usuario(usuario_id, usuario_nombre, email, fecha_registro):
    """
    Actualiza los datos de un usuario en la base de datos.
    :param usuario_id: ID único del usuario a actualizar.
    :param usuario_nombre: Nuevo nombre del usuario.
    :param email: Nuevo correo electrónico del usuario.
    :param fecha_registro: Nueva fecha de registro del usuario.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            UPDATE usuarios
            SET usuario_nombre = ?, email = ?, fecha_registro = ?
            WHERE usuario_id = ?
            """,
            (usuario_nombre, email, fecha_registro, usuario_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error al actualizar el usuario: {e}")
        conn.rollback()
    finally:
        conn.close()

def delete_usuario(usuario_id):
    """
    Elimina un usuario de la base de datos.
    :param usuario_id: ID único del usuario a eliminar.
    :return: None
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE usuario_id = ?", (usuario_id,))
        conn.commit()
    except Exception as e:
        print(f"Error al eliminar el usuario: {e}")
        conn.rollback()
    finally:
        conn.close()