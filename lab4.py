class Nodo:
	def __init__(self,valor):
		self.next = None  #puntero al nodo siguiente
		self.prev = None  #puntero al nodo anterior
		self.valor = valor
	def get_valor(self):
		return self.valor

class ListaDoble:
	def __init__(self):
		self.head = None  #puntero al inicio de la lista
		self.tail = None  #puntero al final de la lista
		self.largo = 0

	def printL(self):
		nodo = self.head
		p = 1
		print('[',end = "")
		while nodo != None:
			if p == 1:
				print(nodo.get_valor(),end = "")
				nodo = nodo.next
				p = 2
			else:
				print (',',end = "")
				p = 1
		print(']')
		
	def rprintL(self):
		nodo = self.tail
		print('[',end = "")
		return self.rprintL_aux(nodo,2)
	def rprintL_aux(self,nodo,p):
		if nodo == None:
			print(']')
			return None
		elif p == 1:
			print (',',end = "")
			p = 2
			return self.rprintL_aux(nodo.prev,p)
		else:
			print(nodo.get_valor(),end = "")
			p = 1
			return self.rprintL_aux(nodo.prev,p)

	def appe (self, dato):
		if isinstance (dato, int):
			self.largo +=1
			if self.head == None:
				self.head = Nodo (dato)
				self.tail = self.head 
			else:
				tmp = self.tail
				ant = tmp
				tmp.next = Nodo (dato)
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
					tmp.next.next.prev = tmp
					tmp.next = tmp.next.next
					self.size -=1
					break
				else:
					tmp = tmp.next
			if not exito:
				return "Elemento no existe"

	def dela(self,valor):
		if self.head == None:
			return "Lista vacia"
		else:
			exito = False
			tmp = self.head 
			while tmp.next != None:
				if tmp.next.get_valor()== valor:
					exito = true
					tmp.next = tmp.next.next
					self.size -=1
				elif self.head.get_valor()== valor:
					self.head = self.head.next
					self.size -=1
					self.head.prev = None
				else:
					tmp = tmp.next
			if not exito:
				return "Elemento no existe"

	def findl(self,valor):
		if self.head == None:
			return "Lista vacia"
		temp = self.tail
		


