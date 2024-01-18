import mysql.connector

class DatabaseManager:
    # Inicialización de la clase. Se establece la conexión a la base de datos y se crea un cursor para las consultas.
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    # Método para obtener las preguntas de la base de datos.
    def get_questions(self, level):
        query = "SELECT * FROM Preguntas WHERE nivel = %s"
        self.cursor.execute(query, (level,))
        return self.cursor.fetchall() 
        
    def close_connection(self):
        self.connection.close()