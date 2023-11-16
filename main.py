import random
import pygame

pygame.init()

dis_height = 400
dis_width = 600
dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 69, 0)
green = (34, 139, 34)
gray = (169, 169, 169)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("Marker Felt", 20)
score_font = pygame.font.SysFont("comicsansms", 25)


def draw_whole_snake(entity_list, block):
    for x in entity_list:
        pygame.draw.rect(dis, green, [x[0], x[1], block, block])


def show_score(score):
    value = score_font.render("Your score: " + str(score), True, black)
    dis.blit(value, [10, 10])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 3, dis_height / 3])


def game_loop():
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_update = 0
    y1_update = 0

    snake_len = 1
    snake_list = []

    score = 0

    # initial coordinates of the food based on the display's measurements & the snake's;
    # the display's grid will have each cell 10 units wide.
    food_x1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y1 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    game_over = False
    game_close = False
    current_direction = 0
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
                if event.key == pygame.K_LEFT and current_direction != "RIGHT":
                    current_direction = "LEFT"
                    x1_update = -snake_block
                    y1_update = 0
                elif event.key == pygame.K_RIGHT and current_direction != "LEFT":
                    current_direction = "RIGHT"
                    x1_update = snake_block
                    y1_update = 0
                elif event.key == pygame.K_UP and current_direction != "DOWN":
                    current_direction = "UP"
                    y1_update = -snake_block
                    x1_update = 0
                elif event.key == pygame.K_DOWN and current_direction != "UP":
                    current_direction = "DOWN"
                    y1_update = snake_block
                    x1_update = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_update
        y1 += y1_update
        dis.fill(gray)
        pygame.draw.rect(dis, red, [food_x1, food_y1, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_whole_snake(snake_list, snake_block)
        show_score(score)

        pygame.display.update()

        if x1 == food_x1 and y1 == food_y1:
            snake_len += 1
            score += 1
            food_x1 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y1 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
