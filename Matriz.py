import pygame, sys, random ,time
pygame.init()
#Pantalla
size = (720,800)
pygame.display.set_caption("Avatars vs Rooks")
screen = pygame.display.set_mode(size)
#Reloj
clock=pygame.time.Clock()
#Fuente
font = pygame.font.Font(None, 60)

#Fondo
matriz = pygame.image.load("Imagenes/Matriz.jpg").convert()
#Imagenes del arquero
ataque1a = pygame.image.load("Imagenes/Arquero/Ataque1.png").convert()
ataque1a.set_colorkey([0,0,0])
ataque2a = pygame.image.load("Imagenes/Arquero/Ataque2.png").convert()
ataque2a.set_colorkey([0,0,0])
ataque3a = pygame.image.load("Imagenes/Arquero/Ataque3.png").convert()
ataque3a.set_colorkey([0,0,0])
ataque4a = pygame.image.load("Imagenes/Arquero/Ataque4.png").convert()
ataque4a.set_colorkey([0,0,0])
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
ataque1e = pygame.image.load("Imagenes/Escudero/Ataque1.png").convert()
ataque1e.set_colorkey([0,0,0])
ataque2e = pygame.image.load("Imagenes/Escudero/Ataque2.png").convert()
ataque2e.set_colorkey([0,0,0])
ataque3e = pygame.image.load("Imagenes/Escudero/Ataque3.png").convert()
ataque3e.set_colorkey([0,0,0])
ataque4e = pygame.image.load("Imagenes/Escudero/Ataque4.png").convert()
ataque4e.set_colorkey([0,0,0])
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
ataque1h = pygame.image.load("Imagenes/Hacha/Ataque1.png").convert()
ataque1h.set_colorkey([0,0,0])
ataque2h = pygame.image.load("Imagenes/Hacha/Ataque2.png").convert()
ataque2h.set_colorkey([0,0,0])
ataque3h = pygame.image.load("Imagenes/Hacha/Ataque3.png").convert()
ataque3h.set_colorkey([0,0,0])
ataque4h = pygame.image.load("Imagenes/Hacha/Ataque4.png").convert()
ataque4h.set_colorkey([0,0,0])
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
ataque1m = pygame.image.load("Imagenes/Maza/Ataque1.png").convert()
ataque1m.set_colorkey([0,0,0])
ataque2m = pygame.image.load("Imagenes/Maza/Ataque2.png").convert()
ataque2m.set_colorkey([0,0,0])
ataque3m = pygame.image.load("Imagenes/Maza/Ataque3.png").convert()
ataque3m.set_colorkey([0,0,0])
ataque4m = pygame.image.load("Imagenes/Maza/Ataque4.png").convert()
ataque4m.set_colorkey([0,0,0])
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
#Clase Arquero
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
	#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
	#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
	#E:instancia #S:- #R:-
class Arquero(pygame.sprite.Sprite):
    def __init__(self, position):
            super().__init__()
            self.image = caminar1a
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.frame = 0
            self.caminar = [caminar1a, caminar2a, caminar3a, caminar4a, caminar5a, caminar6a, caminar7a]
            self.ataque = [ataque1a, ataque2a, ataque3a, ataque4a] 
            self.muerte = muertea
            self.daño = dañoa

    def get_frame(self, lista):
    	self.frame += 1
    	if self.frame > (len(lista) - 1):
        	self.frame = 0
    	return lista[self.frame]
    
    def change_image(self, lista):
        self.image = self.get_frame(lista)

    def update(self):
    	if self.rect.y > 20:
        	self.change_image(self.caminar)
        	self.rect.y -= 5
    def attack(self):
    	if self.rect.y == 500:
    		self.change_image(self.ataque)
#Clase Escudero
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
	#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
	#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
	#E:instancia #S:- #R:-
class Escudero(pygame.sprite.Sprite):
    def __init__(self, position):
            super().__init__()
            self.image = caminar1e
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.frame = 0
            self.caminar = [caminar1e, caminar2e, caminar3e, caminar4e, caminar5e, caminar6e, caminar7e]
            self.ataque = [ataque1e, ataque2e, ataque3e, ataque4e] 
            self.muerte = muertee
            self.daño = dañoe

    def get_frame(self, lista):
    	self.frame += 1
    	if self.frame > (len(lista) - 1):
        	self.frame = 0
    	return lista[self.frame]
    
    def change_image(self, lista):
        self.image = self.get_frame(lista)

    def update(self):
    	if self.rect.y > 20:
        	self.change_image(self.caminar)
        	self.rect.y -= 5
    def attack(self):
    	if self.rect.y == 500:
    		self.change_image(self.ataque)
#Clase Hacha
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
	#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
	#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
	#E:instancia #S:- #R:-
