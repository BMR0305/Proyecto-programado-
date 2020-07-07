import pygame, sys 
pygame.init()

size = (720,800)
pygame.display.set_caption("Avatars vs Rooks")
screen = pygame.display.set_mode(size)

clock=pygame.time.Clock()

matriz = pygame.image.load("Imagenes/Matriz.jpg").convert()
D = pygame.image.load("Imagenes/D.png").convert()
D.set_colorkey([0,0,0])
while True:
	for event in pygame.event.get():
		 if event.type == pygame.QUIT:
		 	sys.exit()
	screen.blit(matriz,[0,0])
	screen.blit(D,[140,140])
	pygame.display.flip()
	clock.tick(60) 