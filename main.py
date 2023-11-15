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

x1 = dis_width / 2
y1 = dis_height / 2
x1_update = 0
y1_update = 0

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

game_over = False


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2, dis_height / 2])


while not game_over:
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
    if x1 >= dis_height or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    x1 += x1_update
    y1 += y1_update
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()

    clock.tick(snake_speed)
message("You lost",red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()
