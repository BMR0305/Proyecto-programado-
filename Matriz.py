import pygame, sys 
pygame.init()
#Pantalla
size = (720,800)
pygame.display.set_caption("Avatars vs Rooks")
screen = pygame.display.set_mode(size)
#Reloj
clock=pygame.time.Clock()

#Fondo
matriz = pygame.image.load("Imagenes/Matriz.jpg").convert()
#Imagenes del arquero
ataque1a = pygame.image.load("Imagenes/Arquero/Ataque1.png").convert()
ataque1a.set_colorkey([0,0,0])
ataque2a = pygame.image.load("Imagenes/Arquero/Ataque2.png").convert()
ataque2a.set_colorkey([0,0,0])
ataque3a = pygame.image.load("Imagenes/Arquero/Ataque3.png").convert()
ataque3a.set_colorkey([0,0,0])
ataque4a = pygame.image.load("Imagenes/Arquero/Ataque4.png").convert()
ataque4a.set_colorkey([0,0,0])
caminar1a = pygame.image.load("Imagenes/Arquero/Caminar1.png").convert()
caminar1a.set_colorkey([0,0,0])
caminar2a = pygame.image.load("Imagenes/Arquero/Caminar2.png").convert()
caminar2a.set_colorkey([0,0,0])
caminar3a = pygame.image.load("Imagenes/Arquero/Caminar3.png").convert()
caminar3a.set_colorkey([0,0,0])
caminar4a = pygame.image.load("Imagenes/Arquero/Caminar4.png").convert()
caminar4a.set_colorkey([0,0,0])
caminar5a = pygame.image.load("Imagenes/Arquero/Caminar5.png").convert()
caminar5a.set_colorkey([0,0,0])
caminar6a = pygame.image.load("Imagenes/Arquero/Caminar6.png").convert()
caminar6a.set_colorkey([0,0,0])
caminar7a = pygame.image.load("Imagenes/Arquero/Caminar7.png").convert()
caminar7a.set_colorkey([0,0,0])
dañoa = pygame.image.load("Imagenes/Arquero/Daño.png").convert()
dañoa.set_colorkey([0,0,0])
muertea = pygame.image.load("Imagenes/Arquero/Muerte.png").convert()
muertea.set_colorkey([0,0,0])

#Imagenes del escudero
ataque1e = pygame.image.load("Imagenes/Escudero/Ataque1.png").convert()
ataque1e.set_colorkey([0,0,0])
ataque2e = pygame.image.load("Imagenes/Escudero/Ataque2.png").convert()
ataque2e.set_colorkey([0,0,0])
ataque3e = pygame.image.load("Imagenes/Escudero/Ataque3.png").convert()
ataque3e.set_colorkey([0,0,0])
ataque4e = pygame.image.load("Imagenes/Escudero/Ataque4.png").convert()
ataque4e.set_colorkey([0,0,0])
caminar1e = pygame.image.load("Imagenes/Escudero/Caminar1.png").convert()
caminar1e.set_colorkey([0,0,0])
caminar2e = pygame.image.load("Imagenes/Escudero/Caminar2.png").convert()
caminar2e.set_colorkey([0,0,0])
caminar3e = pygame.image.load("Imagenes/Escudero/Caminar3.png").convert()
caminar3e.set_colorkey([0,0,0])
caminar4e = pygame.image.load("Imagenes/Escudero/Caminar4.png").convert()
caminar4e.set_colorkey([0,0,0])
caminar5e = pygame.image.load("Imagenes/Escudero/Caminar5.png").convert()
caminar5e.set_colorkey([0,0,0])
caminar6e = pygame.image.load("Imagenes/Escudero/Caminar6.png").convert()
caminar6e.set_colorkey([0,0,0])
caminar7e = pygame.image.load("Imagenes/Escudero/Caminar7.png").convert()
caminar7e.set_colorkey([0,0,0])
dañoe = pygame.image.load("Imagenes/Escudero/Daño.png").convert()
dañoe.set_colorkey([0,0,0])
muertee = pygame.image.load("Imagenes/Escudero/Muerte.png").convert()
muertee.set_colorkey([0,0,0])

