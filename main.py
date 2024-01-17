from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader
from Security import Auth
import Navidad.NavidadRoutes as NavidadRoutes
import Niño.NiñoRoutes as NiñoRoutes

app = FastAPI()

@app.get('/')
def index():
    return {'message':"LotoAPI V1"}

@app.get('/secure')
async def info(api_key: APIKeyHeader = Depends(Auth.get_db_api_key)):
    return {'default variable': api_key}

app.include_router(NavidadRoutes.router)
app.include_router(NiñoRoutes.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)