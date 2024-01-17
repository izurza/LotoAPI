from fastapi import Security, HTTPException
from fastapi.security import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN
from Config.config import settings
from DB.DBHelper import get_db_connection

api_key = APIKeyHeader(name="access_token", auto_error=False)

def get_API_key(api_key: str = Security(api_key)) -> str:

    if api_key == settings.API_KEY:
        return api_key
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )

def get_db_api_key(api_key: str = Security(api_key)) -> str:

    #connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={settings.sql_server};DATABASE={settings.sql_database};UID={settings.sql_user};PWD={settings.sql_password};TrustServerCertificate=yes;Trusted_connection=no'
    with get_db_connection().cursor() as cursor:
        cursor.execute('select llave from apikeys where llave=? and isactive=1;'
                       , api_key)
        row = cursor.fetchone()
        if  row != None : return row[0]
        raise HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
    )
    