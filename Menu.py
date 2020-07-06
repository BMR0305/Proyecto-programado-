import pygame, sys 
pygame.init()

size = (720,960)
screen = pygame.display.set_mode(size)
clock=pygame.time.Clock()

background = pygame.image.load("Imagenes/Menu.jpg").convert()
while True:
	for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		 	sys.exit()

	screen.blit(background,[0,0])

	pygame.display.flip()
	clock.tick(60)