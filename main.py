from fastapi import FastAPI
import Navidad.NavidadRoutes as NavidadRoutes
app = FastAPI()

@app.get('/')
def index():
    return {'message':"LotoAPI V1"}

app.include_router(NavidadRoutes.router)