import pygame
import time

pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

car_width = 73

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('car game')

black = (255,0,0)
white = (255,255,255)
red = (0,0,0)
green = (0,255,0)
blue = (0,0,255)


clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')
carImg1 = pygame.image.load('racecar1.png')
gameIcon = pygame.image.load('carIcon.png')

pygame.display.set_icon(gameIcon)

def borders(gameDisplay,black):
	global pixAr
	gameDisplay.fill(white)
	pygame.draw.line(gameDisplay, black, (0,0), (0,600),15)
        pygame.draw.line(gameDisplay, black, (0,600), (800,600),15)
        pygame.draw.line(gameDisplay, black, (800,600),(800,0),15)
        pygame.draw.line(gameDisplay, black, (800,0),(0,0),15)

	pygame.draw.line(gameDisplay, black, (90,90), (90,240),5)
	pygame.draw.line(gameDisplay, black, (90,90), (700,90),5)
	pygame.draw.line(gameDisplay, black, (700,90),(700,500),5)
       	pygame.draw.line(gameDisplay, black, (90,600),(90,540),5)
	pygame.draw.line(gameDisplay, black, (90,540),(270,540),5)
	pygame.draw.line(gameDisplay, black, (90,240), (220,240),5)
        pygame.draw.line(gameDisplay, black, (90,335), (120,335),5)
        pygame.draw.line(gameDisplay, black, (90,335),(90,440),5)
        pygame.draw.line(gameDisplay, black, (90,440),(275,440),5)
        pygame.draw.line(gameDisplay, black, (220,240),(220,340),5)
	pygame.draw.line(gameDisplay, black, (120,335),(120,440),5)
	pygame.draw.line(gameDisplay, black, (90,190),(280,190),5)
	pygame.draw.line(gameDisplay, black, (280,190),(280,340),5)
	pygame.draw.line(gameDisplay, black, (280,340),(220,340),5)
	pygame.draw.line(gameDisplay, black, (270,540),(270,600),5)
	pygame.draw.line(gameDisplay, black, (700,500),(560,500),5)
	pygame.draw.line(gameDisplay, black, (560,500),(560,400),5)
	pygame.draw.line(gameDisplay, black, (560,400),(640,400),5)
	pygame.draw.line(gameDisplay, black, (640,400),(640,190),5)
	pygame.draw.line(gameDisplay, black, (640,190),(540,190),5)
	pygame.draw.line(gameDisplay, black, (540,190),(540,290),5)
	pygame.draw.line(gameDisplay, black, (540,290),(540,290),5)
	pygame.draw.line(gameDisplay, black, (370,600),(370,440),5)
	pygame.draw.line(gameDisplay, black, (370,440),(470,440),5)
	pygame.draw.line(gameDisplay, black, (470,440),(470,600),5)
	pygame.draw.line(gameDisplay, black, (370,340),(370,190),5)
	pygame.draw.line(gameDisplay, black, (455,340),(455,190),5)	
	pygame.draw.line(gameDisplay, black, (370,340),(455,340),5)
#	pygame.draw.line(gameDisplay, black, (90,540),(160,540),5)
	pygame.display.update()

	print	gameDisplay.get_at((0,0 ))
#	pixAr = pygame.PixelArray(gameDisplay)
#	for x in  range(0,800):
#		for y in range(0,600):
#			if pixAr[x][y] == black:
#				print x,y
#				c=c+1
#	print c
#	pygame.display.update()
#

def msg_disp(text):
	largeText = pygame.font.Font('freesansbold.ttf',40)
	TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((400),(300))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def hbd():
	pygame.mixer.music.load('crash.wav')
   	pygame.mixer.music.play(-1)
	gameDisplay.fill(white)
        msg_disp('game over')
	
	time.sleep(3)
	#pygame.draw.line(gameDisplay, blue, (100,200), (300,450),10)
	#pygame.display.update()
	while True:
        	for event in pygame.event.get():
            		if event.type == pygame.QUIT:
                		pygame.quit()
               			quit()
                
        

        	button("Play Again",150,450,100,50,green,green,action)
      		button("Quit",550,450,100,50,black,black,quitgame)
		pygame.display.update()
	        clock.tick(15) 

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action(x,y)         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()


