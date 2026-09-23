import pymysql

# Cambia la contraseña por la de tu usuario root de MySQL
def obtener_conexion():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db='juegos')
