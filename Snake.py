import pygame
import random

pygame.init()
WINDOW=600
COLS=ROWS=20
CELL=WINDOW//COLS
fps=10
screen=pygame.display.set_mode((WINDOW,WINDOW),pygame.SCALED|pygame.RESIZABLE)
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
state="menu"
SPEEDS={"slow":8,"normal_s":10,"fast":14,"faster":18,"fastest":22}
GRIDS={"small":18,"normal_g":24,"big":30,"bigger":36,"biggest":40}
PRESETS={
    "Easiest":("slow","biggest"),
    "EZ_PZ":("slow","small"),
    "EZ":("normal_s","small"),
    "normal":("normal_s","normal_g"),
    "abnormal":("fastest","normal_g"),
    "HELP":("faster","small"),
    "NUH Uh":("fastest","small")
}
sel_speed="normal_s"
sel_grid="normal_g"
big_font=pygame.font.SysFont(None,56)

def reset_game():
    global snake,score,direction,food,state
    mid=COLS//2
    snake=[(mid,mid),(mid-1,mid),(mid-2,mid)]
    direction=(1,0)
    direction_queue.clear()
    score=0
    food=food_snake()
    state="playing"


def start_game(speed_name,grid_name):
    global COLS,ROWS,CELL,fps
    COLS=ROWS=GRIDS[grid_name]
    CELL=WINDOW//COLS
    fps=SPEEDS[speed_name]
    reset_game()

def make_row(labels,y,w,gap):
    total=len(labels)*w+(len(labels)-1)*gap
    x=(WINDOW-total)//2
    row=[]
    for label in labels:
        row.append((label,pygame.Rect(x,y,w,40)))
        x+=w+gap
    return row
def draw_text(msg,y,f=font):
    img=f.render(msg,True,(255,255,255))
    screen.blit(img,img.get_rect(center=(WINDOW//2,y)))
def draw_button(rect,label,selected=False):
    mouse=pygame.mouse.get_pos()
    if selected:
        color=(200,150,30)
    elif rect.collidepoint(mouse):
        color=(70,160,70)
    else:
        color=(40,120,40)
    pygame.draw.rect(screen,color,rect,border_radius=8)
    text=font.render(label,True,(255,255,255))
    screen.blit(text,text.get_rect(center=rect.center))
names=list(PRESETS)
preset_row1=make_row(names[:4],110,130,10)
preset_row2=make_row(names[4:],155,130,10)
preset_btns=preset_row1+preset_row2
speed_btns=make_row(list(SPEEDS),245,100,10)
grid_btns=make_row(list(GRIDS),340,105,8)
start_btn=pygame.Rect(WINDOW//2-120,430,240,44)
restart_btn=pygame.Rect(WINDOW//2-150,310,300,44)
menu_btn=pygame.Rect(WINDOW//2-150,365,300,44)
quit_btn=pygame.Rect(WINDOW//2-150,420,300,44)
def draw_button(rect,label,selected=False):
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
def draw_menu():
    screen.fill((30,60,30))
    draw_text("SNAKE",50,big_font)
    draw_text("Presets",90)
    for label,rect in preset_btns:
        draw_button(rect,label)
    draw_text("Custom:Choose Speed",220)
    for label,rect in speed_btns:
        draw_button(rect,label,label==sel_speed)
    draw_text("Custom:Choose grid",315)
    for label, rect in grid_btns:
        draw_button(rect,label,label==sel_grid)
    draw_button(start_btn,"Start Custom")



stripe_phase=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False

            if event.key ==(pygame.K_F11):
                pygame.display.toggle_fullscreen()
            if state=="playing":
                if event.key in Key_Dir:
                    new_dir=Key_Dir[event.key]
                    last=direction_queue[-1] if direction_queue else direction
                    if new_dir !=(-last[0],-last[1]) and len(direction_queue)<2:
                        direction_queue.append(new_dir)
            elif state=="gameover":
                if event.key==pygame.K_RETURN:
                    reset_game()
                elif event.key==pygame.K_m:
                    state="menu"
        if event.type==pygame.MOUSEBUTTONDOWN :
            if state=="menu":
                for label,rect in preset_btns:
                    if rect.collidepoint(event.pos):
                        start_game(*PRESETS[label])
                for label,rect in speed_btns:
                    if rect.collidepoint(event.pos):
                        sel_speed=label
                for label,rect in grid_btns:
                    if rect.collidepoint(event.pos):
                        sel_grid=label
                if start_btn.collidepoint(event.pos):
                    start_game(sel_speed,sel_grid)
            elif state=="gameover":

            
                if restart_btn.collidepoint(event.pos):
                    reset_game()
                elif menu_btn.collidepoint(event.pos):
                    state="menu"
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
    if state=="menu":
        draw_menu()
        pygame.display.flip()
        clock.tick(30)
        continue

    draw_background()
    if state=="playing":
        stripe_phase=(stripe_phase+4)%CELL
    


    for i,(x,y) in enumerate(snake):
        if i==0:
            color=(30,90,200)
        elif i%2==0:
            color=(50,130,230)
        else:
            color=(35,105,235)
        pygame.draw.rect(screen,color,(x*CELL+1,y*CELL+1,CELL-2,CELL-2),border_radius=3)
        if i>0:
            prev_x,prev_y=snake[i-1]
            stripe=[200,42,129]
            p=max(1,stripe_phase)
            w=min(3,CELL-1-p)
            if w>0:

                if prev_y==y:
                    pygame.draw.rect(screen,stripe,(x*CELL+p,y*CELL+4,w,CELL-8))
                else:
                    pygame.draw.rect(screen,stripe,(x*CELL+4,y*CELL+p,CELL-8,w))
    fx=food[0]*CELL+CELL//2
    fy=food[1]*CELL+CELL//2
    pygame.draw.circle(screen,(210,30,30),(fx,fy),CELL//2-2)
    pygame.draw.circle(screen,(255, 140, 140),(fx-3,fy-3),2)
    pygame.draw.ellipse(screen,(90, 60, 30),(fx-1,fy-CELL//2,2,4))
    pygame.draw.rect(screen,(30, 140, 40),(fx+1,fy-CELL//2,6,4))



    text=font.render(f"score:{score}",True,(255,255,255))
    screen.blit(text,(8,8))
    if state=="gameover":
        overlay=pygame.Surface((WINDOW,WINDOW))
        overlay.set_alpha(160)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        draw_text("Game Over",220,big_font)
        draw_text(f"Score:{score}",270)
        draw_button(restart_btn,"Restart,(Press enter)")
        draw_button(menu_btn,"Menu,(Press M to open M)")
        draw_button(quit_btn,"Quit,(Press ESC to exit)")
        title=big_font.render("Game Over",True,(255,255,255))
        screen.blit(title,title.get_rect(center=(COLS*CELL//2,175)))
        draw_button(restart_btn,"Press Enter to Restart")
        draw_button(quit_btn,"Press ESC to exit")
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
