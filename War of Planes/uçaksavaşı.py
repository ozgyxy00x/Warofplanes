
from pygame import Actor,screen,keyboard,mouse
import random

#YAPILMASI GEREKENLER




WIDTH = 600
HEIGHT = 300


TITLE = 'Uçak Savaşı'

FPS = 100

mod = 'menü'

oynab = Actor("oyna", pos=(300, 120))

htplay = Actor("htplaybutton",(300,190))

isim = Actor("Adsız",(500,5))

buttons = Actor("buttonLarge",(300,40))

wht = Actor("htpw",(150,150))

btmenu = Actor("btmenu",(300,250))

btsettingg = Actor("btsetting",(100,250))

easybutton = Actor("easy",(125,150))

normalbutton = Actor("normal",(300,150))

hardbutton = Actor("hard",(475,150))

#healt = Actor("healt",(50,250))

imlec = Actor("tap") 



ap = Actor("arkaplan")


madalyab = Actor("medalBronze",(550,50))

madalyas = Actor("medalSilver",(550,50))

madalyaa = Actor("medalGold",(550,50))



starb = Actor("starBronze",(475,50))

stars = Actor("starSilver",(475,50))

starg = Actor("starGold",(475,50))



planegreen1 = Actor("planeGreen1",(50,150))

#planegreen2 = Actor("planeGreen2")

#planegreen3 = Actor("planeGreen3")



planered1 = Actor("planered")

#planered2 = Actor("planeRed2")

#planered3 = Actor("planeRed3")



planeyellow1 = Actor("planeyellow")

#planeyellow2 = Actor("planeYellow2")

#planeyellow3 = Actor("planeYellow3")



planeblue1 = Actor("planeblue")

#planeblue2 = Actor("planeBlue2")

#planeblue3 = Actor("planeBlue3")

planect = "planegreen1"







#bak = Actor("puffSmall")
#bab = Actor("puffLarge")

ilerle = Actor("tapRight")
gameovertext = Actor("textGameOver",(300,150))
getreadytext = Actor("textGetReady",(300,250))

dusmanlar=[]
fuzeler=[]

x = 0
mermi = 50
puan = 0
z = 0
hiz = 5

def draw():
    
    global mod,x
    
    
    
    if mod == 'menü':
        
        ap.draw()
        
        oynab.draw()
        
        getreadytext.draw()
        
        buttons.draw()
        
        htplay.draw()
        
        isim.draw()
        
        imlec.draw()
        
    elif mod == 'setting':
        
        ap.draw()
        
        screen.draw.text('ENEMY SPEED',center = (300,50),color ='#2926e0',fontsize = 50)
        
        btsettingg.draw()
        
        easybutton.draw()
        
        normalbutton.draw()
        
        hardbutton.draw()
        
        isim.draw()
        
        imlec.draw()
        
    elif mod == 'htp':
        
        ap.draw()
        
        wht.draw()
        
        isim.draw()
        
    elif mod == 'oyun':
        
        ap.draw()
    #<ap2.draw()
        planegreen1.draw()
        
        
        
        
        
            
        for i in range(len(dusmanlar)):
                    dusmanlar[i].draw()
            
                
        for i in range(len(fuzeler)):
                fuzeler[i].draw()
            
        screen.draw.text(puan,center = (30,30),color= 'black', fontsize = 50)
        
        screen.draw.text(mermi,center = (575,275),color = '#d6511c',fontsize = 45)
        
        if puan >= 25 and puan <= 49:
            madalyab.draw()
        if puan >= 35 and puan <= 59:
            starb.draw()
        if puan >= 50 and puan <= 74:
            madalyas.draw()
        if puan >= 60 and puan <= 99:
            stars.draw()
        if puan >= 75 :
            madalyaa.draw()
        if puan >= 100 :
            starg.draw()
                
        #healt.draw()
        
    elif mod == 'son':
        
        ap.draw()
        #screen.draw.text("OYUN BİTTİ!", center = (300, 150), color = "black", fontsize = 50)
        gameovertext.draw()
        
        btmenu.draw()
        
        imlec.draw()
        
if puan >= 50:
        FPS =+ 25        
    
for i in range(2):
    
    y = random.randint(0,HEIGHT)
    x = random.randint(WIDTH,WIDTH+100)
    planered1 = Actor("planered", (x, y))
    planered1.speed = hiz
    dusmanlar.append(planered1)
    
for i in range(2):
    
    y = random.randint(0,HEIGHT)
    x = random.randint(WIDTH,WIDTH+100)
    planeyellow1 = Actor("planeyellow", (x, y))
    planeyellow1.speed = hiz
    dusmanlar.append(planeyellow1)
    
for i in range(2):
    
    y = random.randint(0,HEIGHT)
    x = random.randint(WIDTH,WIDTH+100)
    planeblue1 = Actor("planeblue", (x, y))
    planeblue1.speed = hiz
    dusmanlar.append(planeblue1)
    
