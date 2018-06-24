import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '0706520jason'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'wangye'

SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                HOST, PORT, DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False
