from Models.PremioResponse import *
import json
import re

with open('Data/Navidad/NumerosGanadores.json', 'r') as f:
    NumerosGanadores = json.load(f)
with open('Data/Navidad/Premios.json', 'r') as f:
    Premios = json.load(f)

def coincidente(numero:str):
    for k,v in NumerosGanadores.items():
        if numero in v:
            return k
    return False
        
def aproximaciones(numero: str):
    for c in [-1,1]:
        if numero == str(int(NumerosGanadores['Gordo'])+c):
            return 'Aproximacion Gordo'
        if numero == str(int(NumerosGanadores['Segundo'])+c):
            return 'Aproximacion Segundo'
        if numero == str(int(NumerosGanadores['Tercero'])+c):
            return 'Aproximacion Tercero'
    return False

def terminaciones(numero:str):
    for n in range(1,5):
        if n<4:
            if numero[n:] == NumerosGanadores['Gordo'][n:]:
                return 'Terminacion Gordo'
            if n==3:
                if numero[n:] == NumerosGanadores['Segundo'][n:]:
                    return 'Pedrea'
                if numero[n:] == NumerosGanadores['Tercero'][n:]:
                    return 'Pedrea'
            if n==2:
                if numero[n:] == NumerosGanadores['Segundo'][n:]:
                    return 'Pedrea'
                if numero[n:] == NumerosGanadores['Tercero'][n:]:
                    return 'Pedrea'
                for cuarto in NumerosGanadores['Cuarto']:
                    if numero[n:] == cuarto[n:]:
                        return 'Pedrea'
        else:
            if numero[n:] == NumerosGanadores['Gordo'][n:]:
                return 'Reintegro'
    return False

def premio(categoria: str, apuesta: float):
    return Premios[f'{categoria}'] * apuesta

def completo(numero: str, apuesta: float = 20.0):
    res = NavidadPrize(numero=numero,
                       apuesta=apuesta)
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