def kontrol():
    if (keyboard.w or keyboard.up) and planegreen1.y > 25 :
        planegreen1.y -= 5
    elif (keyboard.s or keyboard.down) and planegreen1.y < 275:
        planegreen1.y += 5 
    
        
def redplane():
    for i in range(len(dusmanlar)):
        if dusmanlar[i].x > -50 :
            dusmanlar[i].x -= dusmanlar[i].speed
        else:
            dusmanlar.pop(i)
            yeni_dusmanblue()
            
def yeni_dusmanblue():
    x = random.randint(WIDTH,700)
    y = random.randint(0,HEIGHT)
    plane =random.choice(['planeblue','planered','planeyellow'])
    planeblue1 = Actor(plane, (x, y))
    planeblue1.speed = hiz
    dusmanlar.append(planeblue1)


def posa():
    global x,puan,mermi
    
    planegreen1.pos = (50,150)
    puan = 0
    mermi = 50
    
def carpismalar():
    
    global mod,puan,mermi
    
    for i in range(len(dusmanlar)):
        if planegreen1.colliderect(dusmanlar[i]):
            mod = 'son'
        
        for j in range(len(fuzeler)):
            if fuzeler[j].colliderect(dusmanlar[i]):
                
                    
                
                
                if z == 2:
                    
                    dusmanlar.pop(i)
                    fuzeler.pop(j)
                    mermi += 3
                    puan += 1
                    yeni_dusmanblue()
                    yeni_dusmanblue()
                    break
                
                if z == 3:
                    
                    dusmanlar.pop(i)
                    fuzeler.pop(j)
                    mermi += 4
                    puan += 2
                    yeni_dusmanblue()
                    yeni_dusmanblue()
                    break
            
                else:
                    
                    dusmanlar.pop(i)
                    fuzeler.pop(j)
                    mermi += 2
                    puan += 1
                    yeni_dusmanblue()
                    yeni_dusmanblue()
                    break
            #else:
                #mermi -= 1
            
    
def update(dt):
    global mod,z
    
    if mod== 'oyun':
        
        kontrol()
        redplane()
        carpismalar()
    
        
    
        
        
        
    
            
    for i in range(len(fuzeler)):
        if fuzeler[i].x < 0 :
            fuzeler.pop(i)
            draw()
            break
        else:
            fuzeler[i].x = fuzeler[i].x + 26
    
def on_mouse_move(pos):
    imlec.pos = pos
def on_mouse_down(button,pos):
    global mod,z,hiz
    if mermi > 0 :
    
        if mod == 'oyun' and button == mouse.LEFT :
            fuze = Actor("füzeler")
            fuze.pos = planegreen1.pos
            fuzeler.append(fuze)
            
    if oynab.collidepoint(pos) and mod == 'menü' :

        mod = "oyun"
        
        #mlec.image = 'tapTick'
        
    if  mod == 'son' and btmenu.collidepoint(pos) :
        
        mod = 'menü'
        posa()
        dusmanlar[:] = []
        fuzeler[:] = []
        yeni_dusmanblue()
        
        #imlec.image = 'tapTick'
        
    if buttons.collidepoint(pos) and mod == 'menü' :
        
        mod = 'setting'
        
        #mlec.image = 'tapTick'
        
    if btsettingg.collidepoint(pos) and mod == 'setting' :
        
        mod = 'menü'
        
        #imlec.image = 'tapTick'
        
    if easybutton.collidepoint(pos) and mod == 'setting' :
        
        hiz = random.randint(1,5)
        
        z = 1
        
        #imlec.image = 'tapTick'
        
    if normalbutton.collidepoint(pos) and mod == 'setting' :
        
        hiz = random.randint(5,10)
        
        z = 2
        
        imlec.image = 'tapTick'
        
    if hardbutton.collidepoint(pos) and mod == 'setting' :
        
        hiz = random.randint(10,15)
        
        z = 3
        
        #imlec.image = 'tapTick'
        
    if htplay.collidepoint(pos) and mod == 'menu':
        
        mod = 'htp'
        
    #if (htplay.collidepoint(pos) and mod == 'menü') or (hardbutton.collidepoint(pos) and mod == 'setting') or (normalbutton.collidepoint(pos) and mod == 'setting') or (easybutton.collidepoint(pos) and mod == 'setting') or (btsettingg.collidepoint(pos) and mod == 'setting') or (buttons.collidepoint(pos) and mod == 'menü') or (mod == 'son' and btmenu.collidepoint(pos)) or (oynab.collidepoint(pos) and mod == 'menü') or ()
        
        #imlec.image = 'tapTick'
        
    #if  mod == 'son' and btmenu.collidepoint(pos) :
        
        #imlec.image = 'tapTick'
        
    #else:
        #imlec.image = "tap"





        
        
    
