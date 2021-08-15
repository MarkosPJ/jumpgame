import objects_jumpgame
import pygame

player = objects_jumpgame.Player(0,0)

floor = pygame.Rect(10,10,50,50)

cloudimg = pygame.image.load('cloud.png')

hint0 = objects_jumpgame.Hints()
hint1 = objects_jumpgame.Hints()
hint2 = objects_jumpgame.Hints()
