class Prize:
    def __init__(self, numero:str = '00000', estado:str = 'No Premiado', premio:float = 0.0):
        self.numero = numero
        self.estado = estado
        self.premio = premio
    
class NavidadPrize(Prize):
    def __init__(self, numero:str = '00000', apuesta:float = 20.0, estado:str = 'No Premiado', premio:float = 0.0):
        super().__init__(numero, estado, premio)
        self.apuesta = apuesta