#Imagenes del hachero
ataque1h = pygame.image.load("Imagenes/Hacha/Ataque1.png").convert()
ataque1h.set_colorkey([0,0,0])
ataque2h = pygame.image.load("Imagenes/Hacha/Ataque2.png").convert()
ataque2h.set_colorkey([0,0,0])
ataque3h = pygame.image.load("Imagenes/Hacha/Ataque3.png").convert()
ataque3h.set_colorkey([0,0,0])
ataque4h = pygame.image.load("Imagenes/Hacha/Ataque4.png").convert()
ataque4h.set_colorkey([0,0,0])
caminar1h = pygame.image.load("Imagenes/Hacha/Caminar1.png").convert()
caminar1h.set_colorkey([0,0,0])
caminar2h = pygame.image.load("Imagenes/Hacha/Caminar2.png").convert()
caminar2h.set_colorkey([0,0,0])
caminar3h = pygame.image.load("Imagenes/Hacha/Caminar3.png").convert()
caminar3h.set_colorkey([0,0,0])
caminar4h = pygame.image.load("Imagenes/Hacha/Caminar4.png").convert()
caminar4h.set_colorkey([0,0,0])
caminar5h = pygame.image.load("Imagenes/Hacha/Caminar5.png").convert()
caminar5h.set_colorkey([0,0,0])
caminar6h = pygame.image.load("Imagenes/Hacha/Caminar6.png").convert()
caminar6h.set_colorkey([0,0,0])
caminar7h = pygame.image.load("Imagenes/Hacha/Caminar7.png").convert()
caminar7h.set_colorkey([0,0,0])
dañoh = pygame.image.load("Imagenes/Hacha/Daño.png").convert()
dañoh.set_colorkey([0,0,0])
muerteh = pygame.image.load("Imagenes/Hacha/Muerte.png").convert()
muerteh.set_colorkey([0,0,0])

#Imagenes del avatar con maza
ataque1m = pygame.image.load("Imagenes/Maza/Ataque1.png").convert()
ataque1m.set_colorkey([0,0,0])
ataque2m = pygame.image.load("Imagenes/Maza/Ataque2.png").convert()
ataque2m.set_colorkey([0,0,0])
ataque3m = pygame.image.load("Imagenes/Maza/Ataque3.png").convert()
ataque3m.set_colorkey([0,0,0])
ataque4m = pygame.image.load("Imagenes/Maza/Ataque4.png").convert()
ataque4m.set_colorkey([0,0,0])
caminar1m = pygame.image.load("Imagenes/Maza/Caminar1.png").convert()
caminar1m.set_colorkey([0,0,0])
caminar2m = pygame.image.load("Imagenes/Maza/Caminar2.png").convert()
caminar2m.set_colorkey([0,0,0])
caminar3m = pygame.image.load("Imagenes/Maza/Caminar3.png").convert()
caminar3m.set_colorkey([0,0,0])
caminar4m = pygame.image.load("Imagenes/Maza/Caminar4.png").convert()
caminar4m.set_colorkey([0,0,0])
caminar5m = pygame.image.load("Imagenes/Maza/Caminar5.png").convert()
caminar5m.set_colorkey([0,0,0])
caminar6m = pygame.image.load("Imagenes/Maza/Caminar6.png").convert()
caminar6m.set_colorkey([0,0,0])
caminar7m = pygame.image.load("Imagenes/Maza/Caminar7.png").convert()
caminar7m.set_colorkey([0,0,0])
dañom = pygame.image.load("Imagenes/Maza/Daño.png").convert()
dañom.set_colorkey([0,0,0])
muertem = pygame.image.load("Imagenes/Maza/Muerte.png").convert()
muertem.set_colorkey([0,0,0])

class Arquero(pygame.sprite.Sprite):
    def __init__(self, position):
            super().__init__()
            self.image = caminar1a
            self.rect = self.image.get_rect()
            self.rect.topleft = position
            self.frame = 0
            self.caminar = [caminar1a, caminar2a, caminar3a, caminar4a, caminar5a, caminar6a, caminar7a]
            self.ataque = [ataque1a, ataque2a, ataque3a, ataque4a] 
            self.muerte = muertea
            self.daño = dañoa

    def get_frame(self, frame_set):
    	self.frame += 1
    	if self.frame > (len(frame_set) - 1):
        	self.frame = 0
    	return frame_set[self.frame]
    
    def change_image(self, lista):
            if isinstance (lista, list):
                self.image = self.get_frame(lista)
            else:
            	None

    def update(self, direction):
        if direction == 'up':
            self.change_image(self.caminar)
            self.rect.y -= 5

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.update('up')


arquero = Arquero((185,800))

while True:
        for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                        sys.exit()
        arquero.handle_event(event)
        screen.blit(matriz,[0,0])
        screen.blit(arquero.image, arquero.rect)
        pygame.display.flip()
        clock.tick(20) 
