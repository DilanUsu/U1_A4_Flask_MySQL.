# Crea la base de datos "juegos" y la tabla "juegos" (se ejecuta UNA sola vez)
import pymysql

conexion = pymysql.connect(host='localhost', user='root', password='root')
with conexion.cursor() as cursor:
    cursor.execute("CREATE DATABASE IF NOT EXISTS juegos")
    cursor.execute("USE juegos")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS juegos(
            id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            descripcion VARCHAR(255) NOT NULL,
            precio DECIMAL(9,2) NOT NULL
        )
    """)
conexion.commit()
conexion.close()
print("Base de datos y tabla 'juegos' listas.")
