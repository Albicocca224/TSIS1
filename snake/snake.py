import pygame
import time
import random
import psycopg2
snake_speed = 10
window_x = 720
window_y = 480
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.init()
pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
food_timer = 0
food_threshold = 100
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    level_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    level_surface = level_font.render('Level : ' + str(snake_speed - 10), True, color)
    score_rect = score_surface.get_rect()
    level_rect = level_surface.get_rect()
    score_rect.topleft = (10, 10)
    level_rect.topleft = (10, 40)
    game_window.blit(score_surface, score_rect)
    game_window.blit(level_surface, level_rect)
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    if check_username(username):
        if score > get_user_score(username):
            save_score(username, score, snake_speed-10)
    else:
        insert_new_user(username, score, snake_speed-10)
    quit()
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="albicocca",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
def check_username(username):
    cursor.execute("SELECT * FROM snake WHERE username=%s", (username,))
    return cursor.fetchone() is not None
def get_user_level(username):
    cursor.execute("SELECT level FROM snake WHERE username=%s", (username,))
    return cursor.fetchone()[0]
def get_user_score(username):
    cursor.execute("SELECT score FROM snake WHERE username=%s", (username,))
    return cursor.fetchone()[0]
def save_score(username, score, level):
    cursor.execute("UPDATE snake SET score=%s, level=%s WHERE username=%s", (score, level, username))
    conn.commit()
def insert_new_user(username, score, level):
    cursor.execute("INSERT INTO snake (username, score, level) VALUES (%s, %s, %s)", (username, score, level))
    conn.commit()
username=input("Enter your username: ")
if check_username(username):
    snake_speed = get_user_level(username)+10
    score = get_user_score(username)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        snake_speed += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    food_timer+=1
    if food_timer >= food_threshold:
        fruit_spawn = False
        food_timer = 0
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
    show_score(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(snake_speed)
