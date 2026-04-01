import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'user')    # если переменные окружения не определены в файле .env, то значения через запятую применяются по умолчанию
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', 1234)
    HOST = os.environ.get('POSTGRES_HOST', '127.0.0.1')
    PORT = os.environ.get('POSTGRES_PORT, 5532')
    DB = os.environ.get('POSTGRES_DB', 'mydb')
    
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = os.environ.get("SECRET_KEY", "1111") 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
