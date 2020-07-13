import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' 
pygame.init()
#Crear ventana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")

clock=pygame.time.Clock()

#Cargar imagenes
#Boton
volver = pygame.image.load("Imagenes/Volver.png")
volver.set_colorkey([0,0,0])
background = pygame.image.load("Imagenes/Ajustes fondo.jpg").convert()
#color entry
color_inactive = pygame.Color(255,255,255)
color_active = pygame.Color(155,155,155)
#Clase Entry
class Entry():
	def __init__(self,rect):
		self.active = False
		self.color = color_inactive
		self.text = ""
		self.rect = pygame.Rect(rect)

#Entries
cadencia_rooks = Entry([339, 200, 80, 40])
cadencia_arquero = Entry([178, 460, 80, 40])
cadencia_escudero = Entry([548, 459, 80, 40])
cadencia_hacha = Entry([178, 700, 80, 40])
cadencia_maza = Entry([548, 700, 80, 40])
velocidad_arquero = Entry([178, 394, 80, 40])
velocidad_escudero = Entry([548, 389, 80, 40])
velocidad_hacha = Entry([178, 628, 80, 40])
velocidad_maza = Entry([548, 625, 80, 40])
Entries = [cadencia_rooks,cadencia_arquero,cadencia_escudero,cadencia_hacha,cadencia_maza,velocidad_arquero,velocidad_escudero,velocidad_hacha,velocidad_maza]
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = False 
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Menu.py")
			if mouse[0]>339 and mouse[0]<390 and mouse[1]>200 and mouse [1]<240:
				cadencia_rooks.active = True
				cadencia_rooks.color = color_active
			else:
				cadencia_rooks.active = False
				cadencia_rooks.color = color_inactive 
		#Fondo
		screen.blit(background,[0,0])
		screen.blit(volver, [630,5])
		for entry in Entries:
			pygame.draw.rect(screen, [255,255,255], entry, 4)

		pygame.display.flip()
		clock.tick(60)