class Hacha(pygame.sprite.Sprite):
    def __init__(self, position):
            super().__init__()
            self.image = caminar1h
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.frame = 0
            self.caminar = [caminar1h, caminar2h, caminar3h, caminar4h, caminar5h, caminar6h, caminar7h]
            self.ataque = [ataque1h, ataque2h, ataque3h, ataque4h] 
            self.muerte = muerteh
            self.daño = dañoh

    def get_frame(self, lista):
    	self.frame += 1
    	if self.frame > (len(lista) - 1):
        	self.frame = 0
    	return lista[self.frame]
    
    def change_image(self, lista):
        self.image = self.get_frame(lista)

    def update(self):
    	if self.rect.y > 20:
        	self.change_image(self.caminar)
        	self.rect.y -= 5
    def attack(self):
    	if self.rect.y == 500:
    		self.change_image(self.ataque)
#Clase Maza
#Atributos: image,rect,rect.topleft,frame,caminar,ataque,muerte,daño
#Funciones
#get_frame(): obtiene el valor de self.frame
	#E:lista de imagenes #S:imagen segun el frame #R:-
#change_image(): cambia la imagen que se observa en pantalla
	#E:lista de imaganes #S:- #R-:
#update():actualiza la posicion del sprite
	#E:instancia #S:- #R:-
class Maza(pygame.sprite.Sprite):
    def __init__(self, position):
            super().__init__()
            self.image = caminar1m
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.frame = 0
            self.caminar = [caminar1m, caminar2m, caminar3m, caminar4m, caminar5m, caminar6m, caminar7m]
            self.ataque = [ataque1m, ataque2m, ataque3m, ataque4m] 
            self.muerte = muertem
            self.daño = dañom

    def get_frame(self, lista):
    	self.frame += 1
    	if self.frame > (len(lista) - 1):
        	self.frame = 0
    	return lista[self.frame]
    
    def change_image(self, lista):
        self.image = self.get_frame(lista)

    def update(self):
    	if self.rect.y > 0:
        	self.change_image(self.caminar)
        	self.rect.y -= 5
    def attack(self):
    	if self.rect.y == 500:
    		self.change_image(self.ataque)
#Agrupaciones de sprites
all_sprite_list = pygame.sprite.Group()
avatar_list = pygame.sprite.Group()
arquero_list = pygame.sprite.Group()
escudero_list = pygame.sprite.Group()
hacha_list = pygame.sprite.Group()
maza_list = pygame.sprite.Group()
coordy = 800
oleada=1
enemigos = 0

#Creacion de avatars
for i in range(60):
	x = random.choice(["arquero","escudero","hacha","maza"])
	if x == "arquero":
		arquero = Arquero((random.choice([185,270,355,435,520]),coordy))
		arquero_list.add(arquero)
		avatar_list.add(arquero)
		all_sprite_list.add(arquero)
	if x == "escudero":
		escudero = Escudero((random.choice([185,270,355,435,520]),coordy))
		escudero_list.add(escudero)
		avatar_list.add(escudero)
		all_sprite_list.add(escudero)
	if x == "hacha":
		hacha = Hacha((random.choice([185,270,355,435,520]),coordy))
		hacha_list.add(hacha)
		avatar_list.add(hacha)
		all_sprite_list.add(hacha)
	if x == "maza":
		maza = Maza((random.choice([185,270,355,435,520]),coordy))
		maza_list.add(maza)
		avatar_list.add(maza)
		all_sprite_list.add(maza)
	#Revision de nuemro de oleada y de enemigos
	if oleada < 5:
		coordy += 400
		enemigos += 1
		if enemigos==5:
			oleada += 1
			enemigos =0
	elif oleada < 9:
		coordy += 280
		enemigos += 1
		if enemigos==5:
			oleada += 1
			enemigos =0
	elif oleada < 13:
		coordy += 160
		enemigos += 1
		if enemigos==5:
			oleada += 1
			enemigos =0
	else:
		break
segundo2 = 0
minuto1 = 0
minuto2 = 0
resto = 0
while True:
	tiempo = pygame.time.get_ticks()//1000-resto
	if tiempo > 9:
		segundo2 += 1
		resto += 9
	if segundo2 > 6:
		segundo2 = 0
		minuto1 +=1
	if minuto1 > 9:
		minuto1 = 0
		minuto2 += 1
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	#Renderizado del reloj
	relojseg1 = font.render(str(tiempo),0,(255,255,255))
	relojseg2 = font.render(str(segundo2),0,(255,255,255))
	separacion = font.render(":",0,(255,255,255))
	relojmin1 = font.render(str(minuto1),0,(255,255,255))
	relojmin2 = font.render(str(minuto2),0,(255,255,255))

	screen.blit(matriz,[0,0])
	screen.blit(relojseg1,[140,710])
	screen.blit(relojseg2,[120,710])
	screen.blit(relojmin1,[80,710])
	screen.blit(relojmin2,[60,710])
	screen.blit(separacion,[105,706])
	all_sprite_list.draw(screen)
	for avatar in avatar_list:
		if avatar.rect.y == 500:
			avatar.attack()
		else:
			avatar.update()
		
	pygame.display.flip()
	clock.tick(20) 
