#/usr/bin/env python
#coding=utf8
# 演示了方块的遮盖，还原。方块透明度的变化，通过贪吃蛇演示了动画制作的原理
# 左键，滚轮上下方块的遮盖，还原
# 滚轮点击 方块透明度的变化
# 方向键或WASD 控制贪吃蛇移动
import random, sys, copy, os, pygame
from pygame.locals import *

FPS = 30 # frames per second to update the screen
WINWIDTH = 600 # width of the program's window, in pixels
WINHEIGHT =  400 # height in pixels

TILEWIDTH = 100
CELLSIZE = 20
COVERSPEED = 5

assert WINWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINWIDTH / CELLSIZE)
CELLHEIGHT = int(WINHEIGHT / CELLSIZE)


BRIGHTBLUE = (  0, 170, 255)
WHITE	  = (255, 255, 255)
WHITE		= (255, 255, 255)
BLACK		= (  0,   0,   0)
BRIGHTRED	= (255,   0,   0)
RED		  = (155,   0,   0)
BRIGHTGREEN  = (  0, 255,   0)
GREEN		= (  0, 155,   0)
BLUE		 = (  0,   0, 155)
BRIGHTYELLOW = (255, 255,   0)
YELLOW	   = (155, 155,   0)
DARKGRAY	 = ( 40,  40,  40)
DARKGREEN = (  0, 255,   0)

BGCOLOR = BRIGHTBLUE
TEXTCOLOR = WHITE

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
HEAD = 0 # syntactic sugar: index of the worm's head
# Set a random start point.
startx = random.randint(5, CELLWIDTH - 6)
starty = random.randint(5, CELLHEIGHT - 6)
ADD_LEN = 9

wormCoords = [{'x': startx, 'y': starty},]

for i in range(0 , ADD_LEN):
	wormCoords.append({'x': startx - i, 'y': starty})

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT , BASE_RECT_POS ,BASE_RECT , FLASH_RECT , FLASH_RECT_POS

	# Pygame initialization and basic set up of the global variables.
	pygame.init()
	FPSCLOCK = pygame.time.Clock()

	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

	pygame.display.set_caption('Puzzle Slider&Flash')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

	BASE_RECT_POS = pygame.Rect(100, 100, TILEWIDTH, TILEWIDTH)
	BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
	
	FLASH_RECT_POS = pygame.Rect(300, 100, TILEWIDTH, TILEWIDTH)
	FLASH_RECT = pygame.draw.rect(DISPLAYSURF , RED, FLASH_RECT_POS )
	drawWorm(wormCoords)
	drawGrid()
	while True: 
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		runGame()			

		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT:
				terminate()
		

def flashButtonAnimation(flashColor = RED , animationSpeed=50):

	origSurf = DISPLAYSURF.copy()
	flashSurf = pygame.Surface((TILEWIDTH, TILEWIDTH))
	flashSurf = flashSurf.convert_alpha()
	r, g, b = flashColor
	for start, end, step in ( (255, 0, -1),(0, 255, 1)): # animation loop
		for alpha in range(start, end, animationSpeed * step):
			DISPLAYSURF.blit(origSurf, (0, 0))
			flashSurf.fill((r, g, b, alpha))
			DISPLAYSURF.blit(flashSurf, (300 , 100))
			pygame.display.update()
			FPSCLOCK.tick(FPS)
	DISPLAYSURF.blit(origSurf, (0, 0))

def runGame():
	direction = RIGHT
	while True:
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT:
				terminate()

			if event.type == MOUSEBUTTONUP:
				if event.button == 1 or event.button ==5:
				 	for cover in range(100 , 0-COVERSPEED , -COVERSPEED):
				 		print cover
						COV_RECT_POS = pygame.Rect(100, 100, cover, TILEWIDTH)
						BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
						COV_RECT = pygame.draw.rect(DISPLAYSURF , WHITE, COV_RECT_POS )
						
						pygame.display.update()
						FPSCLOCK.tick(FPS)
				if event.button == 3 or event.button ==4:
			 		for cover in range(0 , 100 +COVERSPEED  , COVERSPEED):
				 		print cover
						COV_RECT_POS = pygame.Rect(100, 100 , cover , TILEWIDTH)
						BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
						COV_RECT = pygame.draw.rect(DISPLAYSURF , WHITE, COV_RECT_POS )
						
						pygame.display.update()
						FPSCLOCK.tick(FPS)

				if event.button == 2:

					DISPLAYSURF.fill(BLACK)
					BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )

					flashButtonAnimation(RED , 5)

			elif event.type == KEYDOWN:
				if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
					direction = LEFT
				elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
					direction = RIGHT
				elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
					direction = UP
				elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
					direction = DOWN
				elif event.key == K_ESCAPE:
					terminate()

		if wormCoords[HEAD]['x'] < -1:
			wormCoords[HEAD]['x'] = CELLWIDTH

		if wormCoords[HEAD]['x'] > CELLWIDTH:
			wormCoords[HEAD]['x'] = -1

		if wormCoords[HEAD]['y'] < -1:
			wormCoords[HEAD]['y'] = CELLHEIGHT
				
		if wormCoords[HEAD]['y'] > CELLHEIGHT:
			wormCoords[HEAD]['y'] = -1

		del wormCoords[-1] # remove worm's tail segment

		# move the worm by adding a segment in the direction it is moving
		if direction == UP:
			newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
		elif direction == DOWN:
			newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
		elif direction == LEFT:
			newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
		elif direction == RIGHT:
			newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}

		wormCoords.insert(0, newHead)
		DISPLAYSURF.fill(BLACK)
			
		drawWorm(wormCoords)
		drawGrid()
		BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
		FLASH_RECT = pygame.draw.rect(DISPLAYSURF , RED, FLASH_RECT_POS )
		pygame.display.update()
		FPSCLOCK.tick(5)

def drawWorm(wormCoords):
	for coord in wormCoords:
		x = coord['x'] * CELLSIZE
		y = coord['y'] * CELLSIZE
		wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
		pygame.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
		wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
		pygame.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)


def terminate():
	pygame.quit()
	sys.exit()

def drawGrid():
	for x in range(0, WINWIDTH, CELLSIZE): # draw vertical lines
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINHEIGHT))
	for y in range(0, WINHEIGHT, CELLSIZE): # draw horizontal lines
		pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINWIDTH, y))


if __name__ == '__main__':
	main()