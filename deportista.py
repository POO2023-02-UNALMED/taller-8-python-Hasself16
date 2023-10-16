class Deportista():
    def __init__(self, deporte, años):
        self.deporte=deporte
        self.añosPracticando=años
    
    def setDeporte(self, deporte):
        self.deporte=deporte

    def getDeporte(self):
        return(self.deporte)
    
    def setAñosPracticando(self, años):
        self.añosPracticando=años

    def getAñosPracticando(self):
        return(self.añosPracticando)