from fastapi import APIRouter
import re
from Niño import NiñoFunctions as NF
router = APIRouter(
    prefix="/Niño",
    tags=["niño"]
)

@router.get('/{numero}/')
def checkNumber1(numero:str):
    if NF.validate(numero):
        return {"message" : "El numero introducido no es correcto"}
    return NF.completo(numero)

@router.get('/estado')
def estado():
    return {"message" : NF.estado()}