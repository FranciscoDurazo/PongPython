import pygame, sys

#SETUP
pygame.init()
clock = pygame.time.Clock() #en mayúsculas

#como crear una función en python 
def ball_animation ():
	#definir que se usan de manera global esas variables
	global ball_speed_x, ball_speed_y
	ball.x += ball_speed_x
	ball.y += ball_speed_y
	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y  *= -1

def player_animation():
	global player_speed
	player.y += player_speed
	if player.top <= 0:
		player.top = 0

	if player.bottom >= screen_height:
		player.bottom = screen_height

def enemy_animation():
	global enemy_speed
	enemy.y += player_speed
	if enemy.top <= 0:
		enemy.top = 0

	if enemy.bottom >= screen_height:
		enemy.bottom = screen_height

screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) #crear la pantalla
pygame.display.set_caption("Pong Mamalon")

#Recatangulos
ball = pygame.Rect(screen_width/2 -11,screen_height/2 -11, 22,22)
player = pygame.Rect(screen_width-20, screen_height/2 - 60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120) #coordenada 1,2, tamaño en x,y

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
enemy_speed = 0
bgcolor = (25,25,25) #RGB -> 25,25,25
objectColor = (115,115,115)

#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	 	#eventos de teclado
		if event.type == pygame.KEYDOWN: #cuando se presiona la tecla
	 		if event.key == pygame.K_DOWN:
	 			player_speed += 3
	 		if event.key == pygame.K_UP:
	 			player_speed -= 3
	 		if event.key == pygme.K_s:
	 			enemy_speed += 3
	 		if event.key == pygame.K_w:
	 			enemy_speed -= 3
	 			#soltar
	    if event.type == pygame.KEYUP:
	 		if event.key == pygame.K_DOWN:
	 			player_speed -= 3

	 		if event.key == pygame.K_UP:
	 			player_speed += 3

	 		if event.key == pygame.K_s:
	 			player_speed -= 3

	 		if event.key == pygame.K_w:
	 			player_speed += 3


	screen.fill(bgcolor)
	pygame.draw.rect(screen, objectColor, player) #dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #dibujar enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #dibujar pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2,screen_height)) #dibujar raya >> dónde,color,inicio,final
	ball_animation()
	player_animation()
	enemy_animation()



	pygame.display.flip() #update a la pantalla
	clock.tick(60) #Framerate

#arr = [1,2,3,4,5]

#for i in arr:
#	print(i)
