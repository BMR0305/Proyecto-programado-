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
font = pygame.font.Font(None, 40)

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
game_over = True
while game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = False 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Menu.py")
			for entry in Entries:
				if entry.rect.collidepoint(event.pos):
					entry.active = True
					entry.color = color_active
				else:
					entry.active = False
					entry.color = color_inactive  
		if event.type == pygame.KEYDOWN:
			for entry in Entries:
				if entry.active: 
					if event.key == pygame.K_RETURN:
						print(entry.text)
						entry.text = ""
					elif event.key == pygame.K_BACKSPACE:
						entry.text = entry.text [:len(entry.text)-1]
					elif len(entry.text)>0:
						if event.key == pygame.K_BACKSPACE:
							entry.text = entry.text [:len(entry.text)-1]
						else:
							None
					elif event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9 :
						entry.text += event.unicode
		#Fondo
		screen.blit(background,[0,0])
		screen.blit(volver, [630,5])
		for entry in Entries:
			pygame.draw.rect(screen, entry.color, entry, 4)
			txt_surface = font.render(entry.text, True, color_inactive)
			screen.blit(txt_surface, (entry.rect.x+5, entry.rect.y+7))

		pygame.display.flip()
		clock.tick(60)
sys.exit()
