class Nodo:
	def __init__(self, valor):
		self.next = None # puntero al nodo siguiente
		self.prev = None # puntero al nodo anterior
		self.valor = valor
class ListaDoble:
	def __init__(self):
		self.head = None # puntero al inicio de la lista
		self.tail = None # puntero al final de la lista
		self.largo = 0

	def appe (self, dato):
		if isinstance (dato, int):
			self.largo +=1
			if self.head == None:
				self.head = Nodo (dato)
				self.tail = self.head
			else:
				tmp = self.tail
				ant = tmp
				tmp = tmp.next
				tmp.prev = ant 
				self.tail = tmp
		else:
			print ("Error")

	def dele(self, valor):
		if self.head == None:
			return "Lista vacia"
		elif self.head.get_valor()== valor:
			self.head = self.head.next
			self.size -=1
			self.head.prev = None
		else:
			exito = False
			tmp = self.head 
			while tmp.next != None:
				if tmp.next.get_valor()== valor:
					exito = true
					tmp.next = tmp.next.next
					self.size -=1
					break
				else:
					tmp = tmp.next
			if not exito:
				return "Elemento no existe"