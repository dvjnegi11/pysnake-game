import pygame
import random
import os

# adding music
pygame.mixer.init()

pygame.init()

# x = pygame.init()
# print(x) print number of modules initialised

# creating a window for game
gameWindow = pygame.display.set_mode((800, 600))
pygame.display.update()

# adding image
back_image = pygame.image.load('b.png')
back_image = pygame.transform.scale(back_image, (800, 600)).convert_alpha()
back_image1 = pygame.image.load('bg.jpg')
back_image1 = pygame.transform.scale(back_image1, (800, 600)).convert_alpha()

# caption for the window [ TITLE ]
pygame.display.set_caption("SNAKE")

# defining color
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

font = pygame.font.SysFont('None', 40)
clock = pygame.time.Clock()


# function for displaying text
def text_screen(text, color, a, b):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [a, b])


# plot snake
def plot_snake(game_window, color, snake_list, snake_size):
    for a, b in snake_list:
        pygame.draw.rect(game_window, color, [a, b, snake_size, snake_size])


# welcome screen
def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        # adding background image
        gameWindow.blit(back_image1, (0, 0))
        text_screen("WELCOME TO SNAKES", white, 240, 240)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('bk.mp3')
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(60)


# creating game loop
# game loop - a loop handles all the events in the game
def game_loop():
    # *** Game specific variables ***
    # variable in case for ending the game
    exit_game = False
    # variable in case the player loss the game
    game_over = False
    x = 45
    v_x = 0
    y = 55
    v_y = 0
    snake_size = 10
    # frame per second
    fps = 30
    food_x = random.randint(12, 400)
    food_y = random.randint(12, 450)
    score = 0
    init_velocity = 5
    snake_list = []
    snake_len = 1
    # check if os file exist
    if not os.path.exists("Hscore.txt"):
        with open("Hscore.txt", "w") as f:
            f.write("0")
    with open("Hscore.txt", "r") as f:
        hscore = f.read()
    while not exit_game:
        if game_over:
            with open("Hscore.txt", "w") as f:
                f.write(str(hscore))
            gameWindow.fill((233, 220, 239))
            # adding background image
            gameWindow.blit(back_image1, (0, 0))
            # game over text
            text_screen("Game Over!!  Press ENTER to CONTINUE", black, 100, 200)
            text_screen("  Score " + str(score), red, 150, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        v_x = init_velocity
                        v_y = 0
                    if event.key == pygame.K_LEFT:
                        v_x = -init_velocity
                        v_y = 0
                    if event.key == pygame.K_UP:
                        v_y = -init_velocity
                        v_x = 0
                    if event.key == pygame.K_DOWN:
                        v_y = init_velocity
                        v_x = 0
            x += v_x
            y += v_y
            if abs(x - food_x) < 6 and abs(y - food_y) < 6:
                score += 5
                food_x = random.randint(30, 370)
                food_y = random.randint(30, 420)
                snake_len += 2
                if score > int(hscore):
                    hscore = score
            gameWindow.fill(white)
            gameWindow.blit(back_image, (0, 0))
            text_screen("Score " + str(score) + "  High Score " + str(hscore), red, 4, 4)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = list([])
            head.append(x)
            head.append(y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('game-over.wav')
                pygame.mixer.music.play()
            if x < 0 or x > 800 or y < 0 or y > 900:
                game_over = True
                pygame.mixer.music.load('game-over.wav')
                pygame.mixer.music.play()
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()


welcome()
