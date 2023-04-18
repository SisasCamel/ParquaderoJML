from ModeloDeCarro import *

class Estacionamiento:
    def __init__(self, numeroDeZonas):
        self.numeroDeZonas = numeroDeZonas


class Zona:
    def __init__(self, height, width):
        self.grid = [[""] * width for _ in range(height)]
    
    def estaLibre(self, row, column):
        return self.grid[row][column] == ""
    
    def parquearCarro(self, row, column, Vehiculo):
        self.Vehiculo = Vehiculo
        message = str(Vehiculo.getPlacas()) + ", " + str(Vehiculo.getType())
        self.grid[row][column] = message


    def printGrid(self):
        print(self.grid)

    def set_cell(self, row, column, value):
        self.grid[row][column] = value
    
    def get_cell(self, row, column):
        return self.grid[row][column]


