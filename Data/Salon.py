import pygame, sys, os
os.environ['SDL_VIDEO_CENTERED'] = '50' 
pygame.init()
#Crear ventana
size = (720,800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Avatar vs Rooks")

clock=pygame.time.Clock()
#Fuente
font = pygame.font.SysFont("Papyrus", 30)
#Boton
volver = pygame.image.load("Imagenes/Volver.png")
volver.set_colorkey([0,0,0])
#Fondo
background = pygame.image.load("Imagenes/Fama.jpg").convert()
#Txt
records = open("Records.txt", "r")
#Lista del podio
final = records.readlines()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit() 
		if event.type == pygame.MOUSEBUTTONDOWN: 
			mouse = event.pos
			print (mouse)
			if mouse[0]>640 and mouse[0]<706 and mouse[1]>12 and mouse [1]<65: #Boton volver
				pygame.quit()
				os.system("Menu.py")
	try:
		screen.blit(background,[0,0])
		screen.blit(volver, [630,5])

		puesto1 = font.render(final[0][:len(final[0])-1], True,[0,0,0])
		screen.blit(puesto1, (157,100))
		puesto1_tiempo = font.render("Tiempo:"+final[1][:3]+"s", True,[0,0,0])
		screen.blit(puesto1_tiempo, (180,210))

		puesto2 = font.render(final[2][:len(final[2])-1], True,[0,0,0])
		screen.blit(puesto2, (420,130))
		puesto2_tiempo = font.render("Tiempo:"+final[3][:3]+"s", True,[0,0,0])
		screen.blit(puesto2_tiempo, (440,285))

		puesto3 = font.render(final[4][:len(final[4])-1], True,[0,0,0])
		screen.blit(puesto3, (85,425))
		puesto3_tiempo = font.render("Tiempo:"+final[5][:3]+"s", True,[0,0,0])
		screen.blit(puesto3_tiempo, (120,590))

		puesto4 = font.render(final[6][:len(final[6])-1], True,[0,0,0])
		screen.blit(puesto4, (415,355))
		puesto4_tiempo = font.render("Tiempo:"+final[7][:3]+"s", True,[0,0,0])
		screen.blit(puesto4_tiempo, (490,490))

		puesto5 = font.render(final[8][:len(final[8])-1], True,[0,0,0])
		screen.blit(puesto5, (380,570))
		puesto5_tiempo = font.render("Tiempo:"+final[9][:3]+"s", True,[0,0,0])
		screen.blit(puesto5_tiempo, (462,723))

		pygame.display.flip()
		clock.tick(60)
	except:
		pass
