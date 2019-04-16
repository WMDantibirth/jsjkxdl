from turtle import *
from math import *
import os
ran=50
rad=0.5
step=1000
tim=0.005
def bg():
    pu()
    goto(-ran*10,0)
    pd()
    pencolor("grey")
    goto(ran*10,0)
    pu()
    for i in range(-9,10):
        pu()
        goto(ran//10*i*10,3)
        pd()
        goto(ran//10*i*10,-3)
        pu()
    goto(0,ran*10)
    pd()
    pencolor("grey")
    goto(0,-ran*10)
    pu()
    for i in range(9,-10,-1):
        pu()
        goto(3,ran//10*i*10)
        pd()
        goto(-3,ran//10*i*10)
        pu()
    for i in range(-ran,ran,2):
        pu()
        goto(i*10,ran*10)
        pd()
        goto(i*10+5,ran*10)
        pu()
    for i in range(ran,-ran,-2):
        pu()
        goto(ran*10,i*10)
        pd()
        goto(ran*10,i*10-5)
        pu()
    for i in range(ran,-ran,-2):
        pu()
        goto(i*10,-ran*10)
        pd()
        goto(i*10-5,-ran*10)
        pu()
    for i in range(-ran,ran,2):
        pu()
        goto(-ran*10,i*10)
        pd()
        goto(-ran*10,i*10+5)
        pu()
def writ(s):
    print()
    print()
    f=open(s,'r');
    for i in f.readlines():
        print(i)
    print()
def dcir(x,y,r):
    pu()
    goto(x*10,(y-r)*10)
    pd()
    circle(r*10)
def wdir(s):
    s2=""
    for i in range(len(s)):
        if i>6:
            s2+=s[i]
    L=s2.split(".")
    if len(L)==2 and L[1]=="mpsv":
        print(L[0])
        print()
def view():
    print()
    print("Current available maps are:")
    print()
    fs=os.listdir("./maps")
    for i in fs:
        wdir(os.path.join("./maps",i))
def maps():
    a=0
def crash(n,stars,x,y):
    if abs(x)>ran or abs(y)>ran:
        return 1
    for i in range(n):
        dx=stars[i][0]-xx
        dy=stars[i][1]-yy
        dis=sqrt(dx**2+dy**2)
        if dis<=stars[i][2]:
            return 1
    return 0
def goal(x1,y1,x2,y2):
    dx=x1-x2; dy=y1-y2;
    return dx**2+dy**2<=rad**2
def shoot(n,star,x1,y1,x2,y2,vx,vy):
    pu()
    goto(x1*10,y1*10)
    pd()
    xx,yy=x1,y1
    for i in range(step):
        ax,ay=0,0
        for j in range(n):
            dx=star[j][0]-xx
            dy=star[j][1]-yy
            dis=sqrt(dx**2+dy**2)
            a=star[j][3]/(dx**2+dy**2)*5
            ax+=a/dis*dx; ay+=a/dis*dy
        vx+=ax*tim; vy+=ay*tim
        xx+=vx*tim; yy+=vy*tim
        goto(xx*10,yy*10)
        for j in range(n):
            dx=star[j][0]-xx
            dy=star[j][1]-yy
            dis=sqrt(dx**2+dy**2)
            if dis<=star[j][2]:
                return 0
        dx=x2-xx
        dy=y2-yy
        dis=sqrt(dx**2+dy**2)
        if dis<=0.5:
            return 1
        if abs(xx)>ran or abs(yy)>ran:
            return 0
    return 0
def leag(x,y,star,n):
    if abs(x)>ran or abs(y)>ran:
        return 0
    for i in range(n):
        dx=star[i][0]-x
        dy=star[i][1]-y
        dis=sqrt(dx**2+dy**2)
        if dis<=star[i][2]:
            return 0
    return 1
def game():
    writ("./game/home.txt")
    while 1:
        while 1:
            L=input().split()
            if len(L)==0 or len(L)>0 and L[0]!="/view" and L[0]!="/choose" and L[0]!="/rule" and L[0]!="/home":
                if len(L)>0 and L[0]=="/help":
                    writ("./game/help.txt")
                else:
                    writ("./error.txt")
            else:
                break
        if L[0]=="/view":
            view()
            continue
        if L[0]=="/choose":
            try:
                f=open("./maps/"+L[1]+".mpsv",'r')
            except:
                print()
                print("There's no such map")
                print()
                continue
            else:
                n=int(f.readline().strip())
                star=[]
                color("black")
                for i in range(n):
                    x,y,r,m=list(map(float,f.readline().strip().split()))
                    star.append([x,y,r,m])
                    dcir(x,y,r)
                    pu()
                    goto(x*10-12,y*10-4)
                    write(str(m))
                print()
                print("/ok if this map is ok")
                print()
                if input()=="/ok":
                    break
                else:
                    clear()
                    writ("./game/ng.txt")
                    continue
        if L[0]=="/rule":
            writ("./game/rule.txt")
            continue
        if L[0]=="/home":
            return
    print()
    print("Please input two numbers split by a blank, which represents the position (x, y) of Player 1's spacecraft.")
    print()
    while 1:
        L=input().split()
        if len(L)!=2:
            print()
            print("Are you sure you inputed exactly two numbers split by a blank?")
            print()
            continue
        try:
            x1=float(L[0])
            y1=float(L[1])
        except:
            print()
            print("Are you sure you inputed exactly two numbers split by a blank?")
            print()
        else:
            print(x1,y1)
            if leag(x1,y1,star,n):
                break
            else:
                print()
                print("A spacecraft cannot be into a planet or out of the board.")
                print()
    color("red")
    dcir(x1,y1,0.5)
    print()
    print("Please input two numbers split by a blank, which represents the position (x, y) of Player 2's spacecraft.")
    print()
    while 1:
        L=input().split()
        if len(L)!=2:
            print()
            print("you should input exactly two numbers split by a blank.")
            print()
            continue
        try:
            x2=float(L[0])
            y2=float(L[1])
        except:
            print()
            print("you should input exactly two numbers split by a blank.")
            print()
        else:
            if leag(x2,y2,star,n):
                break
            else:
                print()
                print("A spacecraft cannot be into a planet or out of the board.")
                print()
    color("blue")
    dcir(x2,y2,0.5)
    writ("./game/start.txt")
    i=1; end=0
    while 1:
        if end:
            break
        if i:
            print("Player 1's turn:")
        else:
            print("Player 2's turn:")
        while 1:
            L=input().split()
            if len(L)==0 or len(L)>0 and L[0]!="/shoot" and L[0]!="/move" and L[0]!="/leave":
                if len(L)>0 and L[0]=="/help":
                    writ("./game/help2.txt")
                else:
                    writ("./error.txt")
            if L[0]=="/shoot":
                try:
                    v,ang=float(L[1]),float(L[2])
                    ang=ang%360
                    ang=ang/180*3.1415926535897932384626
                except:
                    print()
                    print("If you want to shoot, you should input two numbers which represents the speed and the angle of the bullet.")
                    print()
                    continue
                else:
                    if i:
                        color("red")
                        if shoot(n,star,x1,y1,x2,y2,v*cos(ang),v*sin(ang)):
                            print("Congratulations! Player 1 won the game!")
                            end=1
                        break
                    else:
                        color("blue")
                        if shoot(n,star,x2,y2,x1,y1,v*cos(ang),v*sin(ang)):
                            print("Congratulations! Player 2 won the game!")
                            end=1
                        break
            if L[0]=="/move":
                try:
                    x,y=float(L[1]),float(L[2])
                except:
                    print()
                    print("If you want to move, you should input two numbers which represents the position of the spacecraft.")
                    print()
                    continue
                else:
                    if not leag(x,y,star,n):
                        print()
                        print("A spacecraft cannot be into a planet or out of the board.")
                        print()
                        continue
                    if i:
                        color("grey")
                        dcir(x1,y1,0.5)
                        x1,y1=x,y
                        color("red")
                        dcir(x1,y1,0.5)
                    else:
                        color("grey")
                        dcir(x2,y2,0.5)
                        x2,y2=x,y
                        color("blue")
                        dcir(x2,y2,0.5)
                    break
            if L[0]=="/leave":
                if i:
                    print("Player 1 surrendered, Player 2 wins!")
                else:
                    print("Player 2 surrendered, Player 1 wins!")
                end=1
                break
        i=not i
    print("Input anything to return to home page")
    print()
    input()
    reset()
hideturtle()
#bg()
while 1:
    pensize(2)
    writ("./home.txt")
    while 1:
        pensize(2)
        read=input();
        if read!="/maps" and read!="/start" and read!="/info" and read!="/quit":
            if read=="/help":
                writ("./help.txt")
            else:
                writ("./error.txt")
        else:
            break
    if read=="/maps":
        maps()
        continue
    if read=="/start":
        game()
        continue
    if read=="/info":
        writ("./info.txt")
        print("Input any word to return to home page")
        print()
        input()
        continue
    if read=="/quit":
        break
writ("./thanks.txt");
