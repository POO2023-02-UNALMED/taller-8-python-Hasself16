from deportista import Deportista
from persona import Persona


class Futbolista(Persona, Deportista):
    listaFutbolistas=[]
    def __init__(self, nombre, edad, altura, sexo, años, goles, rojas, pierna):
        Persona.__init__(nombre, edad, altura, sexo)
        Deportista.__init__("Futbol", años)
        self.golesMarcados=goles
        self.tarjetasRojas=rojas
        self.piernaHabil=pierna
        Futbolista.listaFutbolistas.append(self)

    def setGolesMarcados(self, goles):
        self.golesMarcados=goles

    def getGolesMarcados(self):
        return(self.golesMarcados)
    
    def setTarjetasRojas(self, rojas):
        self.tarjetasRojas=rojas

    def getTarjetasRojas(self):
        return(self.tarjetasRojas)
    
    def setPiernaHabil(self, pierna):
        self.piernaHabil=pierna
    
    def getPiernaHabil(self):
        return(self.piernaHabil)
    
    def __str__(self):
        return (f"Mi nombre es {self.getNombre} soy profesional en el deporte de {self.getDeporte} Tengo {self.getEdad} años de edad y llevo {self.añosPracticando} años en el deporte")