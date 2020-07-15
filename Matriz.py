import pygame, sys, random ,time, os 
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
#Pantalla
size = (720,800)
pygame.display.set_caption("Avatars vs Rooks")
screen = pygame.display.set_mode(size)
#Reloj
clock=pygame.time.Clock()
#Fuente
font = pygame.font.Font(None, 60)
#Variables de monedas
monedas = 1000
#Fondos
matriz1 = pygame.image.load("Imagenes/Matriz1.jpg").convert()
matriz2 = pygame.image.load("Imagenes/Matriz2.jpg").convert()
matriz3 = pygame.image.load("Imagenes/Matriz3.jpg").convert()
ganador = pygame.image.load("Imagenes/Ganaste.jpg").convert()
perdedor = pygame.image.load("Imagenes/Game over.jpg").convert()
negro = pygame.image.load("Imagenes/Negro.jpg").convert()
#Boton
volver = pygame.image.load("Imagenes/Volver.png")
volver.set_colorkey([0,0,0])
#Imagenes del arquero
ataque0a = pygame.image.load("Imagenes/Arquero/Ataque0.png").convert()
ataque0a.set_colorkey([0,0,0])
ataque1a = pygame.image.load("Imagenes/Arquero/Ataque1.png").convert()
ataque1a.set_colorkey([0,0,0])
ataque2a = pygame.image.load("Imagenes/Arquero/Ataque2.png").convert()
ataque2a.set_colorkey([0,0,0])
ataque3a = pygame.image.load("Imagenes/Arquero/Ataque3.png").convert()
ataque3a.set_colorkey([0,0,0])
ataque4a = pygame.image.load("Imagenes/Arquero/Ataque4.png").convert()
ataque4a.set_colorkey([0,0,0])
ataque5a = pygame.image.load("Imagenes/Arquero/Ataque5.png").convert()
ataque5a.set_colorkey([0,0,0])
ataque6a = pygame.image.load("Imagenes/Arquero/Ataque6.png").convert()
ataque6a.set_colorkey([0,0,0])
ataque7a = pygame.image.load("Imagenes/Arquero/Ataque7.png").convert()
ataque7a.set_colorkey([0,0,0])
caminar1a = pygame.image.load("Imagenes/Arquero/Caminar1.png").convert()
caminar1a.set_colorkey([0,0,0])
caminar2a = pygame.image.load("Imagenes/Arquero/Caminar2.png").convert()
caminar2a.set_colorkey([0,0,0])
caminar3a = pygame.image.load("Imagenes/Arquero/Caminar3.png").convert()
caminar3a.set_colorkey([0,0,0])
caminar4a = pygame.image.load("Imagenes/Arquero/Caminar4.png").convert()
caminar4a.set_colorkey([0,0,0])
caminar5a = pygame.image.load("Imagenes/Arquero/Caminar5.png").convert()
caminar5a.set_colorkey([0,0,0])
caminar6a = pygame.image.load("Imagenes/Arquero/Caminar6.png").convert()
caminar6a.set_colorkey([0,0,0])
caminar7a = pygame.image.load("Imagenes/Arquero/Caminar7.png").convert()
caminar7a.set_colorkey([0,0,0])
dañoa = pygame.image.load("Imagenes/Arquero/Daño.png").convert()
dañoa.set_colorkey([0,0,0])
muertea = pygame.image.load("Imagenes/Arquero/Muerte.png").convert()
muertea.set_colorkey([0,0,0])
#Proyectil arquero
flecha = pygame.image.load("Imagenes/Arquero/Flecha.png").convert()
flecha.set_colorkey([0,0,0])
#Sonido de proyectil
sonidoFlecha = pygame.mixer.Sound("Sonidos/Impacto flecha.wav")
#Imagenes del escudero
ataque0e = pygame.image.load("Imagenes/Escudero/Ataque0.png").convert()
ataque0e.set_colorkey([0,0,0])
ataque1e = pygame.image.load("Imagenes/Escudero/Ataque1.png").convert()
ataque1e.set_colorkey([0,0,0])
ataque2e = pygame.image.load("Imagenes/Escudero/Ataque2.png").convert()
ataque2e.set_colorkey([0,0,0])
ataque3e = pygame.image.load("Imagenes/Escudero/Ataque3.png").convert()
ataque3e.set_colorkey([0,0,0])
ataque4e = pygame.image.load("Imagenes/Escudero/Ataque4.png").convert()
ataque4e.set_colorkey([0,0,0])
ataque5e = pygame.image.load("Imagenes/Escudero/Ataque5.png").convert()
ataque5e.set_colorkey([0,0,0])
ataque6e = pygame.image.load("Imagenes/Escudero/Ataque6.png").convert()
ataque6e.set_colorkey([0,0,0])
ataque7e = pygame.image.load("Imagenes/Escudero/Ataque7.png").convert()
ataque7e.set_colorkey([0,0,0])
caminar1e = pygame.image.load("Imagenes/Escudero/Caminar1.png").convert()
caminar1e.set_colorkey([0,0,0])
caminar2e = pygame.image.load("Imagenes/Escudero/Caminar2.png").convert()
caminar2e.set_colorkey([0,0,0])
caminar3e = pygame.image.load("Imagenes/Escudero/Caminar3.png").convert()
caminar3e.set_colorkey([0,0,0])
caminar4e = pygame.image.load("Imagenes/Escudero/Caminar4.png").convert()
caminar4e.set_colorkey([0,0,0])
caminar5e = pygame.image.load("Imagenes/Escudero/Caminar5.png").convert()
caminar5e.set_colorkey([0,0,0])
caminar6e = pygame.image.load("Imagenes/Escudero/Caminar6.png").convert()
caminar6e.set_colorkey([0,0,0])
caminar7e = pygame.image.load("Imagenes/Escudero/Caminar7.png").convert()
caminar7e.set_colorkey([0,0,0])
dañoe = pygame.image.load("Imagenes/Escudero/Daño.png").convert()
dañoe.set_colorkey([0,0,0])
muertee = pygame.image.load("Imagenes/Escudero/Muerte.png").convert()
muertee.set_colorkey([0,0,0])
#Proyectil escudero
espada = pygame.image.load("Imagenes/Escudero/Espada.png").convert()
espada.set_colorkey([0,0,0])
#Sonido de proyectil
sonidoEspada = pygame.mixer.Sound("Sonidos/Impacto espada.wav")

