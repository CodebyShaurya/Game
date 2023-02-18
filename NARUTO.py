import pygame
global x,y
import sys
from random import randint


def image (imag,a,b):
        back = pygame.image.load(imag)
        face.blit(back, (a,b))


def printing (what):
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(what, True, (0, 255, 0))
        screen.blit(textsurface,(0,0))

def exits ():
        screen.fill(a)
        printing('you lose ')
        score=0
        printing('                    Press p to exit')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p :
                    gameexit=True
                    gameover=True
                    pygame.quit()
                    sys.exit()



'''                                                    assinging cordinates'''
x=11
y=11
q=20

score=0
width=10

a=[0,0,255]
pygame.init()

v = randint(0, 800)
z=randint(0, 450)

letx = randint(0, 800)
lety=randint(0, 450)
gameexit=False
gameover=False


'''                                          CREATE A SCREEN '''


screen=pygame.display.set_mode((860,500))
pygame.display.set_caption('Naruto Evolution')
icon= pygame.image.load('naruto six paths sage mode.png')

face=pygame.display.get_surface()
face.fill(a)

pygame.display.flip()


'''                                              START THE GAME
'''

while not gameexit:
    timer=pygame.time.Clock()
    timer.tick(4)


    

    while gameover==True:
        exits()
        
    for event in pygame.event.get():
       
              
                pygame.display.update()
                scorestr=str(score)
                msg= 'RAMEN EATEN : '+scorestr
                image('57bdcc9f0d5fc_57bdcc8e0c067_930312360.jpg',0,0)
                letx=letx-10
                lety=lety-10
                if letx<-45 or lety<-109:
                        letx = randint(0, 800)
                        lety=randint(0, 450)
                printing(msg)
                if score>=2 and score<5:
                        image('narutolvl 2.png',x,y)
                elif score>=5 and score<8:
                        image('naruto six paths sage moder.png',x,y)
                elif score>=8:
                        image('31-313692_naruto-road-to-boruto-naruto-removebg-preview.png',x,y)
                else:
                        image('narutokid.png',x,y)
                image('png-clipart-japanese-cuisine-ramen-narutomaki-ingredient-others-miscellaneous-food-thumbnail.png',v,z)
                if score>= 2 and score<4:
                        image('Kurama_Render-removebg-preview.png',letx,lety)
                elif score>=4 and score<7:
                        image('Sasuke_Uchih a.png',letx,lety)
                elif score>=7:
                        image('png-clipart-pain-konan-sasori-deidara-obito-uchiha-body-pain-fictional-character-pain-removebg-preview.png',letx,lety)
                
                        
                
                
                print(event)
                if event.type== pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w :
                        y=y-10
                    elif event.key == pygame.K_s:
                        y=y+10
                    elif event.key == pygame.K_a :
                        x=x-10
                    elif event.key == pygame.K_d :
                        x=x+10
                if  y<=-45:
                        print('y coordinate')
                        exits()
                elif x<-109:
                        print('X coordinate')
                        exits()
                

                elif y in range(z-75 ,z+75) and x in range(v-125,v) :
                    score=score+1

                    v = randint(10, 800)
                    z=randint(10, 450)
                    letx = randint(10, 800)
                    lety=randint(10, 450)



                if score>=2:
                    if x in range (letx-135,letx+75) and y in range (lety-75,lety+133) :
                        print('Hit the enemy')
                        exits()
                    

