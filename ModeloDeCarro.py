from enum import Enum

class claseDeCarro(Enum):
    VIP = 1
    DISCAPACITADO = 2
    EMERGENCIAS = 3
    PROVEEDORES = 4
    NORMAL = 5

class Vehiculo:
    def __init__(self, placas):
        self.placas = placas
        if(not placas[0].isalpha() and not placas[1].isalpha() and not placas[2].isalpha()):
            raise ValueError('Las placas de un carro deben comenzar con 3 Letras y acabar con 3 numeros')
        if(placas[3].isalpha() and placas[4].isalpha() and placas[5].isalpha()):
            raise ValueError('Las placas de un carro deben comenzar con 3 Letras y acabar con 3 numeros')
        self.tipoDeVehiculo = claseDeCarro.NORMAL

    def getPlacas(self):
        return self.placas

    def setPlacas(self, placasAponer):
        self.placas = placasAponer

    def getType(self):
        return self.tipoDeVehiculo._name_

    def setClase(self, tipo):
        self.tipo = tipo
        match tipo:
            case 1:
                self.tipoDeVehiculo = claseDeCarro.VIP
            case 2:
                self.tipoDeVehiculo = claseDeCarro.DISCAPACITADO
            case 3:
                self.tipoDeVehiculo = claseDeCarro.EMERGENCIAS
            case 4:
                self.tipoDeVehiculo = claseDeCarro.PROVEEDORES
        