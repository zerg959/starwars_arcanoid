from time import sleep

import pygame

from arcanoid_classes import Picture

pygame.init()

back = (200, 255, 255)  # background color
mw = pygame.display.set_mode((500, 500))  # main window
mw.fill(back)
clock = pygame.time.Clock()

# platform coordinates
racket_x = 200
racket_y = 330
# ---------------------------------------------------------
# ball moving variables
ball_x = 3
ball_y = 3
# ---------------------------------------------------------
# moving flags
moving_left = False
moving_right = False
# ---------------------------------------------------------
# end game flag
game_over = False

# create objects: ball and platform
ball = Picture('rebel_sticker.png', 160, 200, 50, 50)
platform = Picture('yoda_5050.png', racket_x, racket_y, 50, 50)
end_label = Picture('end.png', 125, 125, 300, 300)
go_label = Picture('go_sign.png', 0, 0, 500, 500)
ready = Picture('ready.png', 0, 0, 500, 500)

# create enemies
start_x = 5  # first enemy coord
start_y = 5
enemies_count = 9  # enemies in the first raw
enemies = []  # enemies list

for j in range(3):  # create enemies cycle
    y_coord = start_y + (55 * j)  # shift every next raw on 55 px by axis y
    x_coord = start_x + (27.5 * j)  # and 27.5 by x

    for i in range(enemies_count):  # create raw of enemies same as count
        enemy = Picture('imperial_soldier.png', x_coord, y_coord, 50, 50)
        enemies.append(enemy)  # add to list
        x_coord += 55  # next enemy x coordinate
    enemies_count -= 1  # reduce next raw on 1 enemy

# start game cycle
ready.draw()
pygame.display.update()
sleep(2)
mw.fill(back)
go_label.draw()
pygame.display.update()
mw.fill(back)
sleep(2)
while not game_over:
    ball.fill()
    platform.fill()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        # -------------------------------------------
        # Check buttons and change move flags
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False
            # -----------------------------------------
    # left and right moving
    if moving_left:
        platform.rect.x -= 3

    if moving_right:
        platform.rect.x += 3
    # ----------------------------------------
    # permanent ball moving
    ball.rect.x += ball_x
    ball.rect.y += ball_y
    # ----------------------------------------
    # check borders, change direction if needs
    if ball.rect.y < 0:
        ball_y *= -1

    if ball.rect.x > 450 or ball.rect.x < 0:
        ball_x *= -1
    # check minimal y_coordinate
    if ball.rect.y > 350 or len(enemies) == 0:
        enemies = []
        mw.fill(back)
        end_label.fill()
        end_label.draw()
        pygame.display.update()
        sleep(2)
        game_over = True
        break
    # ----------------------------------------
    # check if ball touch the platform and change direction:
    if ball.rect.colliderect(platform.rect):
        ball_y *= - 1
    # ----------------------------------------
    # draw enemies from the list
    for enemy in enemies:
        enemy.draw()
    # ---------------------------------------
    # check if the ball has the same coordinates as enemy
        if enemy.rect.colliderect(ball.rect):
            enemies.remove(enemy)
            enemy.fill()
            ball_y *= -1
    # draw platform and ball
    platform.draw()
    ball.draw()
    # renew scene
    pygame.display.update()
    clock.tick(40)
