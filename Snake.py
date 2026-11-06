import pygame
import random
import math

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
Fruits={"banana":{"points":2},
        "orange":{"points":3}}
bonus=None
bonus_wait=60
bonus_life=0
def food_snake():
    while True:
        position=(random.randrange(COLS)),(random.randrange(ROWS))
        if position not in snake and (bonus is None or position!=bonus[0]):
            return position
food=food_snake()
running=True
def draw_background():
    screen.fill((20,40,20))
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
tongue_Duration=450
tongue_next=pygame.time.get_ticks()+random.randint(1500,4000)
def draw_tongue():
    global tongue_next
    rn=pygame.time.get_ticks()
    if rn<tongue_next:
        return
    t=(rn-tongue_next)/tongue_Duration
    if t>=1:
        tongue_next=(rn+random.randint(1500,4000))
        return
    hx,hy=snake[0]
    dx,dy=direction
    px,py=-dy,dx
    ext=math.sin(t*math.pi)
    length=CELL*1.1*ext

    start=(hx*CELL+CELL//2+dx*CELL//2,hy*CELL+CELL//2+dy*CELL//2)
    width=max(2,CELL//8)
    color=(220,40,70)

    points=[]
    steps=8
    for i in range(steps+1):
        f=i/steps
        jiggle=math.sin(f*math.pi*2+t*math.pi*6)*CELL*0.15*f
        points.append((start[0]+dx*length*f+px*jiggle,
                       start[1]+dy*length*f+py*jiggle))
    pygame.draw.lines(screen,color,False,points,width)

    tip=points[-1]
    prong=CELL*0.3*ext
    for s in (-1,1):
        end=(tip[0]+dx*prong+px*prong*s, tip[1]+dy*prong+py*prong*s)
        pygame.draw.line(screen,color,tip,end,width)


def spawn_bonus():
    kind=random.choice(list(Fruits))
    while True:
        pos=(random.randrange(COLS),random.randrange(ROWS))
        if pos not in snake and pos!=food:
            return pos,kind


def draw_bonus():
    if bonus is None:
        return
    (bx,by),kind=bonus
    cx=bx*CELL+CELL//2
    cy=by*CELL+CELL//2
    if kind=="orange":
        pygame.draw.circle(screen,(250,150,30),(cx,cy),CELL//2-2)
        pygame.draw.circle(screen,(255,210,140),(cx-3,cy-3),2)
        pygame.draw.ellipse(screen,(30,140,40),(cx,cy-CELL//2,6,4))
    else:
        pts=[(0.1,0.2),(0.3,0.5),(0.5,0.6),(0.7,0.5),(0.9,0.2),
             (0.97,0.5),(0.75,0.85),(0.5,1.0),(0.25,0.85),(0.03,0.5)]
        shape=[(bx*CELL+int(u*CELL),by*CELL+int(v*CELL)) for u,v in pts]
        pygame.draw.polygon(screen,(240,220,60),shape)
        pygame.draw.polygon(screen,(150,120,20),shape,1)
    


def reset_game():
    global snake,score,direction,food,state,bonus,bonus_wait
    bonus=None
    bonus_wait=random.randint(3*fps,8*fps)
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

        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                running=False
            elif event.key==pygame.K_F11:
                pygame.display.toggle_fullscreen()
            elif event.key==pygame.K_p:
                if state=="playing":
                    state="paused"
                elif state=="paused":
                    state="playing"
            elif state=="playing" and event.key in Key_Dir:
                new_dir=Key_Dir[event.key]
                last=direction_queue[-1] if direction_queue else direction
                if new_dir!=(-last[0],-last[1]) and len(direction_queue)<2:
                    direction_queue.append(new_dir)
            elif state=="gameover":
                if event.key==pygame.K_RETURN:
                    reset_game()
                elif event.key==pygame.K_m:
                    state="menu"
            elif state=="paused" and event.key==pygame.K_m:
                state="menu"

        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if state=="menu":
                for label,rect in preset_btns:
                    if rect.collidepoint(event.pos):
                        start_game(*PRESETS[label])
                        break
                else:
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
            ate=False
            if moved_snake==food:
                score+=1
                food= food_snake()
                ate=True
            elif bonus is not None and moved_snake==bonus[0]:
                score+=Fruits[bonus[1]]["points"]
                bonus=None
                bonus_wait=random.randint(3*fps,8*fps)
                ate=True
            if not ate:
                snake.pop()
        if bonus is None:
            bonus_wait-=1
            if bonus_wait<=0:
                    bonus=spawn_bonus()
                    bonus_life=6*fps
        else:
                bonus_life-=1
                if bonus_life<=0:
                    bonus=None
                    bonus_wait=random.randint(3*fps,8*fps)
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
    if state=="playing":
        draw_tongue()
    fx=food[0]*CELL+CELL//2
    fy=food[1]*CELL+CELL//2
    pygame.draw.circle(screen,(210,30,30),(fx,fy),CELL//2-2)
    pygame.draw.circle(screen,(255, 140, 140),(fx-3,fy-3),2)
    pygame.draw.ellipse(screen,(90, 60, 30),(fx-1,fy-CELL//2,2,4))
    pygame.draw.rect(screen,(30, 140, 40),(fx+1,fy-CELL//2,6,4))
    draw_bonus()
    text=font.render(f"score:{score}",True,(255,255,255))
    screen.blit(text,(8,8))
    if state=="gameover":
        overlay=pygame.Surface((WINDOW,WINDOW))
        overlay.set_alpha(160)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        draw_text(f"Score:{score}",270)
        draw_button(restart_btn,"Restart (Press enter)")
        draw_button(menu_btn,"Menu (Press M to open M)")
        draw_button(quit_btn,"Quit (Press ESC to exit)")
        title=big_font.render("Game Over",True,(255,255,255))
        screen.blit(title,title.get_rect(center=(WINDOW//2,175)))
    if state=="paused":
        overlay=pygame.Surface((WINDOW,WINDOW))
        overlay.set_alpha(120)
        overlay.fill((0,0,0))
        screen.blit(overlay,(0,0))
        draw_text("Paused",260,big_font)
        draw_text("press P to resume/pause",310)
        draw_text("press M to go to Menu",345)
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
