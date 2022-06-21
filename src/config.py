#configuraciones para la produccion y el modo desarrollo
class Config:
    DEBUG = True
    TESTING = True

    #configuracion de la base de datos

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/practicaflaskblog"

class ProductionsConfig(Config):
    DEBUG=False

class DelvelopmentConfig(Config):
    SECRET_KEY = 'dev'
    DEBUG = True
    TESTING = True