#Imagenes del hachero
ataque0h = pygame.image.load("Imagenes/Hacha/Ataque0.png").convert()
ataque0h.set_colorkey([0,0,0])
ataque1h = pygame.image.load("Imagenes/Hacha/Ataque1.png").convert()
ataque1h.set_colorkey([0,0,0])
ataque2h = pygame.image.load("Imagenes/Hacha/Ataque2.png").convert()
ataque2h.set_colorkey([0,0,0])
ataque3h = pygame.image.load("Imagenes/Hacha/Ataque3.png").convert()
ataque3h.set_colorkey([0,0,0])
ataque4h = pygame.image.load("Imagenes/Hacha/Ataque4.png").convert()
ataque4h.set_colorkey([0,0,0])
ataque5h = pygame.image.load("Imagenes/Hacha/Ataque5.png").convert()
ataque5h.set_colorkey([0,0,0])
ataque6h = pygame.image.load("Imagenes/Hacha/Ataque6.png").convert()
ataque6h.set_colorkey([0,0,0])
ataque7h = pygame.image.load("Imagenes/Hacha/Ataque7.png").convert()
ataque7h.set_colorkey([0,0,0])
caminar1h = pygame.image.load("Imagenes/Hacha/Caminar1.png").convert()
caminar1h.set_colorkey([0,0,0])
caminar2h = pygame.image.load("Imagenes/Hacha/Caminar2.png").convert()
caminar2h.set_colorkey([0,0,0])
caminar3h = pygame.image.load("Imagenes/Hacha/Caminar3.png").convert()
caminar3h.set_colorkey([0,0,0])
caminar4h = pygame.image.load("Imagenes/Hacha/Caminar4.png").convert()
caminar4h.set_colorkey([0,0,0])
caminar5h = pygame.image.load("Imagenes/Hacha/Caminar5.png").convert()
caminar5h.set_colorkey([0,0,0])
caminar6h = pygame.image.load("Imagenes/Hacha/Caminar6.png").convert()
caminar6h.set_colorkey([0,0,0])
caminar7h = pygame.image.load("Imagenes/Hacha/Caminar7.png").convert()
caminar7h.set_colorkey([0,0,0])
dañoh = pygame.image.load("Imagenes/Hacha/Daño.png").convert()
dañoh.set_colorkey([0,0,0])
muerteh = pygame.image.load("Imagenes/Hacha/Muerte.png").convert()
muerteh.set_colorkey([0,0,0])

#Imagenes del avatar con maza
ataque0m = pygame.image.load("Imagenes/Maza/Ataque0.png").convert()
ataque0m.set_colorkey([0,0,0])
ataque1m = pygame.image.load("Imagenes/Maza/Ataque1.png").convert()
ataque1m.set_colorkey([0,0,0])
ataque2m = pygame.image.load("Imagenes/Maza/Ataque2.png").convert()
ataque2m.set_colorkey([0,0,0])
ataque3m = pygame.image.load("Imagenes/Maza/Ataque3.png").convert()
ataque3m.set_colorkey([0,0,0])
ataque4m = pygame.image.load("Imagenes/Maza/Ataque4.png").convert()
ataque4m.set_colorkey([0,0,0])
ataque5m = pygame.image.load("Imagenes/Maza/Ataque5.png").convert()
ataque5m.set_colorkey([0,0,0])
ataque6m = pygame.image.load("Imagenes/Maza/Ataque6.png").convert()
ataque6m.set_colorkey([0,0,0])
ataque7m = pygame.image.load("Imagenes/Maza/Ataque7.png").convert()
ataque7m.set_colorkey([0,0,0])
caminar1m = pygame.image.load("Imagenes/Maza/Caminar1.png").convert()
caminar1m.set_colorkey([0,0,0])
caminar2m = pygame.image.load("Imagenes/Maza/Caminar2.png").convert()
caminar2m.set_colorkey([0,0,0])
caminar3m = pygame.image.load("Imagenes/Maza/Caminar3.png").convert()
caminar3m.set_colorkey([0,0,0])
caminar4m = pygame.image.load("Imagenes/Maza/Caminar4.png").convert()
caminar4m.set_colorkey([0,0,0])
caminar5m = pygame.image.load("Imagenes/Maza/Caminar5.png").convert()
caminar5m.set_colorkey([0,0,0])
caminar6m = pygame.image.load("Imagenes/Maza/Caminar6.png").convert()
caminar6m.set_colorkey([0,0,0])
caminar7m = pygame.image.load("Imagenes/Maza/Caminar7.png").convert()
caminar7m.set_colorkey([0,0,0])
dañom = pygame.image.load("Imagenes/Maza/Daño.png").convert()
dañom.set_colorkey([0,0,0])
muertem = pygame.image.load("Imagenes/Maza/Muerte.png").convert()
muertem.set_colorkey([0,0,0])

