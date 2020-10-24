import pygame, sys

#SETUP
pygame.init()
clock = pygame.time.Clock() #en mayúsculas

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) #crear la pantalla
pygame.display.set_caption("Pong Mamalon")

#Recatangulos
ball = pygame.Rect(screen_width/2 -11,screen_height/2 -11, 22,22)
player = pygame.Rect(screen_width-20, screen_height/2 - 60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120) #coordenada 1,2, tamaño en x,y

bgcolor = (25,25,25) #RGB -> 25,25,25
objectColor = (115,115,115)

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	screen.fill(bgcolor)
	pygame.draw.rect(screen, objectColor, player) #dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #dibujar enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #dibujar pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2,screen_height)) #dibujar raya >> donde,color,inicio,final



	pygame.display.flip() #update a la pantalla
	clock.tick(60) #Framerate

#arr = [1,2,3,4,5]

#for i in arr:
#	print(i)
