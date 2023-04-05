import pygame
from pygame.constants import QUIT,K_DOWN,K_UP
pygame.init()
screen = width,hight = 800, 600
print(screen)
BLACK=0,0,0
WHITE=255,255,255
RED = 255,160,122
GREEN = 124,252,0
main_surface = pygame.display.set_mode(screen)
ball = pygame.Surface((20,20))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = 1
is_working = True  

while is_working:
    for event in pygame.event.get():
        if event.type==QUIT:
            is_working==False
    
    
    pressed_keys = pygame.key.get_pressed(); 
    
    # if ball_rect.bottom>=hight or ball_rect.top<=0:
    #     ball_speed[1] = -ball_speed[1]
    #     ball.fill(RED)
    
    
    if ball_rect.right>=width or ball_rect.left<=0: 
        # ball_speed[0] = -ball_speed[0]
        ball.fill(GREEN)
    
    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)
    
    if pressed_keys[K_DOWN]:
        ball_rect = ball_rect.move(0,ball_speed)
        
    if pressed_keys[K_UP]:
        ball_rect = ball_rect.move(0,-ball_speed)
    pygame.display.flip()         