#Cargar las imagenes de los rooks
sand_rook_icon = pygame.image.load("Imagenes/Base.png")
sand_rook = pygame.image.load("Imagenes/Sand.png")
rock_rook_icon = pygame.image.load("Imagenes/Base.png")
rock_rook = pygame.image.load("Imagenes/Sand.png")
fire_rook_icon = pygame.image.load("Imagenes/Base.png")
fire_rook = pygame.image.load("Imagenes/Sand.png")
water_rook_icon = pygame.image.load("Imagenes/Base.png")
water_rook = pygame.image.load("Imagenes/Sand.png")
arena = pygame.image.load("Imagenes/Disparos/Arena.png")
arena.set_colorkey([0,0,0])
piedra = pygame.image.load("Imagenes/Disparos/Piedra.png")
piedra.set_colorkey([0,0,0])
fuego = pygame.image.load("Imagenes/Disparos/Magma.gif")
fuego.set_colorkey([0,0,0])
agua = pygame.image.load("Imagenes/Disparos/Hielo.png")
agua.set_colorkey([0,0,0])
#Imagenes de monedas
oro = pygame.image.load("Imagenes/Oro.png").convert()
oro.set_colorkey([0,0,0])
plata = pygame.image.load("Imagenes/Plata.png").convert()
plata.set_colorkey([0,0,0])
cobre = pygame.image.load("Imagenes/Cobre.png").convert()
cobre.set_colorkey([0,0,0])

#Clase Arquero
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
		#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
		#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
		#E:instancia #S:- #R:-
#attack(): inicia la secuencia de ataaque
		#E: instancia #S:- #R:-
class Arquero(pygame.sprite.Sprite):
	def __init__(self, position):
			super().__init__()
			self.image = caminar1a
			self.rect = self.image.get_rect()
			self.rect.topleft = position
			self.frame = 0
			self.caminar = [caminar1a, caminar2a, caminar3a, caminar4a, caminar5a, caminar6a, caminar7a]
			self.ataque = [ataque0a, ataque1a, ataque2a, ataque3a, ataque4a, ataque5a, ataque6a, ataque7a] 
			self.muerte = muertea
			self.daño = dañoa
			self.proyectil = flecha
			self.vida = 5
			self.atacando = False

	def get_frame(self, lista, accion):
		if accion == "caminar":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame = 0
				return lista[self.frame]
		if accion == "ataque":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame = 0
						proyectil = Proyectil("flecha")
						proyectil.rect.x = self.rect.x+40
						proyectil.rect.y = self.rect.y-20
						all_sprite_list.add(proyectil)
						proyectil_list.add(proyectil)

				return lista[self.frame]
	def change_image(self, lista,accion):
		self.image = self.get_frame(lista,accion)

	def update(self):
		if self.rect.y > 20:
				self.change_image(self.caminar, "caminar")
				self.rect.y -= 5
		
	def attack(self):
		self.change_image(self.ataque, "ataque")

#Clase Escudero
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
		#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
		#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
		#E:instancia #S:- #R:-
#attack(): inicia la secuencia de ataaque
		#E: instancia #S:- #R:-
class Escudero(pygame.sprite.Sprite):
	def __init__(self, position):
			super().__init__()
			self.image = caminar1e
			self.rect = self.image.get_rect()
			self.rect.topleft = position
			self.frame = 0
			self.caminar = [caminar1e, caminar2e, caminar3e, caminar4e, caminar5e, caminar6e, caminar7e]
			self.ataque = [ataque0e, ataque1e, ataque2e, ataque3e, ataque4e, ataque5e, ataque6e, ataque7e] 
			self.muerte = muertee
			self.daño = dañoe
			self.vida = 10
			self.atacando = False

	def get_frame(self, lista, accion):
		if accion == "caminar":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame = 0
				return lista[self.frame]
		if accion == "ataque":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame= 0
						proyectil = Proyectil("espada")
						proyectil.rect.x = self.rect.x+40
						proyectil.rect.y = self.rect.y-20
						all_sprite_list.add(proyectil)
						proyectil_list.add(proyectil) 
				return lista[self.frame]
	def change_image(self, lista,accion):
		self.image = self.get_frame(lista,accion)

	def update(self):
		if self.rect.y > 20:
				self.change_image(self.caminar, "caminar")
				self.rect.y -= 5
	
	def attack(self):
		self.change_image(self.ataque, "ataque")
#Clase Hacha
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
		#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
		#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
		#E:instancia #S:- #R:-
#attack(): inicia la secuencia de ataaque
		#E: instancia #S:- #R:-
class Hacha(pygame.sprite.Sprite):
	def __init__(self, position):
			super().__init__()
			self.image = caminar1h
			self.rect = self.image.get_rect()
			self.rect.topleft = position
			self.frame = 0
			self.caminar = [caminar1h, caminar2h, caminar3h, caminar4h, caminar5h, caminar6h, caminar7h]
			self.ataque = [ataque0h, ataque1h, ataque2h, ataque3h, ataque4h, ataque5h, ataque6h, ataque7h]
			self.muerte = muerteh
			self.daño = dañoh
			self.vida = 20
			self.potencia = 9
			self.atacando = False

	def get_frame(self, lista, accion):
		if accion == "caminar":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame = 0
				return lista[self.frame]
		if accion == "ataque":
				self.frame += 1
				if self.frame > (len(lista) - 1):
						self.frame = 0 
				return lista[self.frame]
	def change_image(self, lista,accion):
		self.image = self.get_frame(lista,accion)

	def update(self):
		if self.rect.y > 20:
				self.change_image(self.caminar, "caminar")
				self.rect.y -= 5
	
	def attack(self):
		self.change_image(self.ataque, "ataque")
