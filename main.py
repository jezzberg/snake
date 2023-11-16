import random
import time

import pygame

pygame.init()

dis_height = 600
dis_width = 800
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)

snake_block = 15
snake_speed = 20

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def game_loop():
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_update = 0
    y1_update = 0

    points_counter = 0

    # initial coordinates of the food based on the display's measurements & the snake's;
    # the display's grid will have each cell 10 units wide.
    food_x1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y1 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    game_over = False
    game_close = False
    while not game_over:

        while game_close:
            dis.fill(white)
            message("You lost! Press Q - Quit or R - Replay.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
                elif event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_update = -snake_block
                    y1_update = 0
                elif event.key == pygame.K_RIGHT:
                    x1_update = snake_block
                    y1_update = 0
                elif event.key == pygame.K_UP:
                    y1_update = -snake_block
                    x1_update = 0
                elif event.key == pygame.K_DOWN:
                    y1_update = snake_block
                    x1_update = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_update
        y1 += y1_update
        dis.fill(white)
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        pygame.draw.rect(dis, blue, [food_x1, food_y1, snake_block, snake_block])
        pygame.display.update()

        if x1 == food_x1 and y1 == food_y1:
            points_counter += 1
            print("Current points: " + str(points_counter))

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
