import pygame
pygame.init();
height = 1600
width = 1000
gameDisplay = pygame.display.set_mode((height,width))
pygame.display.set_caption('iogame')
pygame.display.update()
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

class bullet:
	def __init__(self, direction_x,direction_y,position_x,position_y):
		self.direction_x = direction_x/20
		self.direction_y = direction_y/20
		self.position_x = int(position_x)
		self.position_y = int(position_y)
		self.stop = False
	def move(self):
		self.position_x += int(self.direction_x*3)
		self.position_y += int(self.direction_y*3)
		if (self.position_x < 0 or self.position_x > 1600 or self.position_y < 0 or self.position_y > width):
			self.stop = True

def distance(x1,y1,x2,y2):
	return math.sqrt((x1-x2)**2 +(y1-y2)**2)
#position
player1_x =  500;
player1_y = 200;
player2_x =  700;
player2_y = 200;
GameExit = False
#speed
player1_velocity_x = 0
player1_velocity_y = 0
player2_velocity_x = 0
player2_velocity_y = 0
#info of players
player1_health = 100
player2_health = 100
radius = 30
#player1 shoot , player2 run
bullet_array = []
while not GameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:#event.type來決定是哪個事件
			GameExit = True

		if event.type == pygame.KEYDOWN:#處理key events(KEY_DOWN只是一個觸發,按下的瞬間才是事件)
			if event.key == pygame.K_LEFT:
				player1_velocity_x = -3
			if event.key == pygame.K_RIGHT:
				player1_velocity_x = 3
			if event.key == pygame.K_UP:
				player1_velocity_y = -3#up is sub
			if event.key == pygame.K_DOWN:
				player1_velocity_y = 3
			if event.key == pygame.K_a:
				player2_velocity_x = -3
			if event.key == pygame.K_d:
				player2_velocity_x = 3
			if event.key == pygame.K_w:
				player2_velocity_y = -3#up is sub
			if event.key == pygame.K_s:
				player2_velocity_y = 3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				player1_velocity_x = 0;
				player1_velocity_y = 0;
			if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_w or event.key == pygame.K_s:
				player2_velocity_x = 0;
				player2_velocity_y = 0;
		if event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			bullet_array.append(bullet(mouse_x-player1_x,mouse_y-player1_y,player1_x,player1_y))
	player1_x += player1_velocity_x
	player1_y += player1_velocity_y
	player2_x += player2_velocity_x
	player2_y += player2_velocity_y
	#check if hit or not
	for e in bullet_array:
		if distance(player2_x,player2_y,e.position_x,e.position_y) < 30:
			GameExit = True
			break
		if e.stop:
			bullet_array.remove(e)
		else:
			e.move()
	#print player1,player2,bullets,background
	gameDisplay.fill(white)
	pygame.draw.circle(gameDisplay,red,[player1_x,player1_y],30)
	pygame.draw.circle(gameDisplay,blue,[player2_x,player2_y],30)
	for e in bullet_array:
		pygame.draw.circle(gameDisplay,black,[e.position_x,e.position_y],20)

	pygame.display.update()
	clock.tick(60)

pygame.quit()
quit()
