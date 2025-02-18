import pygame
pygame.init()
speed = [0,0]
screen=pygame.display.set_mode((1700,950))
cal=pygame.image.load("cal.png")
MUSIC=pygame.mixer.music.load("MUSIC.wav")
BOBA_FETT=pygame.image.load("BOBA FETT AND PLES DONT SUE ME.png")
WEAPON=pygame.image.load("weapon-of-BOBA-FETT-AND-PLES-DONT-SUE-ME.png")
Darth_Zannah_lightsaber=pygame.image.load("Darth Zannah lightsaber.png")
Darth_Zannah=pygame.image.load("Darth Zannah.png")
good_man=pygame.image.load("i am iorn man.png")
refleted=False
msb=pygame.image.load("master_sword_btow.png")
msb_rect=msb.get_rect()
msb=pygame.transform.scale(msb,(200,150))
WEAPON=pygame.transform.scale(WEAPON,(400,450))
i_ran_out_of_names=pygame.image.load("i_am_god_dun_dun_dun_un_habgesa_shool_sucks.png")
boko=pygame.image.load("boko tiko.png")
ball=pygame.image.load("ballllll.png")
gun=pygame.image.load("balster.png")
dark=pygame.image.load("dark saber.png")
crossguard=pygame.image.load("crossguard.png")
crossguard=pygame.transform.scale(crossguard,(130,230))
dark=pygame.transform.scale(dark,(100,230))
gun=pygame.transform.scale(gun,(50,45))
gunrect=gun.get_rect()
darkrect=dark.get_rect()
crossguardrect=crossguard.get_rect()
pygame.mixer.music.play(-1)
baton=pygame.image.load("weapon-of-the-stormtrooper-removebg-preview.png")
stone=pygame.image.load("stone.jpg")
kijimi=pygame.image.load("kijimi.png")
stormtrooper=pygame.image.load("stormtrooper.png")
stormtroopers=[]
stormtroopers_rect=[]
sith_cal_health=500
lightsaber_clash=pygame.mixer.Sound("lightsaber-clash.wav")
saber_hummingwav=pygame.mixer.Sound("saber-hummingwav.wav")
stormtrooperhealths=[]
sith_cal=pygame.image.load("sith cal.png")
sith_lightsaber=pygame.image.load("sith cal's litghtsaber.png")
Darth_Zannah_lightsaber=pygame.transform.flip(Darth_Zannah_lightsaber,True,False)
sineing=False
ball_rect=ball.get_rect()
air_to_ground=True
Darth_Zannah_lightsaber=pygame.transform.scale(Darth_Zannah_lightsaber,(170,170))
Darth_Zannah=pygame.transform.scale(Darth_Zannah,(230,330))
sith_cal=pygame.transform.scale(sith_cal,(230,330))
sith_lightsaber=pygame.transform.scale(sith_lightsaber,(150,289))
cal=pygame.transform.scale(cal, (650,450))
kijimi=pygame.transform.scale(kijimi,(1700,950))
stone=pygame.transform.scale(stone,(1700,100))
Darth_Zannah_lightsaber_rect=Darth_Zannah_lightsaber.get_rect()
Darth_Zannah_rect=Darth_Zannah.get_rect()
BOBA_FETT=pygame.transform.scale(BOBA_FETT,(230,350))
BOBA_FETT_rect=BOBA_FETT.get_rect()
BOBA_FETT_rect.bottom=865
BOBA_FETT_rect.right=1700
stone_rect=stone.get_rect()
stone_rect.y = 850
cal_rect = cal.get_rect()
boko_rect=boko.get_rect()
sith_lightsaber_rect=sith_lightsaber.get_rect()
sith_cal_rect=sith_cal.get_rect()
stormtrooper_rect = stormtrooper.get_rect()
stormtrooper_rect=stormtrooper_rect.move(946,449)
stormtrooperhealth=5
baton=pygame.transform.scale(baton,(200,250))
baton_rect=baton.get_rect()
calhealth=30000
WEAPON_rect=WEAPON.get_rect()
baton_rect=baton_rect.move(800,450)
Darth_Zannah_lightsaber_rect.right=1600
Darth_Zannah_lightsaber_rect.bottom=700
shot=pygame.image.load("shot.png")
shot_rect=shot.get_rect()
ammo=101
Darth_Zannah_rect.right=1700                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
cal_rect.bottom =865
boko_rect.right=1700                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
boko_rect.bottom =865
ball_rect.center=boko_rect.center
Darth_Zannah_rect.bottom=865
sith_cal_rect.bottom=865
sith_cal_rect.right=1700
sith_lightsaber_rect.bottom=840
sith_lightsaber_rect.right=1550
lightsaber=pygame.image.load("duble.png")
lightsaber=pygame.transform.scale(lightsaber, (300,275))
lightsaber=pygame.transform.rotate(lightsaber,45)
lightsaber_rect=lightsaber.get_rect()
Bhealth=500
lightsaber_rect.x =20
lightsaber_rect.bottom =750
#stormtroopers_rect
level=1
jumpdealy=155
grounded=False
rotate = 0
atdelay=60
#what did i do here 60,70 ok but i am not taking because
atcounter=0
aiphase=0
def __init__(self):
    self.last = pygame.time.get_ticks()
    self.cooldown = 500    
