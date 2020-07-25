import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' 
pygame.init()
#Crear ventana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")

clock=pygame.time.Clock()

#Boton
background = pygame.image.load("Imagenes/Tutorial.jpg").convert()
#Bucle principal
while True:
	#captura de eventos
	for event in pygame.event.get():
		#salir de juego
		if event.type == pygame.QUIT:
			sys.exit() 
		#deteccion del mouse
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			#detección para volver al menu
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Avatars_vs_Rook.py")
	try:
		#renderizado del fondo
		screen.blit(background,[0,0])
		#actualizacción de
		pygame.display.flip()
		clock.tick(60)
	except:
		pass
