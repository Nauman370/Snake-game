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
state="playing"
big_font=pygame.font.SysFont(None,56)

def reset_game():
    global snake,score,direction,food,state
    snake=[(10,10),(10,9),(10,8)]
    direction=(1,0)
    direction_queue.clear()
    score=0
    food=food_snake()
    state="playing"

restart_btn=pygame.Rect(80, 230, 240, 40)
quit_btn=pygame.Rect(80,285,240,40)

def draw_button(rect,label):
    mouse=pygame.mouse.get_pos()
    color=(70,160,70) if rect.collidepoint(mouse) else(40,120,40)
    pygame.draw.rect(screen,color,rect,border_radius=8)
    text=font.render(label,True,(255,255,255))
    screen.blit(text,text.get_rect(center=rect.center))
direction_queue=[]

Key_Dir={
    pygame.K_UP:(0,-1), pygame.K_w: (0,-1),
    pygame.K_DOWN:(0,1), pygame.K_s: (0,1),
    pygame.K_LEFT:(-1,0),pygame.K_a:(-1,0),
    pygame.K_RIGHT:(1,0),pygame.K_d:(1,0),
}




while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            if state=="playing":
                if event.key in Key_Dir:
                    new_dir=Key_Dir[event.key]
                last=direction_queue[-1] if direction_queue else direction
                if new_dir !=(-last[0],-last[1]) and len(direction_queue)<2:
                    direction_queue.append(new_dir)


            elif state=="gameover":
                if event.key==pygame.K_RETURN:
                    reset_game()
        if event.type==pygame.MOUSEBUTTONDOWN and state=="gameover":
            if restart_btn.collidepoint(event.pos):
                reset_game()
            elif quit_btn.collidepoint(event.pos):
                running=False
    
    if state=="playing":
        if direction_queue:
            direction=direction_queue.pop(0)

        snk_x,snk_y=snake[0]
        dir_x,dir_y= direction
        moved_snake=(snk_x+dir_x,snk_y+dir_y)

        hit_wall=not(0<=moved_snake[0]<COLS and 0 <=moved_snake[1]<ROWS)
        hit_self=moved_snake in snake

        if (hit_wall or hit_self) is True:
            state="gameover"

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
        elif i%2==0:
            color=(50,130,230)
        else:
            color=(35,105,235)
        pygame.draw.rect(screen,color,(x*CELL+1,y*CELL+1,CELL-2,CELL-2),border_radius=3)
    fx=food[0]*CELL+CELL//2
    fy=food[1]*CELL+CELL//2
    pygame.draw.circle(screen,(210,30,30),(fx,fy),CELL//2-2)
    pygame.draw.circle(screen,(255, 140, 140),(fx-3,fy-3),2)
    pygame.draw.ellipse(screen,(90, 60, 30),(fx-1,fy-CELL//2,2,4))
    pygame.draw.rect(screen,(30, 140, 40),(fx+1,fy-CELL//2,6,4))



    text=font.render(f"score:{score}",True,(255,255,255))
    screen.blit(text,(8,8))
    if state=="gameover":
        overlay=pygame.Surface((COLS*CELL,ROWS*CELL))
        overlay.set_alpha(160)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        title=big_font.render("Game Over",True,(255,255,255))
        screen.blit(title,title.get_rect(center=(COLS*CELL//2,175)))
        draw_button(restart_btn,"Press Enter to Restart")
        draw_button(quit_btn,"Press ESC to exit")
    pygame.display.flip()
    clock.tick(8)
pygame.quit()
