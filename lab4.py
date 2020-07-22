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
		return self.rprintL_aux(nodo,1)
	def rprintL_aux(self,nodo,p):
		if nodo == None:
			print(']')
			return None
		elif p == 1:
			print (',',end = "")
			p = 2
		else:
			print(nodo.get_valor(),end = "")
			p = 1
			return self.rprintL_aux(nodo.prev,p)
