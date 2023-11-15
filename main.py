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

x1 = dis_width/2
y1 = dis_height/2
x1_update = 0
y1_update = 0

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_update = -10
                y1_update = 0
            elif event.key == pygame.K_RIGHT:
                x1_update = 10
                y1_update = 0
            elif event.key == pygame.K_UP:
                y1_update = -10
                x1_update = 0
            elif event.key == pygame.K_DOWN:
                y1_update = 10
                x1_update = 0
    x1 += x1_update
    y1 += y1_update
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()
