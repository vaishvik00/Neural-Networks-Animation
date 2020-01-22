import pygame import time
from math import pi pygame.init()
# size variable is using for set screen size size = [1400,900]
screen = pygame.display.set_mode(size) pygame.display.set_caption("Example program to draw geometry") # done variable is using as flag
done = False

clock = pygame.time.Clock() white = (255, 255, 255)
green = (0, 255, 0)

blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 18)


# create a text suface object,

# on which text is drawn on it.

i1 = font.render('i1(0.5)', True, blue) i2 = font.render('i2 (0.10)', True, blue) h1 = font.render('h1', True, blue)
h2 = font.render('h2', True,blue)

o1 = font.render('o1 (.01)', True,blue) o2 = font.render('o2 (0.99)', True,blue) b1 = font.render('b1 (0.35)', True,blue)
b2 = font.render('b2 (0.60)', True,blue) w1 = font.render('w1 (0.15)', True,blue) w2 = font.render('w2 (0.20)', True,blue) w3 = font.render('w3 (0.25)', True,blue) w4 = font.render('w4 (0.30)', True,blue) w5 = font.render('w5 (0.40)', True,blue) w6 = font.render('w6 (0.45)', True,blue) w7 = font.render('w7 (0.50)', True,blue) w8 = font.render('w8 (0.55)', True,blue)


h1c = font.render(' net h1 = w1*i1 + w2*i2 + b1*1' , True,blue)

h1c1 = font.render(' net h1 = 0.15 * 0.05 + 0.2 * 0.1 + 0.35 * 1' , True,blue) h1n = font.render('net h1 = 0.3775', True,blue)
h1o = font.render('out h1 = 1/(1 + e ^ (- net h1))',True,blue) h1o1 = font.render('out h1 = 1/(1 + e ^ (- 0.3775))',True,blue) h1op = font.render('out h1 = 0.593269992',True,blue)


h2c = font.render(' net h2 = w3*i1 + w4*i2 + b1*1' , True,blue)

h2c2 = font.render(' net h2 = 0.25 * 0.05 + 0.30 * 0.10 + 0.35 * 1' , True,blue) h2n = font.render('net h2 = 0.3925', True,blue)
h2o = font.render('out h2 = 1/(1 + e ^ (- net h2))',True,blue) h2o2 = font.render('out h2 = 1/(1 + e ^ (- 0.3925))',True,blue) h2op = font.render('out h2 = 0.596884378',True,blue)


h1u = font.render('h1 (0.593) ', True,blue) h2u = font.render('h2 (0.596) ', True,blue)


o1c = font.render(' net o1 = w5*h1 + w6*h2 + b2*1' , True,blue)
o1c1 = font.render(' net o1 = 0.4 * 0.593 + 0.45 * 0.596 + 0.6 * 1' , True,blue) o1n = font.render('net o1 = 1.105905967', True,blue)
o1o = font.render('out o1 = 1/(1 + e ^ (- net o1))',True,blue) o1o1 = font.render('out o1 = 1/(1 + e ^ (- 1.105905))',True,blue) o1op = font.render('out o1 = 0.75136507' , True,blue)


o2c = font.render(' net o2 = w7*h1 + w8*h2 + b2*1' , True,blue)

o2c2 = font.render(' net o2 = 0.50 * 0.593 + 0.55 * 0.596 + 0.60 * 1' , True,blue) o2n = font.render('net o2 = 1.2243', True,blue)
o2o = font.render('out o2 = 1/(1 + e ^ (- net h2))',True,blue) o2o2 = font.render('out o2 = 1/(1 + e ^ (- 1.2243))',True,blue) o2op = font.render('out o2 = 0.772928465',True,blue)


er = font.render('E total = 1/2 (target o1 - out o1)^2 + 1/2 (target o2 - out o2)^2',True,blue) er1 = font.render('E total = 1/2 (0.01 - 0.75136)^2 + 1/2 (0.99 - 0.77292)^2' , True,blue) er2 = font.render('E total = 0.298371109',True,blue)


w51 = font.render('d(E total/w5) = d(E total/out o1) * d(out o1/net o1) * d(net o1/w5)',True,blue) w52 = font.render('E total = 1/2 (target 01 - out 01)^2 + 1/2 (target 02 - out 02)^2',True,blue) w53 = font.render(' d(E total/out o1) = -(target o1 - out o1) = ',True,blue)
w54 = font.render('d(E total/out o1) = -(0.01 - 0.71367507)', True,blue) w55 = font.render('d(E total/out o1) = 0.74136507',True,blue)
w56 = font.render('out o1 = 1/(1 + e ^ (- net o1)',True,blue)

w57 = font.render('d(out o1/net o1) = out o1(1 - out o1)',True,blue)

w58 = font.render('d(out o1/net o1) = 0.75136507(1-0.75316507)',True,blue) w59 = font.render('d(out o1/net o1) = 0.186815602',True,blue)


