import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' 
pygame.init()
#Crear ventana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")

clock=pygame.time.Clock()

#Cargar imagnes
#Boton
volver = pygame.image.load("Imagenes/Volver.png")
volver.set_colorkey([0,0,0])
background = pygame.image.load("Imagenes/Ajustes fondo.jpg").convert()
#Clase Entry
class Entry():
	def __init__():
		self.activo = False
		self.color = color_inactive
#Entries
input_box = pygame.Rect(320, 185, 230, 40)
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = False 
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			print(mouse)
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Menu.py")
		#Fondo
		screen.blit(background,[0,0])
		screen.blit(volver, [630,5])

		pygame.draw.rect(screen, [255,255,255], input_box, 4)

		pygame.display.flip()
		clock.tick(60)