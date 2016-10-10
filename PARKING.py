archivo = open("parking", "w")

class Parking:
    nombre = ""
    coches = []
    def agregar(self, coche ):
        self.coches.append(coche)
    def __init__(self, nombre, coches):
        self.nombre = nombre
        self.coches = coches


class Coche:
    marca = ""
    modelo = ""
    placas = ""
    color = ""
    entrada = ""
    hora = ""
    def __init__ (self, marca = "", modelo = "", tipo = "", placas = "", color = "", entrada = "", hora= ""):
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.placas = placas
        self.color = color
        self.entrada = entrada
        self.hora = hora

print "Parking Management System"
print "Buen Dia"

entrada = raw_input("Presiona 1 para agregar un coche: ")
print entrada

if entrada == "1":
    coche = Coche()
    coche.marca = raw_input("Ingresar marca = ")
    coche.modelo = raw_input("Ingresar modelo = ")
    coche.tipo = raw_input("ingresar tipo = ")
    coche.placas = raw_input("Ingresar placas = ")
    coche.color = raw_input("Ingresar color = ")
    coche.entrada = raw_input("Fecha de Entrada = ")
    coche.hora = raw_input("Hora")
    print (coche)
else:
    print "No hay opcion para el numero indicado"


