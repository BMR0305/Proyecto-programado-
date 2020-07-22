#Clase Nodo:
#Atributos:
	#next: referencia al siguiente nodo
	#prev: referencia al nodo anterio
	#valor: valor contenido en el nodo
#Metodos:
	#get.valor(): obtiene el valor de la instancia
class Nodo:
	def __init__(self,valor):
		self.next = None  #puntero al nodo siguiente
		self.prev = None  #puntero al nodo anterior
		self.valor = valor
	def get_valor(self):
		return self.valor
#Clase ListaDoble
#Atributos:
	#head: referencia al primer nodo de la lista
	#prev: referencia al ultimo nodo de la lista
	#size: contiene el largo de la lista
#Metodos:
	#printL(): enseña la lista en consola
	#rprintL(): enseña la lista alrevez en consola
	#appe(): añade un nodo a la lista con el valor dado
		#E: numero #S:añade un nodo a la lista #R:numero debe ser entero
	#dele(): elimina el primer elemento de la lista igual al valor dado
		#E: numero #S:lista con el nodo igual al valor eliminado #R:-
	#dela(): elimina todos los elementos de la lista igual al valor dado
		#E: numero #S:lista con los nodos igual al valor eliminados #R:-
	#findl(): dice en que posicion de la lista se encuentra el valor dado
		#E: numero #S:posicion en la lista del nodo #R:-
	#ins(): inserta un nodo antes de otro nodo que el valor del mismo sea igual a el segundo numero dado
		#E 2 numeros #S primer numero insertado como nodo antes del primer nodo con el segundo valor #R-
class ListaDoble:
	def __init__(self):
		self.head = None  #puntero al inicio de la lista
		self.tail = None  #puntero al final de la lista
		self.size = 0

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
			return self.rprintL_aux(nodo,p)
		else:
			print(nodo.get_valor(),end = "")
			p = 1
			return self.rprintL_aux(nodo.prev,p)

	def appe (self, dato):
		if isinstance (dato, int):
			self.size +=1
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
				if self.tail.get_valor()== valor and tmp.next.get_valor()== valor:
					self.tail = self.tail.prev
					self.size -=1
					self.tail.next = None
					exito = True
					break
				elif tmp.next.get_valor()== valor:
					exito = True
					tmp.next.next.prev = tmp
					tmp.next = tmp.next.next
					self.size -=1
					exito = True
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
				if self.tail.get_valor()== valor and tmp.next.get_valor()== valor:
					self.tail = self.tail.prev
					self.size -=1
					self.tail.next = None
					exito = True
				elif tmp.next.get_valor()== valor:
					exito = True
					tmp.next.next.prev = tmp
					tmp.next = tmp.next.next
					self.size -=1
					exito = True
				elif self.head.get_valor()== valor:
					self.head = self.head.next
					self.size -=1
					self.head.prev = None
					exito = True
				else:
					tmp = tmp.next
			if not exito:
				return "Elemento no existe"

	def findl(self,valor):
		if self.head == None:
			return "Lista vacia"
		temp = self.tail
		find = False
		n = self.size
		i = 0
		while temp != None:
			if temp.get_valor() == valor:
				find = True
				i += 1
				break
			else:
				temp = temp.prev
				i += 1
		n-=1
		i-=1
		final = abs(n-i)
		if find == True:
			return final
		else:
			return "No se encontro el valor"
			
	def ins(self,valor1, valor2):
		if self.head == None:
			return "Lista vacia"
		elif isinstance (valor1, int):
			self.size +=1
			if self.head.get_valor() == valor2:
				tmp = self.head
				self.head = Nodo(valor1)
				self.head.next = tmp  
			else:
				exito = False
				tmp = self.head 
				while tmp.next != None:
					if tmp.next.get_valor()== valor2:
						exito = True
						sig = tmp.next
						tmp.next = Nodo(valor1)
						tmp.next.prev = tmp
						tmp.next.next = sig
						sig.prev = tmp.next 
						self.size +=1
						break
					else:
						tmp = tmp.next
				if not exito:
					return "Elemento no existe"