sabertime=180
def move(self):
   # fire gun, only if c,ooldown has been 0.3 seconds since last
    now = pygame.time.getticks()
    if now - self.last >= self.cooldown:
        self.last = now,
lightsabers=[lightsaber,dark,gun,crossguard,msb,good_man,i_ran_out_of_names]
current_lightsaber=0
bash= False
# look at while true 
font=pygame.font.SysFont(None,30)
while True:    
    if sineing==True:
        atcounter+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            
    keys = pygame.key.get_pressed()
    if grounded==True:
        if keys[pygame.K_s]:
            current_lightsaber+=1
            if current_lightsaber>5:
                current_lightsaber=0
        if keys[pygame.K_UP] and jumpdealy<0:
            jumpdealy=150
            cal_rect = cal_rect.move(0, -2000)
            #lightsaber_rect = lightsaber_rect.move(0, -20)
            
    jumpdealy-=1
    
    if keys[pygame.K_RIGHT] and not keys [pygame.K_a]:
        cal_rect = cal_rect.move(3, 0)
        #lightsaber_rect = lightsaber_rect.move(1, 0)

    if keys[pygame.K_LEFT]  and not keys [pygame.K_a]:
        cal_rect = cal_rect.move(-3, 0)
        #lightsaber_rect = lightsaber_rect.move(-1, 0)
    sabertime-=1
    if keys  [pygame.K_SPACE] and sabertime<0 and not current_lightsaber==2   :
        lightsaber_clash.play()
        sabertime=600
        if sineing==False:
            sineing=True
            #lightsaber = pygame.transform.rotate(lightsaber,-90)
            atcounter=0
    if keys [pygame.K_d] and not keys [pygame.K_a]:
        cal_rect = cal_rect.move(-5, 0)
    if keys [pygame.K_x] and not keys [pygame.K_a]:
        cal_rect = cal_rect.move(5, 0)

    if current_lightsaber==2 and keys [pygame.K_SPACE] and ammo>0 and bash==False :
        ammo-=1
        bash=True
        shot_rect.center=[cal_rect.right-60, cal_rect.y +200]
    if bash==True:
        shot_rect=shot_rect.move(50,0)
        if shot_rect.left>1600:
            bash=False
    if aiphase==0:
        
        if cal_rect.x>stormtrooper_rect.x:
            stormtrooper_rect=stormtrooper_rect.move(2, 0)
            baton_rect=baton_rect.move(2, 0)
        if cal_rect.x<stormtrooper_rect.x:    
            stormtrooper_rect=stormtrooper_rect.move(-2, 0)
            baton_rect=baton_rect.move(-2, 0)
    if baton_rect.colliderect(cal_rect) and len(stormtroopers)>0:
        if not keys [pygame.K_a]:
            calhealth-=13 
        else :
            
            saber_hummingwav.play()
    else:
        saber_hummingwav.stop()
    if sineing:
        if current_lightsaber==0:
            lightsaber_rect.center = [cal_rect.right-120, cal_rect.y +200]
        if current_lightsaber==1:
            lightsaber_rect.center = [cal_rect.right-1, cal_rect.y +200]
        if current_lightsaber==2:
            lightsaber_rect.center = [cal_rect.right-120, cal_rect.y +450]
        if current_lightsaber==3:
            lightsaber_rect.center = [cal_rect.right-120, cal_rect.y +200]
        if current_lightsaber==4:
            lightsaber_rect.center = [cal_rect.right-39,cal_rect.y+279]
        if current_lightsaber==5:
            lightsaber_rect.center = [cal_rect.right-90,cal_rect.y+230]
        if current_lightsaber==6:
            lightsaber_rect.center = [cal_rect.right-110,cal_rect.y+190]
    else:
        if current_lightsaber==0:
            lightsaber_rect.center = [cal_rect.right-240, cal_rect.y +200]
        if current_lightsaber==1:
            lightsaber_rect.center = [cal_rect.right-50, cal_rect.y +200]
        if current_lightsaber==2:
            lightsaber_rect.center = [cal_rect.right-60, cal_rect.y +450]
        if current_lightsaber==3:
            lightsaber_rect.center = [cal_rect.right-120, cal_rect.y +200]
        if current_lightsaber==4:
            lightsaber_rect.center = [cal_rect.right-110,cal_rect.y+331]
        if current_lightsaber==5:
            lightsaber_rect.center = [cal_rect.right-130,cal_rect.y+230]
        if current_lightsaber==6:
            lightsaber_rect.center = [cal_rect.right-160,cal_rect.y+190]
    
    if aiphase==0 and level== 5:
        if cal_rect.x>BOBA_FETT_rect.x:
            BOBA_FETT_rect=BOBA_FETT_rect.move(2, 0)
            #baton_rect=baton_rect.move(2, 0)
        if cal_rect.x<BOBA_FETT_rect.x:    
            BOBA_FETT_rect=BOBA_FETT_rect.move(-2, 0)
           # baton_rect=baton_rect.move(-2, 0)
    
    if atcounter >= atdelay:
        sineing = False
        #lightsaber = pygame.transform.rotate(lightsaber, 90)
        atcounter = 55
    if len(stormtrooperhealths)>0 and lightsaber_rect.colliderect(stormtroopers_rect[0]) and sineing:
        stormtrooperhealths[0]-=5        
        sineing=False
    if  len(stormtrooperhealths)>0 and current_lightsaber==2 and shot_rect.colliderect(stormtroopers_rect[0]) and bash:
        stormtrooperhealths[0]-=5
    if cal_rect.colliderect(stone_rect):
        cal_rect.bottom = 870

        grounded=True    

    if cal_rect.top<0:
        cal_rect.top=0
                       
    cal_rect = cal_rect.move(0, 5)
    lightsaber_rect = lightsaber_rect.move(0, 5)
    if cal_rect.right>=1700:
        if level==5:
            if Bhealth<=0:
                level+=1

                cal_rect.left=0
                stormtrooperhealth=5
                stormtroopers=[]
                stormtroopers_rect=[]
                stormtrooperhealths=[] 
                for P in range (level):
                    stormtrooperhealths.append(5)
                    stormtroopers.append(stormtrooper)
                    rect=stormtrooper_rect.move(P*19.9,0)
                    stormtroopers_rect.append(rect)
                stormtrooperhealth=5*level

        else:        
            level+=1

            cal_rect.left=0
            stormtrooperhealth=5
            stormtroopers=[]
            stormtroopers_rect=[]
            stormtrooperhealths=[] 
            for P in range (level):
                stormtrooperhealths.append(5)
                stormtroopers.append(stormtrooper)
                rect=stormtrooper_rect.move(P*19.9,0)
                stormtroopers_rect.append(rect)
            stormtrooperhealth=5*level
    if calhealth<0:
        pygame.quit()
    screen.blit(kijimi, (0,0))
  # if level==8:
