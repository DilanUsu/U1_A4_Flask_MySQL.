# Crea la base de datos "juegos" y la tabla "juegos" (se ejecuta UNA sola vez)
import os

import pymysql
from dotenv import load_dotenv

load_dotenv()

conexion = pymysql.connect(host=os.environ.get('DB_HOST', 'localhost'),
                           user=os.environ['DB_USER'],
                           password=os.environ['DB_PASSWORD'])
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