#Clase Maza
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
		#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
		#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
		#E:instancia #S:- #R:-
#attack(): inicia la secuencia de ataaque
		#E: instancia #S:- #R:-
class Maza(pygame.sprite.Sprite):
	def __init__(self, position):
		super().__init__()
		self.image = caminar1m
		self.rect = self.image.get_rect()
		self.rect.topleft = position
		self.frame = 0
		self.caminar = [caminar1m, caminar2m, caminar3m, caminar4m, caminar5m, caminar6m, caminar7m]
		self.ataque = [ataque0m, ataque1m, ataque2m, ataque3m, ataque4m, ataque5m, ataque6m, ataque7m] 
		self.muerte = muertem
		self.daño = dañom
		self.vida = 25
		self.potencia = 12
		self.atacando = False

	def get_frame(self, lista, accion):
		if accion == "caminar":
			self.frame += 1
			if self.frame > (len(lista) - 1):
				self.frame = 0
			return lista[self.frame]
		if accion == "ataque":
			self.frame += 1
			if self.frame > (len(lista) - 1):
				self.frame =0 
			return lista[self.frame]
	def change_image(self, lista,accion):
		self.image = self.get_frame(lista,accion)

	def update(self):
		if self.rect.y > 20:
			self.change_image(self.caminar, "caminar")
			self.rect.y -= 5

	
	def attack(self):
		self.change_image(self.ataque, "ataque")

#Clase Proyectil
#Atributos: self.image, self.rect
#Funciones
#update(): actualiza la posicion del sprite
		#E: instancia #S: - #R: -
class Proyectil(pygame.sprite.Sprite):
	def __init__(self,tipo):
		super().__init__()
		if tipo == "flecha":
			self.image = flecha
			self.potencia = 2
		if tipo == "espada":
			self.image = espada
			self.potencia = 3
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y -= 10 
#Clase Moneda
#Atributos:self.tipo,self.image,self.rect
#Funciones -
class Moneda(pygame.sprite.Sprite):
	def __init__(self,tipo):
		super().__init__()
		self.tipo = tipo
		if tipo =="oro":
			self.image = oro
			self.rect = self.image.get_rect()
		if tipo =="plata":
			self.image = plata
			self.rect = self.image.get_rect()
		if tipo =="cobre":
			self.image = cobre
			self.rect = self.image.get_rect()

#Clase Sand
#Atributos: self.image, self.rect
#Funciones:
#attack(): crea la instancia elemental (ataque de los rooks)
		#E: instancia #S: - #R: -  
