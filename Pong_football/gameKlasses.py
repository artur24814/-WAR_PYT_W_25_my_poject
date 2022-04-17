import pygame,sys, random
import time

def club1_animation():
    global index_club_list1, clubs_surf1
    index_club_list1 += 1
    if index_club_list1 >= len(list_of_clubs1) : index_club_list1 = 0
    clubs_surf1 = list_of_clubs1[int(index_club_list1)]

def club2_animation():
    global index_club_list2, clubs_surf2
    index_club_list2 += 0.1
    if index_club_list2 >= len(list_of_clubs2) : index_club_list2 = 0
    clubs_surf2 = list_of_clubs1[int(index_club_list2)]


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

#text varible
player1_score = 0
player2_score = 0
game_font = pygame.font.Font('font/Pixeltype.ttf', 50)

#main window
screen_wight = 1505
screen_height = 930
screen = pygame.display.set_mode((screen_wight, screen_height))
background = pygame.image.load('image/football-field.jpg')
pygame.display.set_caption('Pong football')

#game start
start_surf = pygame.image.load('image/start.png')
start_rect = start_surf.get_rect(center = (750, 430))
geme_text = game_font.render('choose your football club', False, (100, 100, 100))
geme_text_rect = geme_text.get_rect(center = (750,100))
chouse1 = game_font.render('play with computer', False, (100,100,100))
chouse1_rect = chouse1.get_rect(center=(750, 700))
chouse2 = game_font.render('play with player', False, (100,100,100))
chouse2_rect = chouse2.get_rect(center=(750, 800))

mouse_rect = pygame.Rect(0, 0, 75, 75)
mouse_rect.center = pygame.mouse.get_pos()


#foolball clubs player 1
club1_1= pygame.image.load('image/Arsenal.png').convert_alpha()
club1_2= pygame.image.load('image/AstonV.png').convert_alpha()
club1_3= pygame.image.load('image/Chelsea.png').convert_alpha()
club1_4= pygame.image.load('image/city.png').convert_alpha()
club1_5= pygame.image.load('image/Everton.png').convert_alpha()
club1_6= pygame.image.load('image/liverpool.png').convert_alpha()
club1_7= pygame.image.load('image/Man_u.png').convert_alpha()
club1_8= pygame.image.load('image/newcasl.png').convert_alpha()
club1_9= pygame.image.load('image/nordwich.png').convert_alpha()
club1_10= pygame.image.load('image/saint.png').convert_alpha()
club1_11= pygame.image.load('image/totenhem.png').convert_alpha()
club1_12= pygame.image.load('image/west_ham.png').convert_alpha()
list_of_clubs1 = [club1_1, club1_2, club1_3, club1_4, club1_5, club1_6, club1_7, club1_8, club1_9, club1_10, club1_11, club1_12]
index_club_list1 = 0
clubs_surf1 = list_of_clubs1[index_club_list1]
clubs_rect1 = clubs_surf1.get_rect(center = (300, 400))
#foolball clubs player 2
club2_1 = pygame.image.load('image/Arsenal.png').convert_alpha()
club2_2= pygame.image.load('image/AstonV.png').convert_alpha()
club2_3= pygame.image.load('image/Chelsea.png').convert_alpha()
club2_4= pygame.image.load('image/city.png').convert_alpha()
club2_5= pygame.image.load('image/Everton.png').convert_alpha()
club2_6= pygame.image.load('image/liverpool.png').convert_alpha()
club2_7= pygame.image.load('image/Man_u.png').convert_alpha()
club2_8= pygame.image.load('image/newcasl.png').convert_alpha()
club2_9= pygame.image.load('image/nordwich.png').convert_alpha()
club2_10= pygame.image.load('image/saint.png').convert_alpha()
club2_11= pygame.image.load('image/totenhem.png').convert_alpha()
club2_12= pygame.image.load('image/west_ham.png').convert_alpha()
list_of_clubs2 = [club2_1, club2_2, club2_3, club2_4, club2_5, club2_6, club2_7, club2_8, club2_9, club2_10, club2_11, club2_12]
index_club_list2 = 0
clubs_surf2 = list_of_clubs2[index_club_list2]
clubs_rect2 = clubs_surf2.get_rect(center = (1200, 400))


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
game_active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_active = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -= 7
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                club2_animation()
            if event.key == pygame.K_a:
                club1_animation()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed += 7
    if game_active:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            game_active = False
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
    else:
        screen.fill('white')
        screen.blit(start_surf, start_rect)
        screen.blit(geme_text, geme_text_rect)
        screen.blit(chouse1,chouse1_rect)
        screen.blit(chouse2,chouse2_rect)
        screen.blit(clubs_surf1, clubs_rect1)
        screen.blit(clubs_surf2, clubs_rect2)


        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     # and mouse_rect.colliderect(chouse1_rect) or  mouse_rect.colliderect(chouse2_rect):
        #     game_active = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                club2_animation()
        #     if event.key == pygame.K_a:
        #         club1_animation()
        pygame.display.flip()

    clock.tick(60)



