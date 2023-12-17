import os
import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT, K_w
pygame.init()
FPS = pygame.time.Clock()
            # Display
WIDTH = 1200
HEIGHT=750
FONT=pygame.font.SysFont("Verdana", 20)
main_display = pygame.display.set_mode((WIDTH,HEIGHT))
BACKGROUND=pygame.transform.scale(pygame.image.load('background.png'), (WIDTH,HEIGHT))
BG_X1=0
BG_X2=BACKGROUND.get_width()
BG_move=3
            # Player
PLAYER_PATH = ('goose') 
PLAYER_IMAGES=os.listdir(PLAYER_PATH)           
player =pygame.image.load("player.png").convert_alpha()

player_size = player.get_size()
player_rect=pygame.Rect(0 ,300, *player_size)
player_move_down=[0,5]
player_move_up=[0,-5]
player_move_left=[-5,0]
player_move_right=[5,0]
# player_rect = player.get_rect()
# player = pygame.Surface(player_size)
# player.fill(COLOR_WHITE)
COLOR_WHITE=(255,255,255)
            # Enemy
def create_enemy():            
    COLOR_BLUE = (0,0,255)
    enemy =pygame.image.load("enemy.png").convert_alpha()
    enemy_size=enemy.get_size()
    enemy_rect=pygame.Rect(WIDTH ,random.randint(50,HEIGHT-50), *enemy_size)
    enemy_move=[random.randint(-28,-12),0]
    return [enemy, enemy_rect, enemy_move]
CREATE_ENEMY = pygame.USEREVENT+1
pygame.time.set_timer(CREATE_ENEMY,2000)
    # enemy_size = (20,80)
    # enemy = pygame.Surface(enemy_size)
    # enemy.fill(COLOR_BLUE)
            # Prize
def create_prize():              
    COLOR_RED = (255,0,0)
    # prize_size = (20,20)
    prize =pygame.image.load("bonus.png").convert_alpha()
    prize_size=prize.get_size()
    # prize = pygame.Surface(prize_size)
    # prize.fill(COLOR_RED)
    prize_rect=pygame.Rect(random.randint(100,WIDTH-100),0, *prize_size)
    prize_move=[0,random.randint(4,8)]
    return[prize,prize_rect,prize_move]
CREATE_PRIZE = pygame.USEREVENT+2
pygame.time.set_timer(CREATE_PRIZE,5000)


CHANGE_GOOSE_IMAGE = pygame.USEREVENT+3
pygame.time.set_timer(CHANGE_GOOSE_IMAGE,200)

enemies=[]
prizes=[]
counter=0
playing=True
image_goose_index = 0

while playing:
    FPS.tick(1200)   
    for event in pygame.event.get():
        if event.type==QUIT:
            playing=False 
        if event.type==CREATE_ENEMY:
            enemies.append(create_enemy())
        if event.type==CREATE_PRIZE:
            prizes.append(create_prize())
        if event.type== CHANGE_GOOSE_IMAGE:
            print(PLAYER_IMAGES)
            player=pygame.image.load(os.path.join(PLAYER_PATH, PLAYER_IMAGES[image_goose_index]))
            image_goose_index+=1
            if image_goose_index>=len(PLAYER_IMAGES):
                image_goose_index=0
                       
    # main_display.blit(BACKGROUND, (0,0))
    BG_X1-=BG_move
    BG_X2-=BG_move
    
    if BG_X1<-BACKGROUND.get_width():
        BG_X1=BACKGROUND.get_width()
    
    if BG_X2<-BACKGROUND.get_width():
        BG_X2=BACKGROUND.get_width()
    
    main_display.blit(BACKGROUND, (BG_X1,0))
    main_display.blit(BACKGROUND, (BG_X2,0))
    
    keys=pygame.key.get_pressed()
    if keys[K_DOWN]and player_rect.bottom<HEIGHT: 
        player_rect = player_rect.move(player_move_down)
    if keys [K_UP] and player_rect.top>0: 
        player_rect = player_rect.move(player_move_up)
    if keys[K_LEFT]and player_rect.left>0: 
        player_rect = player_rect.move(player_move_left)
    if keys[K_RIGHT]and player_rect.right<WIDTH: 
        player_rect = player_rect.move(player_move_right)
    
    for enemy in enemies:
        enemy[1]=enemy[1].move(enemy[2])
        main_display.blit(enemy[0], enemy[1])
     
        if player_rect.colliderect(enemy[1]):
            playing=False
        
    for prize in prizes:
        prize[1]=prize[1].move(prize[2])
        main_display.blit(prize[0], prize[1]) 
        
        if player_rect.colliderect(prize[1]):
            counter +=1
            prizes.pop(prizes.index(prize))
    
    main_display.blit(FONT.render(str(counter),True, COLOR_WHITE),(WIDTH-50,20))          
    main_display.blit(player, player_rect)  
      
    pygame.display.flip()
    
    for enemy in enemies:
        if enemy[1].left<0:
            enemies.pop(enemies.index(enemy))
    for prize in prizes:
        if prize[1].top>HEIGHT:
            prizes.pop(prizes.index(prize))
        
            
            
    