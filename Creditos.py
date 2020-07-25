import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' #se centra la ventana de juego
pygame.init()
#Crear ventana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")
#Reloj
clock=pygame.time.Clock()
#Fondo
background = pygame.image.load("Imagenes/Creditos.jpg").convert()
#Boton
volver = pygame.image.load("Imagenes/Volver.png")
volver.set_colorkey([0,0,0])
#Bucle principal
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			if mouse[0]>14 and mouse[0]<81 and mouse[1]>734 and mouse [1]<783: #Boton volver, regresa al menú
				pygame.quit()
				os.system("Avatars_vs_Rook.py")
	try:
		#Renderizado de fondo
		screen.blit(background,[0,0])
		screen.blit(volver,[5,725])

		pygame.display.flip()
		clock.tick(60)
	except:
		pass