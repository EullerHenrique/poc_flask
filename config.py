import os

SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
     '{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = '12345',
        servidor = 'localhost',
        porta = 3307,  
        database = 'jogoteca'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'