# Example file showing a circle moving on screen
import pygame
from Cursor import Cursor, Projectile
from Snake import Snake
FIRE_RATE = 10
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))

clock = pygame.time.Clock()
running = True
dt = 0


player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# initialize the player character
player = Cursor(screen, 300, 300)
# proj = Projectile(screen, player.shoot())

snake = Snake(screen, (200,200))


#########################################################################################################
# Main loop starts here
#
#
#
#
#
#####################################################################################################
proj_list = []
shot_fired = False
frames = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("White")




    # this is used to control the imputs from the player
    player_pos = [player.get_posx(), player.get_posy()]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and (player_pos[1]>0):
        player.move_up()
    if keys[pygame.K_DOWN] and (player_pos[1]<screen.get_height()):
        player.move_down()
    if keys[pygame.K_LEFT] and (player_pos[0]>0):
        player.move_left()
    if keys[pygame.K_RIGHT] and (player_pos[0]<screen.get_width()):
        player.move_right()
    if keys[pygame.K_SPACE]:
        # create projectile object and set shot fired flag to true so that we can start drawing the projectiles.
        # we do not create the object before this because we do not want it to appear on screen until space key has been placed
        # object could have been initialized and hidden in the beginning if we set it's starting position to off the screen, but then we would be stuck with a single projectile object

        # if statement below is to slow down the rate of fire so that it is not a constart steam
        if frames >= FIRE_RATE:
            proj_list.append(Projectile(screen, [player.get_posx()-player.get_width()/2.5, player.get_posy()-10]))
            shot_fired = True
            frames = 0


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and (player_pos[1]>0):
        snake.move_up()

    if keys[pygame.K_s] and (player_pos[1]<screen.get_height()):
        snake.move_down()
        snake.add_body_segment()
    if keys[pygame.K_a] and (player_pos[0]>0):
        snake.move_left()
    if keys[pygame.K_d] and (player_pos[0]<screen.get_width()):
        snake.move_right()
        snake.delete_body_segment()


    frames += 1
    # we only want to draw the pojectiles when the "fire" command key has been pressed
    # when a projectile has reached its maximum distance it will inform main it is ready for deletion
    if shot_fired == True:
        for item in proj_list:
            if item.draw_projectile() == "delete":
                proj_list.remove(item)
                del item


    # the player's character has to be drawn onto the screen every frame otherwise it will never appear or move
    player.draw()

    snake.draw()

    # flip() the display to put your work on screen

    pygame.display.flip()


    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30)


pygame.quit()