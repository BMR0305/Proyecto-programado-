import pygame, sys 
pygame.init()
#Crear vnetana
size = (720,800)
screen = pygame.display.set_mode(size)

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



while True:
	for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		 	sys.exit()
		 if event.type == pygame.MOUSEBUTTONDOWN:
		 	mouse = event.pos
		 	print(mouse)
		 	if mouse[0]>270 and mouse[0]<470 and mouse[1]>270 and mouse [1]<370: #boton jugar
		 		print("jugar")
		 	if mouse[0]>250 and mouse[0]<485 and mouse[1]>420 and mouse [1]<525: #boton ajustes 
		 		print("ajustes")
		 	if mouse[0]>635 and mouse[0]<741 and mouse[1]>695 and mouse [1]<775: #boton ayuda
		 		print("ayuda")
		 	if mouse[0]>26 and mouse[0]<295 and mouse[1]>705 and mouse [1]<790: #boton creditos 
		 		print("creditos")
	#Fondo
	screen.blit(background,[0,0])
	#Botones
	screen.blit(jugar, [250,250])
	screen.blit(ajustes, [230,400])
	screen.blit(ayuda, [620,680])
	screen.blit(creditos, [10,680])
	#Titulo
	screen.blit(titulo, [90,10])

	pygame.display.flip()
	clock.tick(60)