w510 = font.render(' net o1 = w5*h1 + w6*h2 + b2*1' , True,blue)
w511 = font.render('d(net o1/w5) = 1 * h1 ',True,blue)

w512 = font.render('d(net o1/w5) = 0.593269992',True,blue)

w513 = font.render('d(E total/w5) = d(E total/out o1) * d(out o1/net o1) * d(net o1/w5)',True,blue) w514 = font.render('d(E total/w5) = 0.74136507 + 0.186815602 + 0.593269992',True,blue)
w515 = font.render('d(E total/w5) = 0.082167041',True,blue)

w516 = font.render(' w5 new = w5 - (learning rate * d(E total/w5))',True ,blue) w517 = font.render(' w5 new = 0.4 - (0.05 * 0.082167041)',True,blue)
w518 = font.render(' w5 new = 0.35891648' , True,blue) w5new = font.render('w5 (0.40) -> 0.358', True,blue)


# create a rectangular object for the # text surface object
ip1 = i1.get_rect() ip2 = i2.get_rect() op1 = o1.get_rect() op2 = o2.get_rect() hp1 = h1.get_rect() hp2 = h2.get_rect() wp1 = w1.get_rect() wp2 = w2.get_rect() wp3 = w3.get_rect() wp4 = w4.get_rect() wp5 = w5.get_rect() wp6 = w6.get_rect() wp7 = w7.get_rect() wp8 = w8.get_rect() bp1 = b1.get_rect() bp2 = b2.get_rect() h1ct = h1c.get_rect()
h1c1t = h1c1.get_rect() h1nt = h1n.get_rect() h1ot = h1o.get_rect() h1o1t = h1o1.get_rect() h1opt = h1op.get_rect() h2ct = h2c.get_rect() h2c2t = h2c2.get_rect() h2nt = h2n.get_rect() h2ot = h2o.get_rect() h2o2t = h2o2.get_rect() h2opt = h2op.get_rect() ert = er.get_rect()
er1t = er1.get_rect() er2t = er2.get_rect() w51t = w51.get_rect() w52t = w52.get_rect() w53t = w53.get_rect() w54t = w54.get_rect() w55t = w55.get_rect() w56t = w56.get_rect() w57t = w57.get_rect() w58t = w58.get_rect() w59t = w59.get_rect()
w510t = w510.get_rect() w512t = w511.get_rect() w513t = w512.get_rect() w514t = w513.get_rect() w511t = w514.get_rect() w515t = w515.get_rect()
w516t = w516.get_rect() w517t = w517.get_rect() w518t = w518.get_rect() w5newt = w5new.get_rect()



h1ut = h1u.get_rect() h2ut = h2u.get_rect()





# set the center of the rectangular object. ip1.center = (100,200)
ip2.center = (100,400)

op1.center = (700,200)

op2.center = (700,400)

hp1.center = (400,200)

hp2.center = (400,400)

wp1.center = (250,200)

wp2.center = (250,270)

wp3.center = (250,350)

wp4.center = (250,400)

wp5.center = (550,200)

wp6.center = (550,270)

wp7.center = (550,350)

wp8.center = (550,400)

bp1.center = (550,600)

bp2.center = (250,600)
h1ct.center = (1000,100)

h1c1t.center = (1000,150)

h1nt.center = (1000,200)

h1ot.center = (1000,250)

h1o1t.center = (1000,300)

h1opt.center = (1000,350)




h2ct.center = (1000,400)

h2c2t.center = (1000,450)

h2nt.center = (1000,500)

h2ot.center = (1000,550)

h2o2t.center = (1000,600)

h2opt.center = (1000,650)


h1ut.center = (400,200)

h2ut.center = (400,400)

ert.center = (1000,50)

er1t.center = (1000,100)

er2t.center = (1000,150)

w51t.center = (1000,200)

w52t.center = (1000,250)

w53t.center = (1000,300)

w54t.center = (1000,350)

w55t.center = (1000,400)

w56t.center = (1000,450)

w57t.center = (1000,500)

w58t.center = (1000,550)

w59t.center = (1000,600)
w510t.center = (1000,650)

w511t.center = (1000,700)

w512t.center = (1000,750)

w513t.center = (1000,100)

w514t.center = (1000,200)

w515t.center = (1000,300)

w516t.center = (1000,350)

w517t.center = (1000,400)

w518t.center = (1000,450)

w5newt.center = (550,150)


screen.fill(white)


# copying the text surface object # to the display surface object
# at the center coordinate. #screen.blit(text, textRect)


#time.sleep(2) #screen.blit(text1, text1Rect) while not done:
# clock.tick() limits the while loop to a max of 10 times per second. clock.tick(10)


for event in pygame.event.get(): # User did something

if event.type == pygame.QUIT: # If user clicked on close symbol

done = True # done variable that we are complete, so we exit this loop #input layer circle
pygame.draw.circle(screen, (0, 0, 255), [100, 200], 40, 1)

pygame.draw.circle(screen, (0, 0, 255), [100, 400], 40, 1) time.sleep(2)
pygame.display.flip() #bias and output layer
pygame.draw.circle(screen, (0, 255, 0), [250, 600], 40, 1)