#
    if level==9:
        if sith_cal_rect.x>cal_rect.x+399:
            sith_cal_rect.x-=1
        if sith_cal_rect.x+399<cal_rect.x:
            sith_cal_rect.x+=1
        sith_lightsaber_rect.center=sith_cal_rect.center
        if shot_rect.colliderect(sith_cal_rect) and bash:
            sith_cal_health-=25
        if lightsaber_rect.colliderect(sith_cal_rect) and sineing:
            sith_cal_health-=25
        if sith_cal_health>=0:
            if cal_rect.colliderect(sith_lightsaber_rect):
                calhealth-=25
            screen.blit(sith_cal,sith_cal_rect)
            screen.blit(sith_lightsaber,sith_lightsaber_rect)
    if level==10:
        screen.blit(Darth_Zannah,Darth_Zannah_rect)
        screen.blit(Darth_Zannah_lightsaber,Darth_Zannah_lightsaber_rect)
        print ("ten")
    if level==11:
        if lightsaber_rect.colliderect(ball_rect) and keys[pygame.K_z] and not refleted and current_lightsaber==4:
            refleted=True
        if ball_rect.right<0 or ball_rect.left>screen.get_width():
            ball_rect.x=boko_rect.x
            refleted=False
        else:
            if refleted:
                ball_rect.x+=12
            else:
                ball_rect.x-=12
        screen.blit(boko,boko_rect)
        screen.blit(ball,ball_rect)
    if level==5 and Bhealth>0:
        if BOBA_FETT_rect.x>cal_rect.x+399:
            BOBA_FETT_rect.x-=1
        if BOBA_FETT_rect.x+399<cal_rect.x:
        
            BOBA_FETT_rect.x+=1
        WEAPON_rect.center=BOBA_FETT_rect.center
        if WEAPON_rect.colliderect(cal_rect):
            calhealth-=3
        if lightsaber_rect.colliderect(BOBA_FETT_rect) and sineing:
            Bhealth-=25
            sineing=False
        if shot_rect.colliderect(BOBA_FETT_rect) and bash:
            Bhealth-=25
            bash=False
        screen.blit(BOBA_FETT,BOBA_FETT_rect) 
        screen.blit(font.render(str(Bhealth),True,"red"),BOBA_FETT_rect)
        screen.blit(WEAPON,WEAPON_rect)
    screen.blit(stone,stone_rect)
    screen.blit(cal,cal_rect)
    if bash==True:
        screen.blit(shot,shot_rect)
    #for Su in  range (len (stormtroopers)): 
    if len(stormtrooperhealths)>0 and stormtrooperhealths[0]>0:
     
        screen.blit(stormtroopers[0],stormtroopers_rect[0])
        screen.blit(baton, baton_rect)
    elif len(stormtrooperhealths)>0 and stormtrooperhealths[0]<1:
        stormtroopers.pop(0)
        stormtroopers_rect.pop(0)
        stormtrooperhealths.pop(0)
    screen.blit(lightsabers[current_lightsaber],lightsaber_rect)
    pygame.transform.scale(lightsaber, (200, 150))
    pygame.display.flip()

#find out the real name of the master_sword  
#bater
# 20 for boss 27 for fnle boss
#death mine game 