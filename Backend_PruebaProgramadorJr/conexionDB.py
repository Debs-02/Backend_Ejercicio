import pyodbc


class conexionSQLServer:
    def __init__(self):
        self.conexion = None  # Inicializamos la conexión como None

    def conectar(self):
        """ Esta función establece la conexión a la base de datos """
        try:
            # Definir los parámetros de la conexión
            server = 'DEBANY\\YAM'  # Cambia por el nombre de tu servidor
            database = 'EjercicioProgramadorJr'  # Cambia por el nombre de tu base de datos
            username = 'sa'  # Cambia por tu nombre de usuario
            password = 'chocolate439'  # Cambia por tu contraseña

            # Crear la cadena de conexión
            conexion_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

            # Intentamos realizar la conexión
            self.conexion = pyodbc.connect(conexion_str)
            print("Conexión exitosa")
        except Exception as e:
            print("Error al conectar a la base de datos: ", e)

    def obtener_conexion(self):
        """ Devuelve la conexión abierta """
        return self.conexion

    def cerrar_conexion(self):
        """ Cierra la conexión con la base de datos """
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")