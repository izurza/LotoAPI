from fastapi import APIRouter
import re
from Navidad import NavidadFunctions as NF
router = APIRouter()

@router.get('/{numero}/')
def checkNumber(numero:str):
    if NF.validate(numero):
        return {"message" : "El numero introducido no es correcto"}
    return NF.completo(numero)

@router.get('/{numero}/{apuesta}')
def checkNumber(numero:str, apuesta:float):
    if NF.validate(numero):
        return {"message" : "El numero introducido no es correcto"}
    return NF.completo(numero, apuesta)
