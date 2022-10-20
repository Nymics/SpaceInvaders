import pygame
import random

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800, 800))

# Title and Icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load(f'../Assets/spaceship.png')
pygame.display.set_icon(icon)

# Player Img
player_icon = pygame.image.load('../Assets/spaceship_small.png')

# Player Start Location
player_x = 400
player_y = 650
player_x_change = 0
player_y_change = 0

# Enemy
# Enemy Img
enemy_icon = pygame.image.load('../Assets/ufo.png')
# Player Start Location
enemy_x = 400
enemy_y = 50
enemy_y_change = 0.05
enemy_x_change_mod = [-5.1, 5.1]


# bullet
# bullet Img
bullet_icon = pygame.image.load('../Assets/bullet.png')
# Player Start Location
bullet_x = 400
bullet_y = 50
bullet_y_change = 0.05


background_icon = pygame.image.load('../Assets/background.jpg')


def draw_player(x, y):
    screen.blit(player_icon, (x, y))


def draw_enemy(x, y):

    screen.blit(enemy_icon, (x, y))


def draw_bullet(x, y):
    screen.blit(bullet_icon, (x, y))


running = True
MOVEEVENT, t, trail = pygame.USEREVENT + 1, 1, []
pygame.time.set_timer(MOVEEVENT, t)

# Game Loop
while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == MOVEEVENT:
            print(event.type)
            # draw_enemy(600, 400)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_UP:
                player_y_change = -0.5
            if event.key == pygame.K_DOWN:
                player_y_change = 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_y_change = 0

    # Background fill
    screen.fill((0, 0, 0))
    screen.blit(background_icon, (+0, 0))
    # print(event)

    # Player Boundaries
    if player_x <= 15:
        # player_x_change = 0
        player_x = 775
    elif player_x >= 775:
        player_x = 15

    # Draw Player
    player_x += player_x_change
    player_y += player_y_change
    draw_player(player_x, player_y)


    # Draw Enemies
    enemy_y = enemy_y + enemy_y_change
    enemy_x_change = random.choice(enemy_x_change_mod)
    # print(enemy_x_change)
    # enemy_x = ene
    # draw_enemy(600+enemy_x_change, enemy_y)
    draw_enemy(500 + enemy_x_change, enemy_y)
    draw_enemy(400, enemy_y)
    draw_enemy(300, enemy_y)
    draw_enemy(200, enemy_y)
    draw_enemy(100, enemy_y)

    # Draw bullets
    # draw_bullet(player_x, player_y)

    # update screen
    pygame.display.update()

# this is outside of my loop

