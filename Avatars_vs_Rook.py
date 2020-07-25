import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' #se centra la ventana de juego
pygame.init()
#Crear vnetana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")
#Reloj
clock=pygame.time.Clock()

#Cargar imagnes
background = pygame.image.load("Imagenes/Menu.jpg").convert()
jugar = pygame.image.load("Imagenes/Jugar.png").convert()
jugar.set_colorkey([0,0,0])
ayuda = pygame.image.load("Imagenes/Ayuda.png").convert()
ayuda.set_colorkey([0,0,0])
ajustes = pygame.image.load("Imagenes/Ajustes.png").convert()
ajustes.set_colorkey([0,0,0])
titulo = pygame.image.load("Imagenes/Titulo.png").convert()
titulo.set_colorkey([0,0,0])
creditos = pygame.image.load("Imagenes/Creditos.png").convert()
creditos.set_colorkey([0,0,0])
usuario = pygame.image.load("Imagenes/Usuario.png").convert()
usuario.set_colorkey([0,0,0])
#Variables del entry
active = False
text = ""
font = pygame.font.Font(None, 40)
color_inactive = pygame.Color(255,255,255)
color_active = pygame.Color(155,155,155)
color = color_inactive
input_box = pygame.Rect(320, 185, 230, 40)

game_over = True
#Bucle principal
while game_over:
	#Captura de eventos
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			if mouse[0]>270 and mouse[0]<470 and mouse[1]>270 and mouse [1]<370 and text != "": #boton jugar, abre al pestaña de juego
				#Guarda en un txt el usuario actual
				usuario = open("Usuario.txt","w")
				usuario.write(text)
				usuario.close()
				#Guarda el usuario en el sistema de registro
				usuarios = open("Registro de Usuarios.txt","a")
				usuarios.write(text+", ")
				usuarios.close()
				game_over = False
				pygame.quit()
				os.system("Matriz.py")

			if mouse[0]>250 and mouse[0]<485 and mouse[1]>420 and mouse [1]<525: #boton ajustes, abre la opestaña de ajustes 
				game_over = False
				pygame.quit()
				os.system("Ajustes.py")
			if mouse[0]>635 and mouse[0]<741 and mouse[1]>695 and mouse [1]<775: #boton ayuda,abre la pestaña de ayuda
				pygame.quit()
				os.system("Ayuda.py")
			if mouse[0]>26 and mouse[0]<295 and mouse[1]>705 and mouse [1]<790: #boton creditos, abre la pestaña de créditos 
				pygame.quit()
				os.system("Creditos.py")
			if mouse[0]>341 and mouse[0]<393 and mouse[1]>553 and mouse [1]<650: #salon de la fama, abre la pestaña del salon de la fama
				pygame.quit()
				os.system("Salon.py")
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
					text += event.unicode #escribe las teclas que se presionan
	try:
		#Fondo
		screen.blit(background,[0,0])
		#Botones
		screen.blit(jugar, [250,250])
		screen.blit(ajustes, [230,400])
		screen.blit(ayuda, [620,680])
		screen.blit(creditos, [10,680])
		screen.blit(usuario,[175,175])
		#Titulo
		screen.blit(titulo, [90,10])
		#Input box
		pygame.draw.rect(screen, color, input_box, 4)
		#Renderiza el texto
		txt_surface = font.render(text, True, color_inactive)
		screen.blit(txt_surface, (input_box.x+5, input_box.y+7))
		
		pygame.display.flip()
		clock.tick(60)

	except:
		pass



sys.exit()
