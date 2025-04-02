import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
width = 600
height = 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Snake settings
snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def our_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

# Function to display a message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [width / 6, height / 3])

# Function to generate new food coordinates
def generate_food():
    return round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Game loop function
def gameLoop():
    game_over = False
    game_close = False

    # Initial game variables
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1

    # Generate food position
    foodx, foody = generate_food()

    clock = pygame.time.Clock()

    while not game_over:

        while game_close:
            window.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            our_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # Reset game variables
                        game_close = False
                        x1 = width / 2
                        y1 = height / 2
                        x1_change = 0
                        y1_change = 0
                        snake_List = []
                        Length_of_snake = 1
                        foodx, foody = generate_food()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:  # Prevent moving in opposite direction
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        window.fill(blue)
        pygame.draw.rect(window, white, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        our_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if snake eats the food
        if x1 == foodx and y1 == foody:
            foodx, foody = generate_food()  # Generate new food position
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
gameLoop()
