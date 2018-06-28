#/usr/bin/env python
#coding=utf8
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


def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT , BASE_RECT_POS ,BASE_RECT , FLASH_RECT , FLASH_RECT_POS

	# Pygame initialization and basic set up of the global variables.
	pygame.init()
	FPSCLOCK = pygame.time.Clock()

	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

	pygame.display.set_caption('Puzzle Slider&Flash')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 16)

	BASE_RECT_POS = pygame.Rect(100, 100, TILEWIDTH, TILEWIDTH)
	BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
	
	FLASH_RECT_POS = pygame.Rect(200, 100, TILEWIDTH, TILEWIDTH)
	FLASH_RECT = pygame.draw.rect(DISPLAYSURF , RED, FLASH_RECT_POS )

	# DISPLAYSURF.fill(WHITE)
	drawGrid()
	while True: 
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		runGame()			

	
def flashButtonAnimation(flashColor = RED , animationSpeed=50):

	origSurf = DISPLAYSURF.copy()

	flashSurf = pygame.Surface((TILEWIDTH, TILEWIDTH))
	flashSurf = flashSurf.convert_alpha()
	r, g, b = flashColor
	for start, end, step in ( (255, 0, -1),): # animation loop
		for alpha in range(start, end, animationSpeed * step):
			DISPLAYSURF.blit(origSurf, (0, 0))
			flashSurf.fill((r, g, b, alpha))

			DISPLAYSURF.blit(flashSurf, (200 , 100))

			pygame.display.update()
			FPSCLOCK.tick(FPS)
	DISPLAYSURF.blit(origSurf, (0, 0))

def flashButtonAnimation2(flashColor = RED , animationSpeed=50):

	origSurf = DISPLAYSURF.copy()

	flashSurf = pygame.Surface((TILEWIDTH, TILEWIDTH))
	flashSurf = flashSurf.convert_alpha()
	r, g, b = flashColor
	for start, end, step in ( (0 , 255, 1),): # animation loop
		for alpha in range(start, end, animationSpeed * step):
			DISPLAYSURF.blit(origSurf, (0, 0))
			flashSurf.fill((r, g, b, alpha))

			DISPLAYSURF.blit(flashSurf, (200 , 100))

			pygame.display.update()
			FPSCLOCK.tick(FPS)
	DISPLAYSURF.blit(origSurf, (0, 0))

def flashButtonAnimation3(flashColor = RED , animationSpeed=50):

	origSurf = DISPLAYSURF.copy()

	flashSurf = pygame.Surface((TILEWIDTH, TILEWIDTH))
	flashSurf = flashSurf.convert_alpha()
	r, g, b = flashColor
	for start, end, step in ( (0 , 255, 1),(255,0,-1)): # animation loop
		for alpha in range(start, end, animationSpeed * step):
			DISPLAYSURF.blit(origSurf, (0, 0))
			flashSurf.fill((r, g, b, alpha))

			DISPLAYSURF.blit(flashSurf, (100 , 100))

			pygame.display.update()
			FPSCLOCK.tick(FPS)
	DISPLAYSURF.blit(origSurf, (0, 0))
def runGame():
	textSurf = BASICFONT.render(' ', True, BLACK)
	textRect = textSurf.get_rect()
	textRect.center = (0, 0)

	while True:
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT  or (event.type == KEYUP and event.key == K_ESCAPE):
				terminate()

			if event.type == MOUSEBUTTONUP:
				
				if event.button == 2:

					DISPLAYSURF.fill(WHITE)
					BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )

					flashButtonAnimation(RED , 5)
					flashButtonAnimation2(BRIGHTGREEN , 5)
					# flashButtonAnimation3(BRIGHTBLUE , 5)
			if event.type == MOUSEMOTION:

				mousex, mousey = event.pos
				textSurf = BASICFONT.render(str(mousex) + ' / ' + str(mousey), True, BLACK,YELLOW)
				textRect = textSurf.get_rect()
				textRect.topright = (mousex, mousey)
						


		DISPLAYSURF.fill(WHITE)
		
		drawGrid()
		BASE_RECT = pygame.draw.rect(DISPLAYSURF , BRIGHTBLUE, BASE_RECT_POS )
		FLASH_RECT = pygame.draw.rect(DISPLAYSURF , RED, FLASH_RECT_POS )

		DISPLAYSURF.blit(textSurf, textRect)
		pygame.display.update()
		FPSCLOCK.tick(5)



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