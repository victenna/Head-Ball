import pygame,random,time
pygame.init()
screen = pygame.display.set_mode((1200,900))
clock = pygame.time.Clock()
start = time.time()
images=[pygame.image.load('m_man0.png'),pygame.image.load('m_man1.png')]
images1=[pygame.image.load('mman0.png'),pygame.image.load('mman1.png')]
balls=pygame.image.load('ball1.png')
bg=pygame.image.load('bg.png')
class Boy():
    def __init__(self,image,x,y):
        super().__init__()
        self.image = image
        self.x=x
        self.y=y
        self.rect = self.image.get_rect(center=(self.x,self.y))
    def position(self,image):
        self.image = image
        self.rect = self.image.get_rect(center=(self.x,self.y))
    def draw(self):
        screen.blit(self.image,self.rect)
boy=Boy(images[0],415,695)
boy1=Boy(images1[0],600,695)
class Ball():
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('ball1.png')
        self.image=pygame.transform.scale(self.image,(30,30))
        self.x=x
        self.y=y
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.dy=-20
    def motion(self,q):
        self.x=self.x+q*2.5
        self.dy=self.dy+0.5
        self.y=self.y+self.dy
        self.rect = self.image.get_rect(center=(self.x,self.y))
    def draw(self):
        screen.blit(self.image,self.rect)
ball=Ball(405,605)
q=0
ttime=0.1
collision=1
while True:
    screen.blit(bg,(0,0))
    tt = (time.time())
    sec=round((tt - start),2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if sec<ttime:
        boy.position(images[0])
        boy1.position(images1[0])
    if q==0:
        if sec>=ttime:
            collision=ball.rect.colliderect(boy1.rect)
            boy.position(images[1])
            ball.motion(1)
            if collision==1:
                boy.position(images[0])
                start = time.time()-0.1
                ball.dy=-20
                q=1
    if q==1:
        if sec>=ttime:
            collision=ball.rect.colliderect(boy.rect)
            boy1.position(images1[1])
            ball.motion(-1)
            if collision==1:
                boy1.position(images1[0])
                start = time.time()-0.1
                ball.dy=-20
                q=0
    boy.draw()
    ball.draw()
    boy1.draw()
    pygame.display.update()
    clock.tick(60)