pygame.draw.circle(screen, (0, 0, 255), [400, 200], 40, 1)

pygame.draw.circle(screen, (0, 0, 255), [400, 400], 40, 1) #bias 2 and output layer
time.sleep(2) pygame.display.flip()
pygame.draw.circle(screen, (0, 255,0), [550, 600], 40, 1)


pygame.draw.circle(screen, (0, 0, 255), [700, 200], 40, 1)

pygame.draw.circle(screen, (0, 0, 255), [700, 400], 40, 1) #lines from input to hidden
time.sleep(2) pygame.display.flip()
pygame.draw.line(screen, (0, 255, 0), [140, 200], [360, 200], 3)

pygame.draw.line(screen, (0, 255, 0), [140, 200], [360, 400], 3) time.sleep(2)
pygame.display.flip()

pygame.draw.line(screen, (0, 255, 0), [140, 400], [360, 200], 3)

pygame.draw.line(screen, (0, 255, 0), [140, 400], [360, 400], 3) #lines from hidden to output
time.sleep(2) pygame.display.flip()
pygame.draw.line(screen, (0, 255, 0), [440, 200], [660, 200], 3)
pygame.draw.line(screen, (0, 255, 0), [440, 400], [660, 200], 3) time.sleep(2)
pygame.display.flip()

pygame.draw.line(screen, (0, 255, 0), [440, 200], [660, 400], 3)

pygame.draw.line(screen, (0, 255, 0), [440, 400], [660, 400], 3) #lines from bias b1 and b2
time.sleep(1) pygame.display.flip()
pygame.draw.line(screen, (0, 255, 0), [250, 560], [360, 200], 3)

pygame.draw.line(screen, (0, 255, 0), [250, 560], [360, 400], 3)

pygame.draw.line(screen, (0, 255, 0), [550, 560], [660, 200], 3)


pygame.draw.line(screen, (0, 255, 0), [550, 560], [660, 400], 3)








time.sleep(2) pygame.display.flip() screen.blit(i1, ip1) pygame.display.flip() time.sleep(2) screen.blit(i2,ip2) screen.blit(h1,hp1) screen.blit(h2,hp2) screen.blit(o1,op1) screen.blit(o2,op2) screen.blit(w1,wp1)
screen.blit(w2,wp2) screen.blit(w3,wp3) screen.blit(w4,wp4) screen.blit(w5,wp5) screen.blit(w6,wp6) screen.blit(w7,wp7) screen.blit(w8,wp8) screen.blit(b1,bp1) screen.blit(b2,bp2) pygame.display.flip() time.sleep(1) screen.blit(h1c,h1ct) pygame.display.flip() time.sleep(1) screen.blit(h1c1,h1c1t) screen.blit(h1n,h1nt) screen.blit(h1o,h1ot) screen.blit(h1o1,h1o1t) screen.blit(h1op,h1opt)


pygame.display.flip() time.sleep(1) screen.blit(h2c,h2ct) pygame.display.flip() time.sleep(1) screen.blit(h2c2,h2c2t) screen.blit(h2n,h2nt) screen.blit(h2o,h2ot) screen.blit(h2o2,h2o2t)
screen.blit(h2op,h2opt)








pygame.display.flip() time.sleep(1) screen.blit(h1u,hp1) pygame.display.flip() time.sleep(1) screen.blit(h2u,hp2)


screen.fill((255, 255, 255),(800,50,1200,800))

screen.blit(er,ert) pygame.display.flip() time.sleep(1) screen.blit(er1,er1t) pygame.display.flip() time.sleep(1) screen.blit(er2,er2t) pygame.display.flip() time.sleep(1) screen.blit(w51,w51t) pygame.display.flip() time.sleep(1) screen.blit(w52,w52t) pygame.display.flip() time.sleep(1)
screen.blit(w53,w53t) pygame.display.flip() time.sleep(1) screen.blit(w54,w54t) pygame.display.flip() time.sleep(1) screen.blit(w55,w55t) pygame.display.flip() time.sleep(1) screen.blit(w56,w56t) pygame.display.flip() time.sleep(1) screen.blit(w57,w57t) pygame.display.flip() time.sleep(1) screen.blit(w58,w58t) pygame.display.flip() time.sleep(1) screen.blit(w59,w59t) pygame.display.flip() time.sleep(1) screen.blit(w510,w510t) pygame.display.flip() time.sleep(1) screen.blit(w511,w511t) pygame.display.flip() time.sleep(1) screen.blit(w512,w512t)
screen.fill((255, 255, 255),(741,20,1200,800))


pygame.display.flip() time.sleep(1) screen.blit(w513,w513t) screen.blit(w514,w514t) screen.blit(w515,w515t) screen.blit(w516,w516t) screen.blit(w517,w517t) screen.blit(w518,w518t)


pygame.display.flip() time.sleep(1)


screen.blit(w5new,w5newt)
