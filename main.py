import pygame

width = 1500
height = 1000
tileCount = 1000
moves_per_frame = 1000

tiles = [[0 for i in range(tileCount)] for j in range(tileCount)]
ant_x = len(tiles) / 2
ant_y = len(tiles) / 2
ant_direction = 0
actions = [1, 0, 1, 1, 1, 1, 1, 0, 0]


def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #pygame.time.delay(1000)
        for i in range(moves_per_frame):
            if ant_x < len(tiles) and ant_x >= 0 and ant_y < len(tiles) and ant_y >= 0:
                draw(screen)
        pygame.display.update()


def draw(screen):
    size = height / tileCount
    pos_x = width / 2 - height / 2

    global ant_x, ant_y, ant_direction
    ant_x = int(ant_x)
    ant_y = int(ant_y)
    ant_direction = int(ant_direction)

    tiles[ant_x][ant_y] = tiles[ant_x][ant_y] + 1
    if tiles[ant_x][ant_y] >= len(actions):
        tiles[ant_x][ant_y] = 0

    tile = actions[tiles[ant_x][ant_y]]
    if tile == 0:
        ant_direction = ant_direction - 1
    else:
        ant_direction = ant_direction + 1

    if ant_direction >= 4:
        ant_direction = 0
    if ant_direction < 0:
        ant_direction = 3

    pygame.draw.rect(screen, (0, int(tiles[ant_x][ant_y] / len(actions) * 250) + 5, 0), (ant_x * size + pos_x, ant_y * size, size, size))

    if ant_direction == 0:
        ant_y = ant_y - 1
    if ant_direction == 1:
        ant_x = ant_x + 1
    if ant_direction == 2:
        ant_y = ant_y + 1
    if ant_direction == 3:
        ant_x = ant_x - 1


main()
