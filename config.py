class Config:
    SECRET_KEY = 'password'

class DevelopmentConfig(Config):
        DEBUG = True
        MYSQL_HOST = 'localhost'
        MYSQL_USER = 'root'
        MYSQL_PASSWORD = ''
        MYSQL_DB = 'audiose'

config = {
    'development': DevelopmentConfig
}
        