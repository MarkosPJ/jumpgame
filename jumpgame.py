import pygame
import objects_jumpgame
from jumpgame_data import *

 
def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pygame-Tutorial: Grundlagen")
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 30)
 
    clock = pygame.time.Clock()

    running = True
    floor1 = pygame.Rect(0, 500, 800, 100)
    count = 0
    while running:
        # Background
        screen.blit(pygame.transform.scale(cloudimg,(800,500)),(0,0))
        
        player1 = pygame.Rect(200, player.y_pos + 440, 25, 60)
        hint_0 = pygame.Rect(hint0.x_pos, 500 - hint0.height,\
                             hint0.width, hint0.height)
        hint_1 = pygame.Rect(hint1.x_pos, 500 - hint1.height,\
                             hint1.width, hint1.height)
        hint_2 = pygame.Rect(hint2.x_pos, 500 - hint2.height,\
                             hint2.width, hint2.height)
        
        
        clock.tick(30)
 
        #screen.fill((0, 0, 0))
        pygame.draw.rect(screen,(255,255,0),floor1)  # The floor.
        pygame.draw.rect(screen,(0,0,0),player1)  # The player.
        pygame.draw.rect(screen,(255,0,0),hint_0)  # The one hint.
        pygame.draw.rect(screen,(255,0,0),hint_1)  # The other hint.
        pygame.draw.rect(screen,(255,0,0),hint_2)  # The next hint.


        #execute movement (of the player and of the hints)
        player.move()
        hint0.approach()
        print(hint0.collide(player))
        if hint0.collide(player):  # Gegen Hindernis gestoßen.
            break
        hint1.approach()
        print(hint1.collide(player))
        if hint1.collide(player):  # Gegen Hindernis gestoßen.
            break
        hint2.approach()
        print(hint2.collide(player))
        if hint2.collide(player):  # Gegen Hindernis gestoßen.
            break
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))

                if event.key == pygame.K_w:
                    #jump
                    if player.isOnFloor():
                        player.jump()
 
        
        print("y_pos =",player.y_pos)

        pygame.display.flip()
 
 
if __name__ == '__main__':
    main()




#if not pygame.font: print('Fehler pygame.font Modul konnte nicht geladen werden!')
#if not pygame.mixer: print('Fehler pygame.mixer Modul konnte nicht geladen werden!')
