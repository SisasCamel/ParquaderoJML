from ModeloDeCarro import *
from Parqueadero import Estacionamiento, Zona

myCarro = Vehiculo("CAS123")
myCarro.setClase(1)

zonaA = Zona(2, 15)

zonaA.printGrid()

zonaA.parquearCarro(1, 5, myCarro)

zonaA.printGrid()

