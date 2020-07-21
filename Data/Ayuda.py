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

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Menu.py")
	try:
		screen.blit(background,[0,0])

		pygame.display.flip()
		clock.tick(60)
	except:
		pass
