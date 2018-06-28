import random, sys, time, math, pygame
from pygame.locals import *

WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)
CAMERASLACK = 90
STARTSIZE = 100

FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRASSCOLOR = (24, 255, 0)
PURPLE      = (255 ,     0 , 255)

MOVERATE = 9
BOUNCERATE = 10	   # how fast the player bounces (large is slower)
BOUNCEHEIGHT = 30	# how high the player bounces


LEFT = 'left'
RIGHT = 'right'


def getBounceAmount(currentBounce , bounceRate , bounceHeight):
	return int(math.sin(math.pi / float(bounceRate) * currentBounce	) * bounceHeight)

def main():
	global  FPSCLOCK,DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG , E_SQUIR_IMG,GRASSIMAGES
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
	pygame.display.set_caption('flip and scale the img')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 32)

	moveLeft  = False
	moveRight = False
	moveUp    = False
	moveDown  = False
	
	

	SQUIR_IMG = pygame.image.load('cat.png')
	Sx = 0
	Sy = 0
	playerObj = {'surface': pygame.transform.scale(SQUIR_IMG, (STARTSIZE , STARTSIZE)),
				 'facing': LEFT,
				 'Sx' : Sx,
				 'Sy' : Sy,
				 'bounce':0,
				 'size':STARTSIZE,
				 }
	playerObj['x'] = 400
	playerObj['y'] = 300

	camerax = 0
	cameray = 0
	while True:
		DISPLAYSURF.fill(GRASSCOLOR)
	
		pos_x = playerObj['x'] -  camerax
		Bounce = getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT)
		pos_y = playerObj['y'] - Bounce - cameray

		DISPLAYSURF.blit(playerObj['surface'] , (pos_x , pos_y) )
		S_R = pygame.Rect(pos_x , pos_y ,100,100)
		pygame.draw.rect(DISPLAYSURF , RED , S_R , 4)

		E_SQUIR_IMG = pygame.transform.scale(SQUIR_IMG, (100, 100))
		DISPLAYSURF.blit(E_SQUIR_IMG , (200 -  camerax , 300 -  cameray - Bounce))

		RedRect = pygame.Rect(-50 -  camerax , -50-  cameray ,100,100)
		pygame.draw.rect(DISPLAYSURF , RED , RedRect)
		pygame.draw.rect(DISPLAYSURF , PURPLE , (-50  , -50 ,100,100))

		R1 = pygame.Rect(0 -  camerax  , 0 -  cameray ,300,  300)
		pygame.draw.rect(DISPLAYSURF , PURPLE , R1  , 4)

		if S_R.colliderect(R1):
			print 'S_R in range'
		if R1.colliderect(S_R):
			print 'R_1 in range'

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			elif event.type == KEYDOWN:
				if event.key in (K_UP, K_w):
					moveDown = False
					moveUp = True
				elif event.key in (K_DOWN, K_s):
					moveUp = False
					moveDown = True
				elif event.key in (K_LEFT, K_a):
					moveRight = False
					moveLeft = True
					if playerObj['facing'] == RIGHT:
						playerObj['surface'] = pygame.transform.flip(playerObj['surface'], True,False)
						playerObj['facing'] = LEFT
				elif event.key in (K_RIGHT, K_d):
					moveLeft = False
					moveRight = True
					if playerObj['facing'] == LEFT:
						playerObj['surface'] = pygame.transform.flip(playerObj['surface'], True,False)
						playerObj['facing'] = RIGHT

			elif event.type == KEYUP:
				print pos_x , pos_y
				# stop moving the player's squirrel
				if event.key in (K_LEFT, K_a):
					moveLeft = False
				elif event.key in (K_RIGHT, K_d):
					moveRight = False
				elif event.key in (K_UP, K_w):
					moveUp = False
				elif event.key in (K_DOWN, K_s):
					moveDown = False

		if moveLeft:
			playerObj['x'] -= MOVERATE
		if moveRight:
			playerObj['x'] += MOVERATE
		if moveUp:
			playerObj['y'] -= MOVERATE
		if moveDown:
			playerObj['y'] += MOVERATE
		

		if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
			playerObj['bounce'] += 1

		if playerObj['bounce'] > BOUNCERATE:
			playerObj['bounce'] = 0 # reset bounce amount


		
		playerCenterx = playerObj['x'] + int(playerObj['size'] / 2)
		playerCentery = playerObj['y'] + int(playerObj['size'] / 2)
		if (camerax + HALF_WINWIDTH) - playerCenterx > CAMERASLACK:
			camerax = playerCenterx + CAMERASLACK - HALF_WINWIDTH
		elif playerCenterx - (camerax + HALF_WINWIDTH) > CAMERASLACK:
			camerax = playerCenterx - CAMERASLACK - HALF_WINWIDTH
		if (cameray + HALF_WINHEIGHT) - playerCentery > CAMERASLACK:
			cameray = playerCentery + CAMERASLACK - HALF_WINHEIGHT
		elif playerCentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
			cameray = playerCentery - CAMERASLACK - HALF_WINHEIGHT

		pygame.display.update()
		FPSCLOCK.tick(FPS)



if __name__ == '__main__':
	main()