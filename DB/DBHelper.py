import pyodbc
from Config.config import settings

def get_db_connection():
    connection_string = f"""
        DRIVER={{ODBC Driver 18 for SQL Server}};
        SERVER={settings.sql_server};
        DATABASE={settings.sql_database};
        TrustServerCertificate=yes;
        Trusted_connection=yes;
    """
    connection = pyodbc.connect(connection_string)
    return connection