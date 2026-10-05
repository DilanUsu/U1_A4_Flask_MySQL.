import os

import pymysql
from dotenv import load_dotenv

# Carga las variables del archivo .env (que NO se sube a Git)
load_dotenv()


def obtener_conexion():
    return pymysql.connect(host=os.environ.get('DB_HOST', 'localhost'),
                           user=os.environ['DB_USER'],
                           password=os.environ['DB_PASSWORD'],
                           db=os.environ.get('DB_NAME', 'juegos'))
