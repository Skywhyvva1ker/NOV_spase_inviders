import pygame as pg
import random


pg.init()

pause = False
game_over = False
screen_width, screen_height = 800, 600

FPS = 60  
clock = pg.time.Clock()

# звуки
laser_sound = pg.mixer.Sound("NOV_spase_inviders/laser.wav")
explosion = pg.mixer.Sound("NOV_spase_inviders/explosion.wav")
laser_sound.set_volume(0.1)
explosion.set_volume(0.05)
pg.mixer.music.load("NOV_spase_inviders/background.wav")
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)
# изображения
bg_img = pg.image.load('NOV_spase_inviders/background.png')
icon_img = pg.image.load('NOV_spase_inviders/ufo.png')

display = pg.display.set_mode((screen_width, screen_height))
pg.display.set_icon(icon_img)
pg.display.set_caption('Космическое вторжение')

sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('NOV_spase_inviders/04B_19.TTF', 48)

# display.fill('blue', (0, 0, screen_width, screen_height))
display.blit(bg_img, (0, 0))        

text_img = sys_font.render('Score 123', True, 'white')
# display.blit(text_img, (100, 50))

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()

game_pause= font.render('Pause', True, 'yellow')
w_pause, h_pause = game_pause.get_size()

# display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))

# игрок
player_img = pg.image.load('NOV_spase_inviders/player.png')
player_width, player_height = player_img.get_size()
player_gap = 10
player_velocity = 10
player_dx = 0
player_x = screen_width/2 - player_width/2
player_y = screen_height  - player_height - player_gap
score = 0

# пуля
bullet_img = pg.image.load('NOV_spase_inviders/bullet.png')
bullet_width, bullet_height = bullet_img.get_size()
bullet_dy = -5
bullet_x = 0     # микро дз - пускать из середины
bullet_y = 0
bullet_alive = False    # есть пуля?

# противник
enemy_img = pg.image.load('NOV_spase_inviders/enemy.png')
enemy_width, enemy_height = enemy_img.get_size()
enemy_dx = 0
enemy_dy = 1
enemy_x = 0
enemy_y = 0

def enemy_create():
    """ Создаем противника в случайном месте вверху окна."""
    global enemy_y, enemy_x
    enemy_x = random.randint(0, screen_width- enemy_width)   # screen_width / 2 - enemy_width / 2
    enemy_y = 0
    print(f'CREATE: {enemy_x=}')

def model_update():
    if not pause:
        palayer_model()
        bullet_model()
        enemy_model()

def palayer_model():
    global player_x
    player_x += player_dx
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

def bullet_model():
    """ Изменяется положение пули.
    """
    global bullet_y, bullet_alive
    bullet_y += bullet_dy
    # пуля улетела за верх экрана
    if bullet_y < 0:
        bullet_alive = False

def bullet_create():
    global bullet_y, bullet_x, bullet_alive
    bullet_alive = True
    bullet_x = player_x + bullet_width/2
    bullet_y = player_y - bullet_height

def enemy_model():
    """ Изменение положения противника, рассчет поражений."""
    global enemy_y, enemy_x, bullet_alive, score, game_over, enemy_dy

    enemy_x += enemy_dx
    enemy_y += enemy_dy
    if enemy_y > screen_height:
        game_over = True


    # пересечение с пулей
    if bullet_alive:
        re = pg.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
        rb = pg.Rect(bullet_x, bullet_y, bullet_width, bullet_height)
        is_crossed = re.colliderect(rb)
        # попал!
        if is_crossed:
            score += 1
            enemy_dy += 0.25
            if enemy_dy >= 5:
                enemy_dy = 4.9
            print('BANG!')
            explosion.play()
            enemy_create()
            bullet_alive = False

def display_redraw():
    if not game_over:
        display.blit(bg_img, (0, 0))
        display.blit(player_img, (player_x, player_y))
        display.blit(enemy_img, (enemy_x, enemy_y))
        score_img = font.render(f"Score: {score}", True, 'red')
        display.blit(score_img, (screen_width - 250, screen_height - 585))
        if bullet_alive:
            display.blit(bullet_img, (bullet_x, bullet_y))
        if pause == True:
            display.blit(game_pause, (screen_width/2 - w_pause/2, screen_height / 2 - h_pause/2))
    else:
        display.blit(game_over_text, (screen_width/2 - w/2, screen_height / 2 - h/2))
    pg.display.update()

def paused_music():
    if pause == True:
        pg.mixer.music.pause() 
    else:
        pg.mixer.music.play()   

def event_processing():
    global player_dx, pause, score, game_over
    running = True
    for event in pg.event.get():
        # нажали крестик на окне
        if event.type == pg.QUIT:
            running = False
        # тут нажимаем на клавиши
        if event.type == pg.KEYDOWN:
            # нажали на q - quit
            if event.key == pg.K_q:
                running = False
            # нажали на p - pause/reusme
            if event.key == pg.K_p:
                pause = not pause
                paused_music()
            # нажали на r - restart
            if event.key == pg.K_r:
                enemy_create()
                score = 0
                game_over = False
                running = True
                while running:
                    model_update()
                    display_redraw()
                    running = event_processing()
        # движение игрока
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                player_dx = -player_velocity
            if event.key == pg.K_d or event.key == pg.K_RIGHT:
                player_dx = player_velocity
        if event.type == pg.KEYUP:
            player_dx = 0

        # по левому клику мыши стреляем
        if event.type == pg.MOUSEBUTTONDOWN:
            if game_over == True:
                print('Game over')
            elif not bullet_alive and event.button == 1:
                laser_sound.play()
            key = pg.mouse.get_pressed()    # key[0] - left, key[2] - right
            print(f'{key[0]=} {bullet_alive=}')
            if not bullet_alive:
                bullet_create()


    clock.tick(FPS)
    return running

# random.seed(77)
enemy_create()
running = True
while running:
    model_update()
    display_redraw()
    running = event_processing()

pg.quit()