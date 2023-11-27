from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.version_info = (1,4, 6,'final',0)
pymysql.install_as_MySQLdb()

# inicializacion db sqlachemi
db = SQLAlchemy()