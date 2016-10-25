from maingame import MainGame
from Window import * 

mainGame = MainGame()
mainGame.editMode()
mainGame.print()
clock = pygame.time.Clock()
loop = True
while loop:
	for e in pygame.event.get():
		if(e.type == pygame.QUIT):
			loop = False
	mainGame.turn()
	clock.tick(10)
