from Models.ErrorResponse import *
from Models.PremioResponse import * 
import json
import re
from datetime import datetime, date

with open('Data/Niño/NumerosGanadores.json', 'r') as f:
    NumerosGanadores = json.load(f)
with open('Data/Niño/Premios.json', 'r') as f:
    Premios = json.load(f)

def coincidente(numero:str):
    for k,v in NumerosGanadores.items():
        if k in ['Primero','Segundo','Tercero']:
            if numero in v:
                return k
    return False
        
def aproximaciones(numero: str):
    for c in [-1,1]:
        try:
            if numero == str(int(NumerosGanadores['Primero'])+c):
                return 'Aproximacion Primero'
            if numero == str(int(NumerosGanadores['Segundo'])+c):
                return 'Aproximacion Segundo'
        except:
            return False
    return False

def terminaciones(numero:str):
    for n in range(1,5):
        if n==1:
            if numero[n:] in NumerosGanadores['Extraccion 4']:
                return 'Extraccion 4'
        if n==2:
            if numero[n:] in NumerosGanadores['Extraccion 3']:
                return 'Extraccion 3'
        if n==3:
            if numero[n:] in NumerosGanadores['Extraccion 2']:
                return 'Extraccion 2'
        else:
            try:
                if numero[n:] == NumerosGanadores['Primero'][n:]:
                    return 'Reintegro'
                if numero[n:] in NumerosGanadores['Extraccion 1']:
                    return 'Reintegro'
            except:
                return False
    return False

def premio(categoria: str, apuesta: float):
    return Premios[f'{categoria}'] * apuesta

def completo(numero: str, apuesta: float = 20.0):
    res = Prize(numero=numero)
    loto = coincidente(numero)
    if loto:
        res.estado = 'Premiado'
        res.premio = premio(loto,apuesta)
        return res
    loto = aproximaciones(numero)
    if loto:
        res.estado = 'Premiado'
        res.premio = premio(loto,apuesta)
        return res
    loto = terminaciones(numero)
    if loto:
        res.estado = 'Premiado'
        res.premio = premio(loto,apuesta)
    return res

def validate(numero:str):
    return re.search('\d{5}',numero) is None

def estado():
    res = ErrorResponse(success=False)
    if (datetime.now().date() < date(2024,1,6)):
        res.message = "El sorteo no ha sucedido todavia"
        return res
    res.success = True
    res.message = "Activo"
    return res
    # for k,v in NumerosGanadores.items():
    #     if k == ["Primero","Segundo","Tercero"]:
    #         if len(v)<1:
    #             return ""
    #     if k == "Extraccion 4":
    #         print(len(v))
    #     if k == "Extraccion 3":
    #         print(len(v))
    #     if k == "Extraccion 2":
    #         print(len(v))
    #     if k == "Extraccion 1":
    #         print(len(v))