def game_intro(x,y):

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("car game", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,green,action)
        button("Quit",550,450,100,50,black,black,quitgame)

        pygame.display.update()
        clock.tick(15)
        

def action(x,y):
	x_change =0
	y_change = 0
	gameExit = True
	while gameExit:
		borders(gameDisplay,black)
	#	x1=x
	#	y1=y
                #if pixAr[x][y] == black:
                #        gameExit = False

		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				pygame.mixer.music.load('jazz.wav')
    				pygame.mixer.music.play(-1)
				if event.key == pygame.K_LEFT:
					x_change = -2
				if event.key == pygame.K_RIGHT:
					x_change = 2
				if event.key == pygame.K_UP:
					y_change = -2
				if event.key == pygame.K_DOWN:
					y_change = 2
			if event.type == pygame.KEYUP:
                		if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					pygame.mixer.music.load('silence.wav')
   					pygame.mixer.music.play(-1)
                    			x_change = 0
					y_change = 0
		x += x_change
		y += y_change
		gameDisplay.fill(white)
#		pygame.draw.line(gameDisplay, blue, (100,200), (300,450),10)
#		pygame.display.update()
	       	borders(gameDisplay,black)
		if x_change == 0 and y_change!=0:
			car4(x,y)
			
		if y_change ==0 and x_change!=0:
			car5(x,y)
			
		if x_change == 0 and y_change ==0 :
			car4(x,y)
		if x > display_width - car_width or x < 0:
			hbd()
            		gameExit = False
		if y > display_height - car_width or y < 0:
                        hbd()
			gameExit = False
	#	x1=[90 ,90 ,700,90 ,90 ,90 ,90 ,90 ,90 ,220,120,90 ,280,280,270,700,560,560]
	#	x2=[90 ,700,700,90 ,270,270,120,90 ,275,220,120,280,220,280,270,560,560,640]
	#	y1=[90 ,90 ,90 ,600,540,240,335,335,440,240,335,190,340,190,540,500,500,400]
	#	y2=[240,90 ,500,540,540,540,335,440,440,340,440,190,340,340,600,500,400,400]
		#if x>=85 and x<=90:
	#		if y>=85 and y<=245:
	#			gameExit = False
		if (gameDisplay.get_at((x,y)) == (255,0,0,255)):
					hbd()
					gameExit = False
					break
		pygame.display.update()
       		clock.tick(60)

def car4(x,y):
                gameDisplay.blit(carImg, (x,y))
#		hbd()

def car5(x,y):
                gameDisplay.blit(carImg1, (x,y))
#		hbd()

def car(x,y):
     while(y<=600 and y>=0):
                y=y-3
         #       print y
                gameDisplay.fill(white)
                gameDisplay.blit(carImg, (x,y))
                #time.sleep(0.1)
                pygame.display.update()
                clock.tick(60)
		if(y==0):
			car1(x,y)

def car1(x,y):
	while(x<=800 and x>=0):
		y=0
		x=x+3
	#	print x
		gameDisplay.fill(white)
		gameDisplay.blit(carImg1, (x,y))
		#time.sleep(0.1)
		pygame.display.update()
		clock.tick(60)
		if(x==732):
			y=0
			car2(x,y)

def car2(x,y):
     while(y<=600 and  y>=0):
		x=730
                y=y+3
         #       print y
                gameDisplay.fill(white)
                gameDisplay.blit(carImg, (x,y))
                #time.sleep(0.1)
                pygame.display.update()
                clock.tick(60)
                if(y==540):
			x=732
			car3(x,y)

def car3(x,y):
        while(x<=800 and x>=0):
                y=531
		x=x-3
                print x
                gameDisplay.fill(white)
                gameDisplay.blit(carImg1, (x,y))
                #time.sleep(0.1)
                pygame.display.update()
                clock.tick(60)
                if(x==0):
                        car(x,y)


x = 10
y = 520

#car(x,y)

game_intro(x,y)

#borders(gameDisplay,black)	
pygame.quit()
quit()
