# -*- coding: utf-8 -*-
import random, sys, copy, os, pygame
from pygame.locals import *
FPS = 30 # frames per second to update the screen
WINWIDTH = 800 # width of the program's window, in pixels
WINHEIGHT = 600 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 50
TILEHEIGHT = 85
TILEFLOORHEIGHT = 40

BRIGHTBLUE = (  0, 170, 255)
WHITE	  = (255, 255, 255)
BGCOLOR = BRIGHTBLUE

def readLevelsFile(filename):
	assert os.path.exists(filename)
	mapFile = open(filename , 'r')
	content = mapFile.readlines( ) + ['\r\n'] #另外再加一行 ['\r\n']
	mapFile.close()

	# print content 
	levels = []
	levelNum = 0
	mapTextLines = []
	mapObj = []


	for lineNum in range(len(content)):
		line = content[lineNum].rstrip('\r\n')
		if ';' in line:
			line = line[:line.find(';')]

		if line != '':
			mapTextLines.append(line)

		#一关结束了，整理该关地图
		elif line == '' and len(mapTextLines) > 0:
			maxWidth = -1
			for i in range(len(mapTextLines)):
				if len(mapTextLines[i]) > maxWidth:
					maxWidth = len(mapTextLines[i])

			for i in range(len(mapTextLines)):
				mapTextLines[i] += ' ' * (maxWidth - len(mapTextLines[i]))

			for x in range(len(mapTextLines[0])):
				mapObj.append([])
			for y in range(len(mapTextLines)):
				for x in range(maxWidth):
					mapObj[x].append(mapTextLines[y][x])

			startx = None # The x and y for the player's starting position
			starty = None
			goals = [] # list of (x, y) tuples for each goal.
			stars = [] # list of (x, y) for each star's starting position.

			# print maxWidth
			for x in range(maxWidth):
				for y in range(len(mapObj[x])):
					if mapObj[x][y] in ('@', '+'):
						# '@' is player, '+' is player & goal
						startx = x
						starty = y
					if mapObj[x][y] in ('.', '+', '*'):
						# '.' is goal, '*' is star & goal
						goals.append((x, y))
					if mapObj[x][y] in ('$', '*'):
						# '$' is star
						stars.append((x, y))
			assert startx != None and starty != None, 'Level %s (around line %s) in %s is missing a "@" or "+" to mark the start point.' % (levelNum+1, lineNum, filename)
			assert len(goals) > 0, 'Level %s (around line %s) in %s must have at least one goal.' % (levelNum+1, lineNum, filename)
			assert len(stars) >= len(goals), 'Level %s (around line %s) in %s is impossible to solve. It has %s goals but only %s stars.' % (levelNum+1, lineNum, filename, len(goals), len(stars))

			# Create level object and starting game state object.
			gameStateObj = {'player': (startx, starty),
					'stepCounter': 0,
					'stars': stars}

			levelObj = {'width': maxWidth,
				'height': len(mapObj),
				'mapObj': mapObj,
				'goals': goals,
				'startState': gameStateObj}

			levels.append(levelObj)

			# Reset the variables for reading the next map.
			mapTextLines = []
			mapObj = []
			gameStateObj = {}
			levelNum += 1
	return levels

