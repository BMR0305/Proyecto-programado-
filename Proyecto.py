import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '10' #se centra la ventana de juego
pygame.init()
#Crear vnetana
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avdvice Machine")
#Reloj
clock=pygame.time.Clock()
#Fondos
background = pygame.image.load("Imagenes/Menu.jpg").convert()
#Botonoes
start = pygame.image.load("Imagenes/Start.png").convert()
#start.set_colorkey([0,0,0])
admin = pygame.image.load("Imagenes/Admin.png").convert()
admin.set_colorkey([0,0,0])
español_v = pygame.image.load("Imagenes/Español_v.png").convert()
español_v.set_colorkey([0,0,0])
español_r = pygame.image.load("Imagenes/Español_r.png").convert()
español_r.set_colorkey([0,0,0])
english_v = pygame.image.load("Imagenes/English_v.png").convert()
english_v.set_colorkey([0,0,0])
english_r = pygame.image.load("Imagenes/English_r.png").convert()
english_r.set_colorkey([0,0,0])
#Variables de entry
active = False
text = ""
font = pygame.font.Font(None, 40)
color_inactive = pygame.Color(45,154,212)
color_active = pygame.Color(47,117,161)
color = color_inactive
input_box = pygame.Rect(167, 550, 230, 40)
escenario = 1
#idioma
idioma = "español"
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  
			sys.exit()
		if escenario == 1:
			if event.type == pygame.MOUSEBUTTONDOWN: 
				mouse = event.pos
				if input_box.collidepoint(event.pos): #revisa si se da click en el entry
					active = True
					color = color_active
				else:
					active = False
					color = color_inactive

			if event.type == pygame.KEYDOWN:
				if active: 
					if event.key == pygame.K_BACKSPACE: #detecta si es el boton es el de borrar para eliminar un caracter
						text = text [:len(text)-1]
					elif len(text)>10: #limite de caracteres
						if event.key == pygame.K_BACKSPACE: 
							text = text [:len(text)-1]
						else:
							None
					else:
						text += event.unicode
	if escenario == 1:
		#Renderiza el fondo
		screen.blit(background,[0,0])
		#Input box
		pygame.draw.rect(screen, color, input_box, 4)
		#Renderiza el texto
		txt_surface = font.render(text, True, color_inactive)
		screen.blit(txt_surface, (input_box.x+5, input_box.y+7))
		#Botones
		screen.blit(start, [372,67])
		screen.blit(admin, [207,435])
		if idioma == "español":
			screen.blit(español_v, [368,200])
			screen.blit(english_r, [275,300])


	pygame.display.flip()
	clock.tick(60)