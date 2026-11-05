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

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP and direction!=(0,1):
                direction=(0,-1)
            elif event.key==pygame.K_DOWN and direction!=(0,-1):
                direction=(0,1)
            elif event.key==pygame.K_LEFT and direction!=(1,0):
                direction=(-1,0)
            elif event.key==pygame.K_RIGHT and direction!=(-1,0):
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
    screen.fill((20,20,20))

    for x,y in snake:
        pygame.draw.rect(screen,(0,200,80), (x*CELL,y*CELL,CELL-1,CELL-1))
    pygame.draw.rect(screen, (220, 50, 50), (food[0] * CELL, food[1] * CELL, CELL - 1, CELL - 1))
    text=font.render(f"score:{score}",True,[255,255,255])
    screen.blit(text,(8,8))
    pygame.display.flip()
    clock.tick(2)
pygame.quit()
                

