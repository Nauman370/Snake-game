import pygame
import random

pygame.init()
CELL=20
COLS,ROWS=20,20
screen=pygame.display.set_mode((COLS*CELL,ROWS*CELL))
pygame.display.set_caption("Snake Game")
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,28)


snake=[(10,10),(10,9),(10,8)]
direction=(1,0)
score=00
def food_snake():
    while True:
        position=(random.randrange(COLS)),(random.randrange(ROWS))
        if position not in snake:
            return position
food=food_snake()
running=True
def draw_background():
    for col in range(COLS):
        for row in range(ROWS):
            if (col+row)%2==0:
                color=(120,200,90)
            else:
                color=(105,185,80)
            pygame.draw.rect(screen,color,(col*CELL,row*CELL,CELL,CELL))
fx=food[0]*CELL+CELL//2
fy=food[1]*CELL+CELL//2
pygame.draw.circle(screen,(210,30,30),(fx,fy),CELL//2-2)
pygame.draw.circle(screen,(255, 140, 140),(fx-3,fy-3),2)
pygame.draw.rect(screen,(90, 60, 30),(fx-1,fy-CELL//2,2,4))
pygame.draw.rect(screen,(30, 140, 40),(fx+1,fy-CELL//2,6,4))


while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key in (pygame.K_UP ,pygame.K_w) and direction!=(0,1):
                direction=(0,-1)
            elif event.key in (pygame.K_DOWN , pygame.K_s) and direction!=(0,-1):
                direction=(0,1)
            elif event.key in (pygame.K_LEFT , pygame.K_a)and direction!=(1,0):
                direction=(-1,0)
            elif event.key in (pygame.K_RIGHT , pygame.K_d) and direction!=(-1,0):
                direction=(1,0)
    snk_x,snk_y=snake[0]
    dir_x,dir_y= direction
    moved_snake=(snk_x+dir_x,snk_y+dir_y)

    hit_wall=not(0<=moved_snake[0]<COLS and 0 <=moved_snake[1]<ROWS)
    hit_self=moved_snake in snake

    if (hit_wall or hit_self) is True:
        running=False
    else:
        snake.insert(0,moved_snake)
        if moved_snake==food:
            score+=1
            food= food_snake()
        else:
            snake.pop()
    draw_background()


    for i,(x,y) in enumerate(snake):
        if i==0:
            color=(30,90,200)
        else:
            color=(50,130,230)
        pygame.draw.rect(screen,color,(x*CELL+1,y*CELL+1,CELL-2,CELL-2),border_radius=3)
    fx=food[0]*CELL+CELL//2
    fy=food[1]*CELL+CELL//2
    pygame.draw.circle(screen,(210,30,30),(fx,fy),CELL//2-2)
    pygame.draw.circle(screen,(255, 140, 140),(fx-3,fy-3),2)
    pygame.draw.rect(screen,(90, 60, 30),(fx-1,fy-CELL//2,2,4))
    pygame.draw.rect(screen,(30, 140, 40),(fx+1,fy-CELL//2,6,4))



    text=font.render(f"score{score}",True,(255,255,255))
    screen.blit(text,(8,8))
    pygame.display.flip()
    clock.tick(8)
pygame.quit()

                

