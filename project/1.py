import pygame
import sys
import cmath
from pygame import mixer

mixer.init()

width=1024
height=570









window=pygame.display.set_mode((width, height+30))
pygame.display.set_caption('Volleyball')
screen=pygame.Surface((width, height))
pygame.key.set_repeat(1,1)
info_string=pygame.Surface((width,height+30))
clock=pygame.time.Clock()
fon = pygame.image.load("fon.jpg")
#цвта

white = [255, 255, 255]

na_fon=[222,150,206]
na_tablo=[0,186,255]
beige=[255,235,211]


bg = pygame.image.load("804358.jpg")

priroda=pygame.mixer.Sound('pri.ogg')
shlepok=pygame.mixer.Sound('shl.ogg')
priroda.play(-1)
pygame.font.init()
l1=100
a=0
b=0



done1=False
done2=False
class Picture:
    def __init__(self,x, y, vx ,vy,filename):
        self.x=x
        self.y=y
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey(white)
        self.vx=vx
        self.vy=vy

    def render(self):
        screen.blit(self.bitmap, (self.x,self.y))
zq2='z2.png'
z1=Picture(width//2-274,50,0,0,'VOLLEYBALL.png')
z2=Picture(width//2-150,160,0,0,zq2)
z11=Picture(width//2-180,160,0,0,'z11.png')
z3=Picture(width//2-190,257,0,0,'z3.png')
z22=Picture(width//2-193,257,0,0,'z22.png')
z4=Picture(width//2-87,354,0,0,'z4.png')
z33=Picture(width//2-94,354,0,0,'z33.png')
stolb=Picture(width/2-15,height/2-25,0,0,'stolb.png')
ball=Picture(300,100,0,0,'21.png')
person1=Picture(width//2-200-l1*3//4,height-190,500,0,'PORS22.png')
person2=Picture(width//2+200,height-190,500,0,'pors26.png')
ship1=Picture(30,height//2+55,10,0,'ship.png')
ship2=Picture(-300,height//2+55,-10,0,'ship2.png')
plan=Picture(-300,height//2+300,100,100,'plan.png')
tr=Picture(-300,5,0,0,'tr.png')
foul=Picture(3000,height//4,0,0,'foul.png')
score=Picture(3000,height//4,0,0,'score.png')
inf_font=pygame.font.SysFont('Arial', 24, True,False)
q1=True
q2=True
q3=True
q4=True
gr=0
gra=50
s=0
dv1=0
dv2=0


inf_font=pygame.font.SysFont('Arial', 24, True,False)
done=True
while done:
    dt = clock.tick(50) / 1000.0
    #выход из игры
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:

                pygame.key.set_repeat(0,0)
                pygame.mouse.set_visible(True)
    screen.blit(fon, (0, 0))
    pos = pygame.mouse.get_pos()
    mouse_x, mouse_y = pos[0], pos[1]

    z2.x=width//2-167
    z3.x=width//2-190
    z4.x=width//2-87

    if mouse_x>=width//2-167 and mouse_x<=width//2+167 and mouse_y>=z2.y and mouse_y<=z2.y+97:
        z2.x=3000
        z11.render()
        if pygame.mouse.get_pressed()[0]:
            done1=True
            done=False
            done3=True

    if mouse_x>=width//2-190 and mouse_x<=width//2+190 and mouse_y>=z3.y and mouse_y<=z3.y+97:
        z3.x=3000
        z22.render()
        if pygame.mouse.get_pressed()[0]:
            done2=True
            done=False
            done3=True


    if mouse_x>=width//2-87 and mouse_x<=width//2+87 and mouse_y>=z4.y and mouse_y<=z4.y+97:
        z4.x=3000
        z33.render()
        if pygame.mouse.get_pressed()[0]:
            sys.exit()

    z1.render()
    z2.render()
    z3.render()
    z4.render()
    info_string.fill((0,120,207))
    pygame.display.update()


    window.blit(info_string, (0,0))
    window.blit(screen, (0, 30))
    pygame.display.flip()





#основной цикл
dvt=0
time=0
while done3:

    dt = clock.tick(50) / 1000.0
    #выход из игры
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            done3=False
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_ESCAPE:

                done3=False
                pygame.key.set_repeat(0,0)
                pygame.mouse.set_visible(True)
    screen.blit(bg, (0, 0))
    if ball.x<=width//2:
        if (pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_d] or
    pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_s]):
            s=1

        if s==1:
            gr=500*1.5
            s=0
    if done1:
        if ball.x <= width // 2 and person2.x <= width * 3 // 4 - 100:
            person2.x += person2.vx * dt
            person2.vx = 300
        if person2.x <= width - l1 and person2.x >= width // 2 and ball.x >= width // 2 and ball.x <= width - 100:
            person2.x += person2.vx * dt
            if ball.x >= person2.x+10:
                person2.vx = abs(ball.vx)+10
            if ball.x < person2.x+10:
                person2.vx = -abs(ball.vx)+10
        elif person2.x < width // 2:
            person2.x += 10
        elif person2.x > width - l1:
            person2.x -= 10
        person2.y += person2.vy * dt
        if person2.y < height - 190:
            person2.vy += 20 * gra * dt
        if person2.y > height - 190:
            person2.y = height - 190
            person2.vy = 0
        if ball.x >= width // 2 and ball.y >= person2.y - 300 and ball.y <= person2.y - 150 and person2.y == height - 190:
            person2.vy = -600
        if ball.x==width-300 and ball.y==100 and person2.y == height - 190:
            gr=500*1.5
    if done2:
        if person2.x <= width - l1 - person2.vx * dt // 2 and person2.x >= width // 2 + person2.vx * dt // 2:
            if pygame.key.get_pressed()[pygame.K_RIGHT] and q3 == True:
                person2.x += person2.vx * dt
                q4 = True
            if pygame.key.get_pressed()[pygame.K_LEFT] and q4 == True:
                person2.x -= person2.vx * dt
                q3 = True
        elif person2.x < width // 2 + person2.vx * dt // 2:
            person2.x += 10
            q4 = False
        elif person2.x > width - l1 - person2.vx * dt // 2:
            person2.x -= 10
            q3 = False
        if ball.x >= width // 2:
            if (pygame.key.get_pressed()[pygame.K_LEFT] or pygame.key.get_pressed()[pygame.K_RIGHT] or
                    pygame.key.get_pressed()[pygame.K_UP] or pygame.key.get_pressed()[pygame.K_DOWN]):
                s = 1
            if s == 1:
                gr = 500 * 1.5
                s = 0
        if pygame.key.get_pressed()[pygame.K_UP] and person2.y == height - 190:
            person2.vy = -600


    if person1.x<=width//2-100-person1.vx*dt//2 and person1.x>=person1.vx*dt//2:
        if pygame.key.get_pressed()[pygame.K_d] and q1==True :
            person1.x+=person1.vx*dt
            q2=True
        if pygame.key.get_pressed()[pygame.K_a] and q2==True:
            person1.x-=person1.vx*dt
            q1=True
    elif person1.x<person1.vx*dt//2:
        person1.x+=10
        q2=False
    elif person1.x>width//2-100-person1.vx*dt//2:
        person1.x-=10
        q1=False




    ball.x+=ball.vx*dt
    ball.y+=ball.vy*dt
    ball.vy+=gr*dt

    ship1.x+=ship1.vx*dt
    ship2.x+=ship2.vx*dt
    plan.x+=plan.vx*dt
    plan.y-=plan.vy*dt

    if ship1.x>=3*width//4:
        ship1.x=-10000
        ship2.x=3*width//4
    if ship2.x<=0:
        ship1.x=0
        ship2.x=10000
    if plan.x>=1000:
        plan.x=-300
        plan.y=height//2+300
    person1.y+=person1.vy*dt
    if person1.y<height-190:
        person1.vy+=20*gra*dt
    if person1.y>height-190:
        person1.y=height-190
        person1.vy=0
    if pygame.key.get_pressed()[pygame.K_w] and person1.y==height-190:
        person1.vy=-600

    person2.y+=person2.vy*dt
    if person2.y<height-190:
        person2.vy+=20*gra*dt
    if person2.y>height-190:
        person2.y=height-190
        person2.vy = 0






    if ball.y >=height-90 and ball.x+20<=width//2:
        ball.y=100
        ball.x=width-300
        gr=0
        b+=1
        ball.vy=0
        ball.vx=0
        q1=True
        q2=True
        q3=True
        q4=True
        dv1=0
        dv2=0
        person1.y=height-190
        person2.y=height-190
        person1.x=width//2-190-l1
        person2.x=width//2+190
        score.x=width*3//4
    if ball.y >=height-90 and ball.x+20>=width//2:
        ball.y=100
        ball.x=300
        q1=True
        q2=True
        q3=True
        q4=True
        dv1=0
        dv2=0
        gr=0
        a+=1
        ball.vy=0
        ball.vx=0
        person1.y=height-190
        person2.y=height-190
        person1.x=width//2-190-l1
        person2.x=width//2+190
        score.x=width//4
    if ball.y + 40 >= person1.y and ball.y + 40 <= person1.y + abs(ball.vy*dt)+abs(person1.vy)+10:
        if ball.x + 20 >= person1.x and ball.x + 20 <= person1.x + l1 // 2.5:
            dv1+=1
            shlepok.play()
            if ball.y + 40 > person1.y:
                ball.y = person1.y - 40
            ball.vy = -ball.vy * 0.7 + person1.vy * 0.5
            ball.vx -= 100
        if ball.x + 20 >= person1.x + l1 // 2.5 and ball.x + 20 <= person1.x + l1 - l1 // 2.5:
            dv1+=1
            shlepok.play()
            if ball.y + 40 > person1.y:
                ball.y = person1.y - 40
            ball.vy = -ball.vy * 0.7 + person1.vy * 0.5

        if ball.x + 20 >= person1.x + l1 - l1 // 2.5 and ball.x + 20 <= person1.x + l1:
            dv1+=1
            shlepok.play()
            if ball.y + 40 > person1.y:
                ball.y = person1.y - 40
            ball.vy = -ball.vy * 0.7 + person1.vy * 0.5
            ball.vx += 300
    if ball.y + 40 >= person2.y and ball.y + 40 <= person2.y + abs(ball.vy*dt)+abs(person2.vy)+10:

        if ball.x + 20 >= person2.x and ball.x + 20 <= person2.x + l1 // 2.5:
            dv2+=1
            shlepok.play()
            if ball.y + 40 > person2.y:
                ball.y = person2.y - 40
            ball.vy = -ball.vy * 0.7 + person2.vy*0.3
            ball.vx -= 300
        if ball.x + 20 >= person2.x + l1 // 2.5 and ball.x + 20 <= person2.x + l1 - l1 // 2.5:
            dv2+=1
            shlepok.play()
            if ball.y + 40 > person2.y:
                ball.y = person2.y - 40
            ball.vy = -ball.vy * 0.7 + person2.vy*0.3

        if ball.x + 20 >= person2.x + l1 - l1 // 2.5 and ball.x + 20 <= person2.x + l1:
            dv2+=1
            shlepok.play()
            if ball.y + 40 > person2.y:
                ball.y = person2.y - 40
            ball.vy = -ball.vy * 0.7 + person2.vy * 0.3
            ball.vx += 100
    if ball.y + 40 >= person1.y + abs(ball.vy*dt)+abs(person1.vy)+10 and (ball.x+40+abs(ball.vx*dt)>=person1.x+person1.vx*dt or (ball.x-abs(ball.vx*dt)<=person1.x+l1+person1.vx*dt )):
        ball.vx=-ball.vx
    if ball.y + 40 >= person1.y + abs(ball.vy*dt)+abs(person1.vy)+10 and (ball.x+40+abs(ball.vx*dt)>=person1.x+person1.vx*dt or (ball.x-abs(ball.vx*dt)<=person1.x+l1+person1.vx*dt )):
        ball.vx=-ball.vx




    if ball.x >= width-40:
         ball.vx = -ball.vx
         ball.x -= 10
    if ball.x <= 0 :
        ball.vx = -ball.vx
        ball.x += 10


    if ball.x +40>= stolb.x-abs(ball.vx*dt)-5 and ball.y+20>=stolb.y and ball.x<=stolb.x+30+abs(ball.vx*dt)+5:
        if ball.vx>0 and ball.x<=width//2:
            ball.x-=10
        if ball.vx<=0 and ball.x>=width//2:
            ball.x+=10
        ball.vx = -ball.vx
    if ball.x +20>= stolb.x-abs(ball.vx*dt)  and ball.y+40>=stolb.y-abs(ball.vy*dt) and ball.x+20<=stolb.x+30+abs(ball.vx*dt):
        ball.y-=abs(ball.vy*dt)
        ball.vy=-abs(ball.vy)




    if ball.x +40>= person1.x and ball.y+20>=person1.y+20 and ball.x+40<=person1.x+l1//2:
         ball.vx = -ball.vx
         ball.x -= 5
         ball.vy+=10


    if ball.y<=0:
        tr.x=ball.x
    else:
        tr.x=-300


    if ball.x+20<=width//2:
        dv2=0
    if ball.x+20>=width//2:
        dv1=0
    if dv2==5:
        ball.y=3000
        foul.x=width*3//4
    if  dv1==5:
        ball.y=3000
        foul.x=width//4

    if foul.x==width//4 or foul.x==width*3//4 :
        dvt+=1
    if dvt==10:
        dvt=0
        foul.x=3000
    if score.x==width//4 or score.x==width*3//4 :
        time+=1
    if time==10:
        time=0
        score.x=3000

    info_string.fill(na_fon)
    pygame.display.update()
    foul.render()
    ship1.render()
    ship2.render()
    person1.render()
    person2.render()
    ball.render()
    stolb.render()
    plan.render()
    tr.render()
    score.render()
    info_string.blit(inf_font.render(u''+str(a)+':'+str(b), 1,(0,250,200)),(width//2-14,0))
    window.blit(info_string, (0,0))
    window.blit(screen, (0, 30))
    pygame.display.flip()




