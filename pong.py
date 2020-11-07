import pygame, sys, random

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
	if ball.colliderect(player) or ball.colliderect(enemy):
		ball_speed_x *= -1
	if ball.left <= 0 or ball.right >= screen_width:
		#goal
		goal()


def player_animation():
	global player_speed
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height



def enemy_animation():
	global enemy_speed
	enemy.y += enemy_speed
	if enemy.top <= 0:
		enemy.top = 0

	if enemy.bottom >= screen_height:
		enemy.bottom = screen_height

def goal():
	global ball_speed_x, ball_speed_y, score_player, score_enemy
	if  ball.x < screen_width/2: 
		score_player += 1
	else:
		score_enemy += 1

	ball.center = (screen_width/2 , screen_height/2) 
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))
	if score_enemy >= 5 or score_player >= 5:
		pygame.exit()
		sys.exit()


screen_width = 1080
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height)) #crear la pantalla
pygame.display.set_caption("Pong Mamalon")

game_font = pygame.font.SysFont("comicsansms", 30)

#Recatangulos
ball = pygame.Rect(screen_width/2 -11,screen_height/2 -11, 22,22)
player = pygame.Rect(screen_width-20, screen_height/2 - 60, 10, 120)
enemy = pygame.Rect(10, screen_height/2 -60, 10, 120) #coordenada 1,2, tamaño en x,y

ball_speed_x = 5
ball_speed_y = 5
player_speed = 0
enemy_speed = 0
score_player = 0
score_enemy = 0
player_step = 3
enemy_step = 3

bgcolor = (25,25,25) #RGB -> 25,25,25
objectColor = (115,115,115)
fontColor = (100,100,100)
#LOOP
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	 	#eventos de teclado
		if event.type == pygame.KEYDOWN:#cuando se presiona la tecla
	 		if event.key == pygame.K_DOWN:
	 			player_speed += player_step
	 		if event.key == pygame.K_UP:
	 			player_speed -= player_step
	 		if event.key == pygame.K_s:
	 			enemy_speed += enemy_step
	 		if event.key == pygame.K_w:
	 			enemy_speed -= enemy_step
	 			#soltar
	    
		if event.type == pygame.KEYUP:
	 		if event.key == pygame.K_DOWN:
	 			player_speed -= player_step

	 		if event.key == pygame.K_UP:
	 			player_speed += player_step

	 		if event.key == pygame.K_s:
	 			enemy_speed -= enemy_step

	 		if event.key == pygame.K_w:
	 			enemy_speed += enemy_step


	screen.fill(bgcolor)
	pygame.draw.rect(screen, objectColor, player) #dibujar player
	pygame.draw.rect(screen, objectColor, enemy) #dibujar enemigo
	pygame.draw.ellipse(screen, objectColor, ball) #dibujar pelota
	pygame.draw.aaline(screen, objectColor, (screen_width/2,0), (screen_width/2,screen_height)) #dibujar raya >> dónde,color,inicio,final
	ball_animation()
	player_animation()
	enemy_animation()
	player_text = game_font.render(f"{score_player}", False, fontColor)
	enemy_text = game_font.render(f"{score_enemy}", False, fontColor)
	screen.blit(player_text, (screen_width/2 + 30, 10))
	screen.blit(enemy_text, (screen_width/2 - 50, 10))

	pygame.display.flip() #update a la pantalla
	clock.tick(60) #Framerate

#arr = [1,2,3,4,5]

#for i in arr:
#	print(i)
