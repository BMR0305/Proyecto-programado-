import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' #se centra la ventana de juego
pygame.init()
#Crear vnetana
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avdvice Machine")
#Reloj
clock=pygame.time.Clock()
#Fondos
background = pygame.image.load("Imagenes/Menu.jpg").convert()
#Variables de entry
active = False
text = ""
font = pygame.font.Font(None, 40)
color_inactive = pygame.Color(255,255,255)
color_active = pygame.Color(155,155,155)
color = color_inactive
input_box = pygame.Rect(320, 185, 230, 40)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:  
			sys.exit()
	#Input box
	pygame.draw.rect(screen, color, input_box, 4)
	#Renderiza el texto
	txt_surface = font.render(text, True, color_inactive)
	screen.blit(txt_surface, (input_box.x+5, input_box.y+7))

	#Renderiza el fondo
	screen.blit(background,[0,0])

	pygame.display.flip()
	clock.tick(60)