class Sand(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = sand_rook
		self.rect = self.image.get_rect()
		self.vida = 7
	def attack(self):
		elemental = Elemental("Sand")
		elemental.rect.x = self.rect.x+15
		elemental.rect.y = self.rect.y+30
		all_sprite_list.add(elemental)
		elemental_list.add(elemental)


#Clase Rock
#Atributos: self.image, self.rect
#Funciones:
#attack(): crea la instancia elemental (ataque de los rooks)
		#E: instancia #S: - #R: - 
class Rock(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = rock_rook
		self.rect = self.image.get_rect()
		self.vida = 14
	def attack(self):
		elemental = Elemental("Rock")
		elemental.rect.x = self.rect.x+15
		elemental.rect.y = self.rect.y+30
		all_sprite_list.add(elemental)
		elemental_list.add(elemental)

#Clase Fire
#Atributos: self.image, self.rect
#Funciones:
#attack(): crea la instancia elemental (ataque de los rooks)
		#E: instancia #S: - #R: - 
class Fire(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = fire_rook
		self.rect = self.image.get_rect()
		self.vida = 16
	def attack(self):
		elemental = Elemental("Fire")
		elemental.rect.x = self.rect.x+15
		elemental.rect.y = self.rect.y+30
		all_sprite_list.add(elemental)
		elemental_list.add(elemental)

#Clase Water
#Atributos: self.image, self.rect
#Funciones:
#attack(): crea la instancia elemental (ataque de los rooks)
		#E: instancia #S: - #R: - 
class Water(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = water_rook
		self.rect = self.image.get_rect()
		self.vida = 16
	def attack(self):
		elemental = Elemental("Water")
		elemental.rect.x = self.rect.x+15
		elemental.rect.y = self.rect.y+30
		all_sprite_list.add(elemental)
		elemental_list.add(elemental)


#Clase Elemental
#Atributos: self.image, self.rect
#Funciones
#update(): actualiza la posicion del sprite
		#E: instancia #S: - #R: -
class Elemental(pygame.sprite.Sprite):
	def __init__(self, tipo):
		super().__init__()
		if tipo == "Sand":
			self.image = arena
			self.potencia = 2
		if tipo == "Rock":
			self.image = piedra
			self.potencia = 4
		if tipo == "Water":
			self.image = agua
			self.potencia = 8
		if tipo == "Fire":
			self.image = fuego
			self.potencia = 8
		self.rect = self.image.get_rect()
	def update(self):
			self.rect.y += 10 



#Agrupaciones de sprites
all_sprite_list = pygame.sprite.Group()
avatar_list = pygame.sprite.Group()
arquero_list = pygame.sprite.Group()
escudero_list = pygame.sprite.Group()
hacha_list = pygame.sprite.Group()
maza_list = pygame.sprite.Group()
proyectil_list = pygame.sprite.Group()
rook_list = pygame.sprite.Group()
monedas_list = pygame.sprite.Group()
elemental_list = pygame.sprite.Group()
#Valores para la creacion de oleadas
coordy =1200
oleada = 1
enemigos = 0
#Creacion de avatars
def invocar():
	global coordy
	global oleada
	global enemigos
	for i in range(60):
		x = random.choice(["arquero", "escudero", "hacha", "maza"]) 
		if x == "arquero":
			arquero = Arquero((random.choice([252,333,416,498,583]),coordy))
			arquero_list.add(arquero)
			avatar_list.add(arquero)
			all_sprite_list.add(arquero)
		if x == "escudero":
			escudero = Escudero((random.choice([252,333,416,498,583]),coordy))
			escudero_list.add(escudero)
			avatar_list.add(escudero)
			all_sprite_list.add(escudero)
		if x == "hacha":
			hacha = Hacha((random.choice([252,333,416,498,583]),coordy))
			hacha_list.add(hacha)
			avatar_list.add(hacha)
			all_sprite_list.add(hacha)
		if x == "maza":
			maza = Maza((random.choice([252,333,416,498,583]),coordy))
			maza_list.add(maza)
			avatar_list.add(maza)
			all_sprite_list.add(maza)
		#Revision de numero de oleada y de enemigos
		if oleada < 5:
			coordy += 300
			enemigos += 1
			if enemigos==5:
				oleada += 1
				enemigos =0
				if oleada == 5:
					coordy+=1200
		elif oleada < 9:
			coordy += 210
			enemigos += 1
			if enemigos==5:
				oleada += 1
				enemigos =0
				if oleada == 9:
					coordy+=1200
		elif oleada < 13:
			coordy += 120
			enemigos += 1
			if enemigos==5:
				oleada += 1
				enemigos =0
				if oleada == 13:
					break
		else:
			break
#Variables del reloj
segundo2 = 0
minuto1 = 0
minuto2 = 0
resto = 0
#Variables de ataque
resto_torre = 0
resto_arquero =0
resto_escudero = 0
resto_hacha = 0
resto_maza = 0
cadencia = 2
cadencia_arquero = 1
cadencia_escudero = 1
cadencia_hacha = 1
cadencia_maza = 1
numero_ataque_hacha = 1
numero_ataque_maza = 1
score = 0
#Variables de compra
sand_rook_hitbox = [pygame.Rect(25,35,135,125), "Sand"]
rock_rook_hitbox = [pygame.Rect(25,187,135,125), "Rock"]
fire_rook_hitbox = [pygame.Rect(25,329,135,125), "Fire"]
water_rook_hitbox = [pygame.Rect(25,470,135,125), "Water"]
hitboxes = [sand_rook_hitbox,rock_rook_hitbox,fire_rook_hitbox,water_rook_hitbox]
agarrar = False
clase = ""
#Cuadrados de la matriz
Cuadro_1 = [pygame.Rect(255,112, 75, 62), 0]
Cuadro_2 = [pygame.Rect(336,112, 75, 62),0] 
Cuadro_3 = [pygame.Rect(419,112, 75, 62),0]
Cuadro_4 = [pygame.Rect(501,112, 75, 62),0]
Cuadro_5 = [pygame.Rect(586,112, 75, 62),0]
Cuadro_6 = [pygame.Rect(255,186, 75, 62),0]
Cuadro_7 = [pygame.Rect(336,186, 75, 62),0]
Cuadro_8 = [pygame.Rect(419,186, 75, 62),0]
Cuadro_9 = [pygame.Rect(501,186, 75, 62),0]
Cuadro_10 = [pygame.Rect(586,186, 75, 62),0]
Cuadro_11 = [pygame.Rect(255,259, 75, 62),0]
Cuadro_12 = [pygame.Rect(336,259, 75, 62),0]
Cuadro_13 = [pygame.Rect(419,259, 75, 62),0]
Cuadro_14 = [pygame.Rect(501,259, 75, 62),0]
Cuadro_15 = [pygame.Rect(586,259, 75, 62),0]
Cuadro_16 = [pygame.Rect(255,339, 75, 62),0]
Cuadro_17 = [pygame.Rect(336,339, 75, 62),0]
Cuadro_18 = [pygame.Rect(419,339, 75, 62),0]
Cuadro_19 = [pygame.Rect(501,339, 75, 62),0]
Cuadro_20 = [pygame.Rect(586,339, 75, 62),0]
Cuadro_21 = [pygame.Rect(255,417, 75, 62),0]
Cuadro_22 = [pygame.Rect(336,417, 75, 62),0]
Cuadro_23 = [pygame.Rect(419,417, 75, 62),0]
Cuadro_24 = [pygame.Rect(501,417, 75, 62),0]
Cuadro_25 = [pygame.Rect(586,417, 75, 62),0]
Cuadro_26 = [pygame.Rect(255,494, 75, 62),0]
Cuadro_27 = [pygame.Rect(336,494, 75, 62),0]
Cuadro_28 = [pygame.Rect(419,494, 75, 62),0]
Cuadro_29 = [pygame.Rect(501,494, 75, 62),0]
Cuadro_30 = [pygame.Rect(586,494, 75, 62),0]
Cuadro_31 = [pygame.Rect(255,569, 75, 62),0]
Cuadro_32 = [pygame.Rect(336,569, 75, 62),0]
Cuadro_33 = [pygame.Rect(419,569, 75, 62),0]
Cuadro_34 = [pygame.Rect(501,569, 75, 62),0]
Cuadro_35 = [pygame.Rect(586,569, 75, 62),0]
Cuadro_36 = [pygame.Rect(255,649, 75, 62),0]
Cuadro_37 = [pygame.Rect(336,649, 75, 62),0]
Cuadro_38 = [pygame.Rect(419,649, 75, 62),0]
Cuadro_39 = [pygame.Rect(501,649, 75, 62),0]
Cuadro_40 = [pygame.Rect(586,649, 75, 62),0]
Cuadros = [Cuadro_1 ,Cuadro_2 ,Cuadro_3 ,Cuadro_4 ,Cuadro_5 ,Cuadro_6 ,Cuadro_7 ,Cuadro_8 ,Cuadro_9 ,Cuadro_10 ,Cuadro_11 ,Cuadro_12 ,Cuadro_13 ,Cuadro_14 ,Cuadro_15 ,Cuadro_16 ,Cuadro_17 ,Cuadro_18 ,Cuadro_19 ,Cuadro_20 ,Cuadro_21 ,Cuadro_22 ,Cuadro_23 ,Cuadro_24 ,Cuadro_25 ,Cuadro_26 ,Cuadro_27 ,Cuadro_28 ,Cuadro_29 ,Cuadro_30 ,Cuadro_31 ,Cuadro_32 ,Cuadro_33 ,Cuadro_34 ,Cuadro_35 ,Cuadro_36 ,Cuadro_37 ,Cuadro_38 ,Cuadro_39 ,Cuadro_40]   
escenario = 1
reset = 1
game_over = False
perdiste = False
ganaste= False
animacion = 0
invocar()
#Main loop
while True:
	tiempo = pygame.time.get_ticks()//1000-resto
	if tiempo == 10 :
		tiempo=0
		segundo2 += 1
		resto += 10
		#Creacion de monedas
		coin = Moneda(random.choice(["cobre","oro","plata"]))
		coin.rect.x = random.randint(260,635)
		coin.rect.y = random.randint(130,750)
		monedas_list.add(coin)
		all_sprite_list.add(coin)

	if segundo2 >= 6:
		segundo2 = 0
		minuto1 +=1
	if minuto1 > 9:
		minuto1 = 0
		minuto2 += 1
	
	tiempo_torre = pygame.time.get_ticks()//1000-resto_torre
	if tiempo_torre == cadencia:
		tiempo_torre = 0
		resto_torre += cadencia
		for rook in rook_list:
			for avatar in avatar_list:
				if rook.rect.x == 252 and avatar.rect.x == 252 and avatar.rect.y < 780 and avatar.rect.y - rook.rect.y > 0: 
						rook.attack()
				if rook.rect.x == 333 and avatar.rect.x == 333 and avatar.rect.y < 780 and avatar.rect.y - rook.rect.y > 0: 
						rook.attack()
				if rook.rect.x == 416 and avatar.rect.x == 416 and avatar.rect.y < 780 and avatar.rect.y - rook.rect.y > 0: 
						rook.attack()
				if rook.rect.x == 498 and avatar.rect.x == 498 and avatar.rect.y < 780 and avatar.rect.y - rook.rect.y > 0: 
						rook.attack()
				if rook.rect.x == 583 and avatar.rect.x == 583 and avatar.rect.y < 780 and avatar.rect.y - rook.rect.y > 0: 
						rook.attack()
	tiempo_arquero = pygame.time.get_ticks()//1000-resto_arquero
	if tiempo_arquero == cadencia_arquero:
		tiempo_arquero = 0
		resto_arquero +=cadencia_arquero
		for arquero in arquero_list:
			for cuadro in Cuadros:
				if      cuadro[1] !=0 and cuadro[0].x==255 and arquero.rect.x == 252 and arquero.rect.y < 750 and arquero.rect.y - cuadro[0].y > 0: 
					arquero.attack()
					arquero.attack()
					arquero.attack()
					arquero.atacando = True
				elif cuadro[1] !=0 and cuadro[0].x==336 and arquero.rect.x == 333 and arquero.rect.y < 750 and arquero.rect.y - cuadro[0].y > 0: 
					arquero.attack()
					arquero.attack()
					arquero.attack()
					arquero.atacando = True
				elif cuadro[1] !=0 and cuadro[0].x==419 and arquero.rect.x == 416 and arquero.rect.y < 750 and arquero.rect.y - cuadro[0].y > 0: 
					arquero.attack()
					arquero.attack()
					arquero.attack()
					arquero.atacando = True
				elif cuadro[1] !=0 and cuadro[0].x==501 and arquero.rect.x == 498 and arquero.rect.y < 750 and arquero.rect.y - cuadro[0].y > 0: 
					arquero.attack()
					arquero.attack()
					arquero.attack()
					arquero.atacando = True
				elif cuadro[1] !=0 and cuadro[0].x==586 and arquero.rect.x == 583 and arquero.rect.y < 750 and arquero.rect.y - cuadro[0].y > 0: 
					arquero.attack()
					arquero.attack()
					arquero.attack()
					arquero.atacando = True
	tiempo_escudero = pygame.time.get_ticks()//1000-resto_escudero
	if tiempo_escudero == cadencia_escudero:
		tiempo_escudero = 0
		resto_escudero +=cadencia_escudero
		for escudero in escudero_list:
			for cuadro in Cuadros:
				if cuadro[1] !=0 and cuadro[0].x==255 and escudero.rect.x == 252 and escudero.rect.y < 700 and escudero.rect.y - cuadro[0].y > 0: 
					escudero.attack()
					escudero.attack()
					escudero.attack()
					escudero.atacando = True
				if cuadro[1] !=0 and cuadro[0].x==336 and escudero.rect.x == 333 and escudero.rect.y < 700 and escudero.rect.y - cuadro[0].y > 0: 
					escudero.attack()
					escudero.attack()
					escudero.attack()
					escudero.atacando = True
				if cuadro[1] !=0 and cuadro[0].x==419 and escudero.rect.x == 416 and escudero.rect.y < 700 and escudero.rect.y - cuadro[0].y > 0: 
					escudero.attack()
					escudero.attack()
					escudero.attack()
					escudero.atacando = True
				if cuadro[1] !=0 and cuadro[0].x==501 and escudero.rect.x == 498 and escudero.rect.y < 700 and escudero.rect.y - cuadro[0].y > 0: 
					escudero.attack()
					escudero.attack()
					escudero.attack()
					escudero.atacando = True
				if cuadro[1] !=0 and cuadro[0].x==586 and escudero.rect.x == 583 and escudero.rect.y < 700 and escudero.rect.y - cuadro[0].y > 0: 
					escudero.attack()
					escudero.attack()
					escudero.attack()
					escudero.atacando = True
	
	tiempo_hacha = pygame.time.get_ticks()//1000-resto_hacha
	if tiempo_hacha == cadencia_hacha:
		tiempo_hacha = 0
		resto_hacha +=cadencia_hacha
		for hacha in hacha_list:
			for rook in rook_list:
					if pygame.sprite.collide_rect(hacha, rook) and hacha.rect.y - rook.rect.y > 0:
						hacha.attack()
						hacha.attack()
						hacha.attack()
						numero_ataque_hacha +=1
						hacha.atacando = True
						if numero_ataque_hacha ==3:
							rook.vida -= hacha.potencia
							numero_ataque=1
					if rook.vida <0:
						rook_list.remove(rook)
						all_sprite_list.remove(rook)
						for avatar in avatar_list:
							avatar.atacando = False
						for cuadro in Cuadros:
							if cuadro[1]==rook:
								cuadro[1] = 0
	tiempo_maza = pygame.time.get_ticks()//1000-resto_maza
	if tiempo_maza == cadencia_maza:
		tiempo_maza = 0
		resto_maza +=cadencia_maza
		for maza in maza_list:
			for rook in rook_list:
				if pygame.sprite.collide_rect(maza, rook) and maza.rect.y - rook.rect.y > 0:
					maza.attack()
					maza.attack()
					maza.attack()
					numero_ataque_maza +=1
					maza.atacando = True
					if numero_ataque_maza ==3:
						rook.vida -= maza.potencia
						numero_ataque=1
				if rook.vida <0:
					rook_list.remove(rook)
					all_sprite_list.remove(rook)
					for avatar in avatar_list:
						avatar.atacando = False
					for cuadro in Cuadros:
						if cuadro[1]==rook:
							cuadro[1] = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	if event.type == pygame.MOUSEMOTION:
		for coin in monedas_list:
			if mouse_pos[0]>=coin.rect.x+10 and mouse_pos[0]<=coin.rect.x+40 and mouse_pos[1]>=coin.rect.y+10 and mouse_pos[1]<=coin.rect.y+40:
				if coin.tipo == "oro":
					monedas += 100
					monedas_list.remove(coin)
					all_sprite_list.remove(coin)
				if coin.tipo == "plata":
					monedas += 50
					monedas_list.remove(coin)
					all_sprite_list.remove(coin)
				if coin.tipo == "cobre":
					monedas += 25
					monedas_list.remove(coin)
					all_sprite_list.remove(coin)

	if pygame.mouse.get_pressed()[0]==1:
		mouse = event.pos
		if mouse[0]>640 and mouse[0]<706 and mouse[1]>9 and mouse [1]<56: #Boton volver
			pygame.quit()
			os.system("Menu.py")
		for hitbox in hitboxes:
			if hitbox[0].collidepoint(mouse) and not agarrar:
				if hitbox[1]=="Sand" and monedas >= 50:
					monedas -=50
					agarrar = True
					clase = hitbox[1]
				if hitbox[1]=="Rock" and monedas >= 100:
					monedas -=100
					agarrar = True
					clase = hitbox[1]
				if hitbox[1]=="Fire" and monedas >= 150:
					monedas -=150
					agarrar = True
					clase = hitbox[1]
				if hitbox[1]=="Water" and monedas >= 150:
					monedas -=150
					agarrar = True
					clase = hitbox[1]
		for cuadro in Cuadros:
			if cuadro[0].collidepoint(mouse) and agarrar and clase == "Sand" and cuadro[1]==0:
				agarrar = False
				sand = Sand()
				sand.rect.x = cuadro[0].x-3
				sand.rect.y = cuadro[0].y-37
				all_sprite_list.add(sand)
				rook_list.add(sand)
				cuadro[1] = sand
				clase == ""

			if cuadro[0].collidepoint(mouse) and agarrar and clase == "Rock" and cuadro[1]==0:
				agarrar = False
				rock = Rock()
				rock.rect.x = cuadro[0].x-3
				rock.rect.y = cuadro[0].y-37
				all_sprite_list.add(rock)
				rook_list.add(rock)
				cuadro[1] = rock
				clase == ""
			if cuadro[0].collidepoint(mouse) and agarrar and clase == "Fire" and cuadro[1]==0:
				agarrar = False
				fire = Fire()
				fire.rect.x = cuadro[0].x-3
				fire.rect.y = cuadro[0].y-37
				all_sprite_list.add(fire)
				rook_list.add(fire)
				cuadro[1] = fire
				clase == ""
			if cuadro[0].collidepoint(mouse) and agarrar and clase == "Water" and cuadro[1]==0:
				agarrar = False
				water = Water()
				water.rect.x = cuadro[0].x-3
				water.rect.y = cuadro[0].y-37
				all_sprite_list.add(water)
				rook_list.add(water)
				cuadro[1] = water
				clase == ""

	if pygame.mouse.get_pressed()[2]==1:
		mouse = event.pos
		for cuadro in Cuadros:
			if cuadro[0].collidepoint(mouse) and not agarrar and cuadro[1]!=0:
				all_sprite_list.remove(cuadro[1])
				rook_list.remove(cuadro[1])
				cuadro[1]=0
	#Renderizado del reloj
	relojseg1 = font.render(str(tiempo),0,(255,255,255))
	relojseg2 = font.render(str(segundo2),0,(255,255,255))
	separacion = font.render(":",0,(255,255,255))
	relojmin1 = font.render(str(minuto1),0,(255,255,255))
	relojmin2 = font.render(str(minuto2),0,(255,255,255))
	#Renderizado de cantidad de monedas
	cant_monedas = font.render(str(monedas),0,(239,184,16))

	for proyectil in proyectil_list:
		for rook in rook_list:
			if pygame.sprite.collide_rect_ratio(0.4)(proyectil, rook):
				all_sprite_list.remove(proyectil)
				proyectil_list.remove(proyectil)
				rook.vida -= proyectil.potencia
				if rook.vida <=0:
					rook_list.remove(rook)
					all_sprite_list.remove(rook)
					for avatar in avatar_list:
						avatar.atacando = False
					for cuadro in Cuadros:
						if cuadro[1]==rook:
							cuadro[1] = 0
			
			if proyectil.rect.y < -10:
				all_sprite_list.remove(proyectil)
				proyectil_list.remove(proyectil)        
		
	for elemental in elemental_list:
		for avatar in avatar_list:
			if pygame.sprite.collide_rect_ratio(0.6)(elemental, avatar):
				all_sprite_list.remove(elemental)
				elemental_list.remove(elemental)
				avatar.vida-=elemental.potencia
				if avatar.vida <=0:
					monedas += 100
					avatar_list.remove(avatar)
					all_sprite_list.remove(avatar)
					if avatar in arquero_list:
						arquero_list.remove(avatar)
					if avatar in escudero_list:
						escudero_list.remove(avatar)
					if avatar in hacha_list:
						hacha_list.remove(avatar)
					if avatar in maza_list:
						maza_list.remove(avatar)
					score +=1 

			if elemental.rect.y > 800:
				all_sprite_list.remove(elemental)
				elemental_list.remove(elemental)
	#Mostrar en pantala
	if escenario ==1:
		screen.blit(matriz1,[0,0])

	if escenario == 2:
		screen.blit(matriz2,[0,0])
		if reset == 1:
			for rook in rook_list:
				rook_list.remove(rook)
				all_sprite_list.remove(rook)
			for elemental in elemental_list:
				elemental_list.remove(elemental)
				all_sprite_list.remove(elemental)
			for cuadro in Cuadros:
				if cuadro[1]!=0:
					cuadro[1] = 0
			reset +=1

	if escenario == 3:
		screen.blit(matriz3,[0,0])
		if reset == 2:
			for rook in rook_list:
				rook_list.remove(rook)
				all_sprite_list.remove(rook)
			for elemental in elemental_list:
				elemental_list.remove(elemental)
				all_sprite_list.remove(elemental)
			for cuadro in Cuadros:
				if cuadro[1]!=0:
					cuadro[1] = 0
			reset +=1
			
	if game_over == False:
		screen.blit(relojseg1,[140,710])
		screen.blit(relojseg2,[120,710])
		screen.blit(relojmin1,[80,710])
		screen.blit(relojmin2,[60,710])
		screen.blit(cant_monedas,[70,635])
		screen.blit(separacion,[105,706])
		screen.blit(volver, [630,0])
		screen.blit(sand_rook_icon, [40,0])
		screen.blit(rock_rook_icon, [40,147])
		screen.blit(fire_rook_icon, [40,287])
		screen.blit(water_rook_icon, [40,430])
		all_sprite_list.draw(screen)
		proyectil_list.update()
		elemental_list.update()
		for avatar in avatar_list:
			if avatar.atacando == False:
				avatar.update()
			if avatar.rect.y <=21:
				perdiste = True
				game_over = True
				animacion = 0
		mouse_pos = pygame.mouse.get_pos()
		if agarrar==True and clase == "Sand":
			screen.blit(sand_rook, [mouse_pos[0]-35, mouse_pos[1]-70])
		if agarrar==True and clase == "Rock":
			screen.blit(rock_rook, [mouse_pos[0]-35, mouse_pos[1]-70])
		if agarrar==True and clase == "Fire":
			screen.blit(fire_rook, [mouse_pos[0]-35, mouse_pos[1]-70])
		if agarrar==True and clase == "Water":
			screen.blit(water_rook, [mouse_pos[0]-35, mouse_pos[1]-70])
		if score == 20:
			escenario +=1
			score=0
			if score == 0 and escenario >3:
				ganaste = True
				game_over =True
				animacion = 0
	if game_over== True:
		if perdiste == True:
			if animacion%2 == 0:
				screen.blit(negro,[0,0])
				time.sleep(0.5)
			if animacion%2 == 1:
				screen.blit(perdedor,[0,0])
			animacion += 1
			time.sleep(0.5)
		if ganaste == True:
			if animacion%2 == 0:
				screen.blit(negro,[0,0])
				time.sleep(0.5)
			if animacion%2 == 1:
				screen.blit(ganador,[0,0])
			if score ==0:
				tiempo_conseguido = tiempo+ segundo2*10 + minuto1 *60
				score +=1
			animacion += 1
			time.sleep(0.5)

			resultado = font.render("Tiempo: "+str(tiempo_conseguido)+" segundos",0,(255,255,255))
			screen.blit(resultado,[150,600])
	#Default
	pygame.display.flip()
	clock.tick(15)
	