def main():
	global FPSCLOCK, DISPLAYSURF, IMAGESDICT, TILEMAPPING, OUTSIDEDECOMAPPING, BASICFONT, PLAYERIMAGES, currentImage

	# Pygame initialization and basic set up of the global variables.
	pygame.init()
	FPSCLOCK = pygame.time.Clock()

	# Because the Surface object stored in DISPLAYSURF was returned
	# from the pygame.display.set_mode() function, this is the
	# Surface object that is drawn to the actual computer screen
	# when pygame.display.update() is called.
	DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

	pygame.display.set_caption('Star Pusher')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

	# A global dict value that will contain all the Pygame
	# Surface objects returned by pygame.image.load().
	IMAGESDICT = {'uncovered goal': pygame.image.load('RedSelector.png'),
				  'covered goal': pygame.image.load('Selector.png'),
				  'star': pygame.image.load('Star.png'),
				  'corner': pygame.image.load('Wall_Block_Tall.png'),
				  'wall': pygame.image.load('Wood_Block_Tall.png'),
				  'inside floor': pygame.image.load('Plain_Block.png'),
				  'outside floor': pygame.image.load('Grass_Block.png'),
				  'title': pygame.image.load('star_title.png'),
				  'solved': pygame.image.load('star_solved.png'),
				  'princess': pygame.image.load('princess.png'),
				  'boy': pygame.image.load('boy.png'),
				  'catgirl': pygame.image.load('catgirl.png'),
				  'horngirl': pygame.image.load('horngirl.png'),
				  'pinkgirl': pygame.image.load('pinkgirl.png'),
				  'rock': pygame.image.load('Rock.png'),
				  'short tree': pygame.image.load('Tree_Short.png'),
				  'tall tree': pygame.image.load('Tree_Tall.png'),
				  'ugly tree': pygame.image.load('Tree_Ugly.png')}

	# These dict values are global, and map the character that appears
	# in the level file to the Surface object it represents.
	TILEMAPPING = {'x': IMAGESDICT['corner'],
				   '#': IMAGESDICT['wall'],
				   'o': IMAGESDICT['inside floor'],
				   ' ': IMAGESDICT['outside floor']}
	OUTSIDEDECOMAPPING = {'1': IMAGESDICT['rock'],
						  '2': IMAGESDICT['short tree'],
						  '3': IMAGESDICT['tall tree'],
						  '4': IMAGESDICT['ugly tree']}


	currentImage = 0
	PLAYERIMAGES = [IMAGESDICT['princess'],
					IMAGESDICT['boy'],
					IMAGESDICT['catgirl'],
					IMAGESDICT['horngirl'],
					IMAGESDICT['pinkgirl']]


	levels = readLevelsFile('starPusherLevels.txt')
	levelNum = 0


	while True: 

		levelObj = levels[levelNum]
		mapObj = levelObj['mapObj']
		gameStateObj = copy.deepcopy(levelObj['startState'])
		mapSurf = drawMap(mapObj, gameStateObj, levelObj['goals'])

		mapSurfRect = mapSurf.get_rect()
		mapSurfRect.center = (HALF_WINWIDTH , HALF_WINHEIGHT )

		DISPLAYSURF.fill(BGCOLOR)
		DISPLAYSURF.blit(mapSurf, mapSurfRect)

		for event in pygame.event.get(): # event handling loop
			if event.type == MOUSEBUTTONUP:
				if event.button == 1 or event.button ==5:
					levelNum += 1
				if event.button == 3 or event.button ==4:
					levelNum -= 1
				print levelNum
				currentImage = levelNum % 4
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		FPSCLOCK.tick()



def drawMap(mapObj, gameStateObj, goals):
	"""Draws the map to a Surface object, including the player and
	stars. This function does not call pygame.display.update(), nor
	does it draw the "Level" and "Steps" text in the corner."""

	# mapSurf will be the single Surface object that the tiles are drawn
	# on, so that it is easy to position the entire map on the DISPLAYSURF
	# Surface object. First, the width and height must be calculated.
	mapSurfWidth = len(mapObj) * TILEWIDTH
	mapSurfHeight = (len(mapObj[0]) - 1) * TILEFLOORHEIGHT + TILEHEIGHT
	mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
	mapSurf.fill(BGCOLOR) # start with a blank color on the surface.

	# Draw the tile sprites onto this surface.
	for x in range(len(mapObj)):
		for y in range(len(mapObj[x])):
			spaceRect = pygame.Rect((x * TILEWIDTH, y * TILEFLOORHEIGHT, TILEWIDTH, TILEHEIGHT))
			if mapObj[x][y] in TILEMAPPING:
				baseTile = TILEMAPPING[mapObj[x][y]]
			elif mapObj[x][y] in OUTSIDEDECOMAPPING:
				baseTile = TILEMAPPING[' ']

			# First draw the base ground/wall tile.
			mapSurf.blit(baseTile, spaceRect)

			if mapObj[x][y] in OUTSIDEDECOMAPPING:
				# Draw any tree/rock decorations that are on this tile.
				mapSurf.blit(OUTSIDEDECOMAPPING[mapObj[x][y]], spaceRect)
			elif (x, y) in gameStateObj['stars']:
				if (x, y) in goals:
					# A goal AND star are on this space, draw goal first.
					mapSurf.blit(IMAGESDICT['covered goal'], spaceRect)
				# Then draw the star sprite.
				mapSurf.blit(IMAGESDICT['star'], spaceRect)
			elif (x, y) in goals:
				# Draw a goal without a star on it.
				mapSurf.blit(IMAGESDICT['uncovered goal'], spaceRect)

			# Last draw the player on the board.
			if (x, y) == gameStateObj['player']:
				# Note: The value "currentImage" refers
				# to a key in "PLAYERIMAGES" which has the
				# specific player image we want to show.
				mapSurf.blit(PLAYERIMAGES[currentImage], spaceRect)

	return mapSurf

		

if __name__ == '__main__':
	# levels = readLevelsFile('starPusherLevels.txt')
	# print levels[0]
	main()
