import pygame,sys, random
import time

def ball_collisions():
    global ball_speed_x, ball_speed_y,player1_score, player2_score,score_time
    ball_rect.x += ball_speed_x
    ball_rect.y += ball_speed_y
    if ball_rect.top <= 0 or ball_rect.bottom >= screen_height:
        ball_speed_y *= -1
    if ball_rect.left <= 0:
        player1_score += 1
        score_time = pygame.time.get_ticks()

    if ball_rect.right >= screen_wight:
        player2_score += 1
        score_time = pygame.time.get_ticks()

    if ball_rect.colliderect(player1) or ball_rect.colliderect(player2):
        pygame.mixer.Sound.play(kick_sound)
        ball_speed_x *= -1

def player1_animation():
    if player1.top <= 0: player1.top = 0
    if player1.bottom >= screen_height : player1.bottom = screen_height

def player2_move():
    if player2.top < ball_rect.y:
        player2.top += player2_speed
    if player2.bottom > ball_rect.y:
        player2.bottom -= player2_speed
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= screen_height:
        player2.bottom = screen_height


def ball_animation():
    global ball_surf, index_animation
    index_animation += 0.1
    if index_animation >= len(list_aniamation): index_animation = 0
    ball_surf = list_aniamation[int(index_animation)]

def ball_restart():
    global  ball_speed_x, ball_speed_y, score_time

    curent_time = pygame.time.get_ticks()
    ball_rect.center = (screen_wight / 2, screen_height / 2)
    pygame.mixer.Sound.play(goal_sound)

    if curent_time - score_time < 700:
        number_three = game_font.render("3", False, 'black')
        screen.blit(number_three, (screen_wight/2 - 10, screen_height / 2 + 30))
    if 700 < curent_time - score_time < 1400:
        number_thwo = game_font.render("2", False, 'black')
        screen.blit(number_thwo, (screen_wight/2 - 10, screen_height / 2 + 30))
    if 1400 < curent_time - score_time < 2100:
        number_one = game_font.render("1", False, 'black')
        screen.blit(number_one, (screen_wight/2 - 10, screen_height / 2 + 30))

    if curent_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y = 6 * random.choice((1, -1))
        ball_speed_x = 6 * random.choice((1, -1))
        score_time = None

#geme setup
pygame.init()
clock = pygame.time.Clock()

#main window
screen_wight = 1505
screen_height = 930
screen = pygame.display.set_mode((screen_wight, screen_height))
background = pygame.image.load('image/football-field.jpg')
pygame.display.set_caption('Pong football')

#Geme ractangles
ball1 = pygame.image.load('image/ball.png').convert_alpha()
ball1 = pygame.transform.scale(ball1, (35,35))
ball2 = pygame.image.load('image/ball_1.png').convert_alpha()
ball2 = pygame.transform.scale(ball2, (35,35))
ball3 = pygame.image.load('image/ball_2.png').convert_alpha()
ball3 = pygame.transform.scale(ball3, (35,35))
ball4 = pygame.image.load('image/ball_3.png').convert_alpha()
ball4 = pygame.transform.scale(ball4, (35,35))
list_aniamation = [ball1, ball2, ball3, ball4]
index_animation = 0
ball_surf = list_aniamation[index_animation]
ball_rect = ball_surf.get_rect(center = (screen_wight/2, screen_height/2))
player1 = pygame.Rect(screen_wight - 20, screen_height/2 - 70, 10, 200)
player2 = pygame.Rect(10, screen_height/2 - 70, 10, 200)

#geme varibles
ball_speed_x = 6 * random.choice((1,-1))
ball_speed_y = 6 * random.choice((1,-1))
player1_speed = 0
player2_speed = 15

#text varible
player1_score = 0
player2_score = 0
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#Score timer
score_time = True

#timer_game
time_limit = 90
start_time = time.time()

#sound
game_sound = pygame.mixer.Sound("audio/stadium1.wav")
game_sound.set_volume(0.01)
game_sound.play(loops=-1)
goal_sound = pygame.mixer.Sound("audio/goal.wav")
goal_sound.set_volume(0.01)
kick_sound = pygame.mixer.Sound("audio/kick.wav")
kick_sound.set_volume(0.03)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed += 7
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        pygame.quit()
        sys.exit()
    player1.y += player1_speed

    player1_animation()
    ball_collisions()
    player2_move()

    #player
    pygame.draw.rect(screen, (200,200,200), player1)
    pygame.draw.rect(screen, (200, 200, 200), player2)

    #ball
    ball_animation()
    screen.blit(ball_surf,ball_rect)

    #score
    player1_text = game_font.render(f"{player1_score}", False, (200,200,200))
    screen.blit(player1_text, (810, 450))
    player2_text = game_font.render(f"{player2_score}", False, (200, 200, 200))
    screen.blit(player2_text, (680, 450))
    #timer
    timer = game_font.render(f"{round(elapsed_time, 2)}", False, (200, 200, 200))
    screen.blit(timer, (20, 40))

    if score_time:
        ball_restart()

    #Update window
    pygame.display.flip()
    screen.blit(background,(0,0))
    clock.tick(60)



