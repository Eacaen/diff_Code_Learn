import random, sys, time, math, pygame
from pygame.locals import *

WINWIDTH = 640 # width of the program's window, in pixels
WINHEIGHT = 480 # height in pixels
FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRASSCOLOR = (24, 255, 0)

MOVERATE = 9
BOUNCERATE = 10	   # how fast the player bounces (large is slower)
BOUNCEHEIGHT = 30	# how high the player bounces


LEFT = 'left'
RIGHT = 'right'
def draw_static():
	global  FPSCLOCK,DISPLAYSURF, BASICFONT, L_SQUIR_IMG, R_SQUIR_IMG , E_SQUIR_IMG,GRASSIMAGES
	GRASSIMAGES = []
	L_SQUIR_IMG = pygame.image.load('squirrel.png')
	DISPLAYSURF.blit(L_SQUIR_IMG , (100,100))

	R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, False)
	DISPLAYSURF.blit(R_SQUIR_IMG , (100,150))

	R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, True, True)
	DISPLAYSURF.blit(R_SQUIR_IMG , (100,200))

	R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, False, True)
	DISPLAYSURF.blit(R_SQUIR_IMG , (100,250))

	R_SQUIR_IMG = pygame.transform.flip(L_SQUIR_IMG, False, False)
	DISPLAYSURF.blit(R_SQUIR_IMG , (100,300))

	E_SQUIR_IMG = pygame.transform.scale(L_SQUIR_IMG, (20, 20))
	DISPLAYSURF.blit(E_SQUIR_IMG , (200,100))

	E_SQUIR_IMG = pygame.transform.scale(L_SQUIR_IMG, (50, 50))
	DISPLAYSURF.blit(E_SQUIR_IMG , (200,200))

	E_SQUIR_IMG = pygame.transform.scale(L_SQUIR_IMG, (100, 100))
	DISPLAYSURF.blit(E_SQUIR_IMG , (200,300))

	E_SQUIR_IMG_Rect = E_SQUIR_IMG.get_rect()
	# print E_SQUIR_IMG_Rect.center
	pygame.draw.rect(DISPLAYSURF , RED , (200,300,100,100), 4)

	pygame.draw.rect(DISPLAYSURF , RED , (320,180,300 , 290),4 )
	for i in range(1, 5):
		GRASSIMAGES.append(pygame.image.load('grass%s.png' % i))

	for i in range(0, 4):
		DISPLAYSURF.blit(GRASSIMAGES[i] , (20 , 200+i * 50))
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
	
	

	SQUIR_IMG = pygame.image.load('squirrel.png')
	MOVE_SQUIR_IMG = pygame.transform.scale(SQUIR_IMG, (100, 100))
	Sx = 0
	Sy = 0
	playerObj = {'surface': MOVE_SQUIR_IMG,
				 'facing': LEFT,
				 'Sx' : Sx,
				 'Sy' : Sy,
				 'bounce':0,
				 }

	playerObj['Sx'] = 400
	playerObj['Sy'] = 300

	while True:
		DISPLAYSURF.fill(GRASSCOLOR)
		draw_static()

		flashIsOn = round(time.time(), 1) * 10 % 3 == 1
		if flashIsOn:
			BOUNCE_SQUIR_IMG = pygame.transform.scale(L_SQUIR_IMG, (100, 100))
			DISPLAYSURF.blit(BOUNCE_SQUIR_IMG , (300,50))

		DISPLAYSURF.blit(playerObj['surface'] , (playerObj['Sx'] , playerObj['Sy'] - \
			getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT)))

		pygame.draw.rect(DISPLAYSURF , RED , (playerObj['Sx'] , playerObj['Sy'] ,100,100), 4)

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
				print playerObj['Sx'] , playerObj['Sy']
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
			playerObj['Sx'] -= MOVERATE
		if moveRight:
			playerObj['Sx'] += MOVERATE
		if moveUp:
			playerObj['Sy'] -= MOVERATE
		if moveDown:
			playerObj['Sy'] += MOVERATE
		

		if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
			playerObj['bounce'] += 1

		if playerObj['bounce'] > BOUNCERATE:
			playerObj['bounce'] = 0 # reset bounce amount

		if playerObj['Sx'] < -5:
			playerObj['Sx'] = WINWIDTH + playerObj['Sx']
		if playerObj['Sx'] > WINWIDTH + 5:
			playerObj['Sx'] = - playerObj['Sx']	

		if playerObj['Sy'] < -5:
			playerObj['Sy'] = WINHEIGHT + playerObj['Sy']
		if playerObj['Sy'] > WINHEIGHT + 5:
			playerObj['Sy'] = - playerObj['Sy']

		pygame.display.update()
		FPSCLOCK.tick(FPS)



if __name__ == '__main__':
	main()