from engine import *

W = 1600
H = 900

def update(dt):
	pass

def render(dt):
	line(0, 0, 1600, 900, (0, 255, 0))
	pass

def onKeyDown(key):
	#if key == pygame.K_w:
	pass
	

def onKeyUp(key):
	#if key == pygame.K_w:
	pass		

initEngine(W, H)
registerKeyEvents(onKeyDown, onKeyUp)
runEngine(update, render)