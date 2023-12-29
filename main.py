from fastapi import FastAPI
import Navidad.NavidadRoutes as NavidadRoutes
import Niño.NiñoRoutes as NiñoRoutes
app = FastAPI()

@app.get('/')
def index():
    return {'message':"LotoAPI V1"}

app.include_router(NavidadRoutes.router)
app.include_router(NiñoRoutes.router)