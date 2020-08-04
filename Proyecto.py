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
fondo = pygame.image.load("Imagenes/Fondo.jpg").convert()
#Botonoes
start = pygame.image.load("Imagenes/Start.png").convert()
start.set_colorkey([0,0,0])
start_p = pygame.image.load("Imagenes/Start_p.png").convert()
start_p.set_colorkey([0,0,0])
admin = pygame.image.load("Imagenes/Admin.png").convert()
admin.set_colorkey([0,0,0])
admin_p = pygame.image.load("Imagenes/Admin_p.png").convert()
admin_p.set_colorkey([0,0,0])
español_v = pygame.image.load("Imagenes/Español_v.png").convert()
español_v.set_colorkey([0,0,0])
español_r = pygame.image.load("Imagenes/Español_r.png").convert()
español_r.set_colorkey([0,0,0])
english_v = pygame.image.load("Imagenes/English_v.png").convert()
english_v.set_colorkey([0,0,0])
english_r = pygame.image.load("Imagenes/English_r.png").convert()
english_r.set_colorkey([0,0,0])
equis = pygame.image.load("Imagenes/Equis.png").convert()
equis.set_colorkey([0,0,0])
#Hitbox botones
hit_start = pygame.Rect(372, 67, 145, 80)
hit_español = pygame.Rect(368,200,150,73)
hit_english = pygame.Rect(275,300,150,73)
hit_admin = pygame.Rect(207,435, 150, 72)
#Variables de entry
active = False
text = ""
font = pygame.font.Font(None, 40)
color_inactive = pygame.Color(45,154,212)
color_active = pygame.Color(47,117,161)
color = color_inactive
input_box = pygame.Rect(167, 550, 230, 40)
escenario = 1
#Variables botones
idioma = "español"
press_s = False
incorrecto= False
while True:
	mouse_pos = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  
			sys.exit()
		if escenario == 1:
			if event.type == pygame.MOUSEBUTTONDOWN: 
				mouse = event.pos
				if input_box.collidepoint(mouse): #revisa si se da click en el entry
					active = True
					color = color_active
				else:
					active = False
					color = color_inactive
				if hit_english.collidepoint(mouse):
					idioma = "english"
				if hit_español.collidepoint(mouse):
					idioma= "español"
				if hit_start.collidepoint(mouse):
					escenario = 2
				if hit_admin.collidepoint(mouse):
					if text == "1234": 
						escenario = 3
					else:
						incorrecto =True
			if event.type == pygame.MOUSEMOTION:
				if mouse_pos[0]>=385 and mouse_pos[0]<=506 and mouse_pos[1]>=80 and mouse_pos[1]<=140:
					press_s = True
				elif mouse_pos[0]>=207 and mouse_pos[0]<=357 and mouse_pos[1]>=435 and mouse_pos[1]<=507:
					press_a = True
				else:
					press_s =False
					press_a =False
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
		if press_s == True:
			screen.blit(start_p,[372,67])
		if press_s ==False:
			screen.blit(start, [372,67])
		if press_a == True:
			screen.blit(admin_p,[207,435])
		if press_a == False:
			screen.blit(admin, [207,435])
		if incorrecto== True:
			screen.blit(equis, [250, 597])
		if idioma == "español":
			screen.blit(español_v, [368,200])
			screen.blit(english_r, [275,300])
		if idioma == "english":
			screen.blit(español_r, [368,200])
			screen.blit(english_v, [275,300])
	
	if escenario ==2:
		screen.blit(fondo,[0,0])
	if escenario ==3:
		screen.blit(background, [0,0])
	pygame.display.flip()
	clock.tick(15)