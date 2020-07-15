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
        print("Consumo por km: ", self.consumo)
        print("----------------------------------------")

    def hacerViaje(self,kms):
    	self.kilometraje.set(kms)

    def set_kilometros(self,kms):
    	self.kilometraje = kms

    def get_kilometros:
    	return self.kilometraje

def revise(vehiculos):
	for vehiculo in vehiculos:
		if vehiculos.get_kilometros > 10000:
			mostrar.vehiculo
