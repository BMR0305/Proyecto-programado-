class Vehiculo:
    def __init__(self, placa, marca, cantidad_ruedas,kilometraje,combustible,consumo):
        self.placa = placa
        self.marca = marca
        self.cantidad_ruedas = cantidad_ruedas
        self.kilometraje = kilometraje
        self.combustible = combustible
        self.consumo = consumo

    def mostrar(self):
        print("Placa: ", self.placa)
        print("Marca: ", self.marca)
        print("Cantidad de ruedas: ", self.cantidad_ruedas)
        print("Kilometraje: ", self.kilometraje)
        print("Combustible: ", self.combustible)
        print("Consumo por km: ", self.consumo, "litros")

    def hacerViaje(self,kms):
    	self.kilometraje.set(kms)

    def set_kilometros(self,kms):
    	self.kilometraje = kms

    def get_kilometros(self):
    	return self.kilometraje
    
    def get_marca(self):
        return self.marca

class Auto(Vehiculo):
    def __init__(self, placa, marca, cantidad_ruedas, kilometraje, combustible, consumo, modelo, año):
        Vehiculo.__init__(self, placa, marca, cantidad_ruedas, kilometraje, combustible, consumo)
        self.modelo = modelo
        self.año = año
    def mostrar(self):
        Vehiculo.mostrar(self)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)
        print("------------------------------")

class Moto(Vehiculo):
    def __init__(self, placa, marca, cantidad_ruedas, kilometraje, combustible, consumo, estilo, cilindraje):
        Vehiculo.__init__(self, placa, marca, cantidad_ruedas, kilometraje, combustible, consumo)
        self.estilo = estilo
        self.cilindraje = cilindraje
    def mostrar(self):
        Vehiculo.mostrar(self)
        print("Estilo: ", self.estilo)
        print("Cilindraje: ", self.cilindraje, "cm³")
        print("------------------------------")

vehiculos = [Auto("1234", "BMW", 4, 11000, "Gasolina", 500, "Serie 2", 2017), Auto("1334", "BMW", 4, 1000, "Gasolina", 700, "R8", 2020), Auto("1256", "Toyota", 4, 15000, "Gasolina", 400, "Corolla", 2018), Auto("7834", "Toyota", 4, 6000, "Diesel", 800, "Hilux", 2020),
             Moto("5876", "Kawasiki", 2, 20000, "Gasolina", 400, "Z1000", 1.043), Moto("1242", "Kawasaki", 2, 12000, "Gasolina", 600, "KX250", 249), Moto("1487", "Honda", 2, 12000, "Gasolina", 300, "CB 190 R", 184.40), Moto("5292", "Suzuki", 2, 18000, "Gasolina", 350, "EN-125 2A", 125)] 


def revise(lista):
    for vehiculo in vehiculos:
        if vehiculo.get_kilometros() > 10000:
            vehiculo.mostrar()

def busque(lista,marca):
    for vehiculo in vehiculos:
        if vehiculo.get_marca() == marca:
            vehiculo.mostrar() 
