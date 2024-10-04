import neat
import pygame
import os
import copy

WIN_WIDTH=500
WIN_HEIGHT=800

FRAME_RATE=30

local_dir=os.path.dirname(__file__)
images_dir=os.path.join(local_dir,"images")

SMALL_MARIO_FACTOR=1
BIG_MARIO_FACTOR=1
PLATFORM_FACTOR=1
KOOPA_FACTOR=1
BG_FACTOR=1
COIN_FACTOR=1
MUSHROOM_FACTOR=1
GOOMBA_FACTOR=1
PIPE_FACTOR=1
BLOCK_FACTOR=1
CASTLE_FACTOR=1
FLAG_FACTOR=1

SMALL_MARIO_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Idle.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Jump.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Run1.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Run2.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Run3.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Small_Slide.png")),SMALL_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir, "Mario_Small_Death.png")),SMALL_MARIO_FACTOR)
                  ]
BIG_MARIO_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Idle.png")),BIG_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Jump.png")),BIG_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Run1.png")),BIG_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Run2.png")),BIG_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Run3.png")),BIG_MARIO_FACTOR),
                  pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Mario_Big_Slide.png")),BIG_MARIO_FACTOR)
                  ]
KOOPA_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Koopa_Shell.png")),KOOPA_FACTOR),
            pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Koopa_Walk1.png")),KOOPA_FACTOR),
            pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Koopa_Walk2.png")),KOOPA_FACTOR)]
BG_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Bush1.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Bush2.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Bush3.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Cloud1.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Cloud2.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Cloud3.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Hill1.png")),BG_FACTOR),
         pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Hill2.png")),BG_FACTOR)]
COIN_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Coin.png")),COIN_FACTOR)]
MUSHROOM_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"MagicMushroom.png")),MUSHROOM_FACTOR),
               pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"1upMushroom.png")),MUSHROOM_FACTOR),
               pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Starman.png")),MUSHROOM_FACTOR)]
GOOMBA_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Goomba_Walk1.png")),GOOMBA_FACTOR),
             pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Goomba_Walk2.png")),GOOMBA_FACTOR),
             pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Goomba_Flat.png")),GOOMBA_FACTOR)
             ]
PIPE_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"PipeBottom.png")),PIPE_FACTOR),
           pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"PipeTop.png")),PIPE_FACTOR),
           pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"PipeConnection.png")),PIPE_FACTOR)]
GROUND_BLOCK_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"GroundBlock.png")),BLOCK_FACTOR)]
PLATFORM_BLOCK_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Brick.png")),BLOCK_FACTOR),
                     pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir, "MysteryBlock.png")),BLOCK_FACTOR),
                     pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir, "EmptyBlock.png")),BLOCK_FACTOR)]
# MYSTERY_BLOCK_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"MysteryBlock.png")),BLOCK_FACTOR),
#                     pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"EmptyBlock.png")),BLOCK_FACTOR)]
HARD_BLOCK_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"HardBlock.png")),BLOCK_FACTOR)]
CASTLE_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Castle.png")),CASTLE_FACTOR)]
FLAG_IMGS=[pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"Flag.png")),FLAG_FACTOR),
           pygame.transform.scale_by(pygame.image.load(os.path.join(images_dir,"FlagPole.png")),FLAG_FACTOR)]

class small_mario:
    IMGS=SMALL_MARIO_IMGS
    WIDTH=SMALL_MARIO_IMGS[0].get_width()
    HEIGHT=SMALL_MARIO_IMGS[0].get_height()
    ANIMATION_TIME=5

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.tick_count=0
        self.img_count=0
        self.img=self.IMGS[0]
        self.velocity_y=0
        self.height=self.y
    def run_forward(self,flag): # flag is true if player is in left of screen else in right
        self.img_count+=1
        if flag:
            self.x+=1
        else:
            #all other objects move to the left with -0.5
            pass
        if self.tick_count<self.ANIMATION_TIME:
            self.img=self.IMGS[2]
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = self.IMGS[3]
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = self.IMGS[4]
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = self.IMGS[3]
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = self.IMGS[2]
            self.img_count = 0
    def run_backward(self,flag):
        self.img_count += 1
        if flag:
            self.x -= 1
        else:
            # all other objects move to the left with -0.5
            pass
        if self.tick_count < self.ANIMATION_TIME:
            self.img = pygame.transform.flip(self.IMGS[2],True,False)
        elif self.img_count < self.ANIMATION_TIME * 2:
            self.img = pygame.transform.flip(self.IMGS[3],True,False)
        elif self.img_count < self.ANIMATION_TIME * 3:
            self.img = pygame.transform.flip(self.IMGS[4],True,False)
        elif self.img_count < self.ANIMATION_TIME * 4:
            self.img = pygame.transform.flip(self.IMGS[3],True,False)
        elif self.img_count == self.ANIMATION_TIME * 4 + 1:
            self.img = pygame.transform.flip(self.IMGS[2],True,False)
            self.img_count = 0
    def move(self,flag2): # flag2 gets off when we land on platform or land
        if flag2:
            self.tick_count += 1
            d = (-16.5) * self.tick_count + 1.5 * (self.tick_count) ** 2
            self.y += d
            self.img=self.IMGS[1]
        if not flag2:
            self.tick_count=0
    def jump(self):
        flag2=True
        return flag2
    def draw(self,window):
        window.blit(self.img,(self.x,self.y))
    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class Platform:
    IMGS=PLATFORM_BLOCK_IMGS
    BLOCK_WIDTH=PLATFORM_BLOCK_IMGS[0].get_width()
    BLOCK_HEIGHT=PLATFORM_BLOCK_IMGS[0].get_height()

    def __init__(self,x,y,blocks):
        self.x=x
        self.y=y
        self.blocks=blocks #list of numbers: i represents PLATFORM_BLOCK_IMGS
    def move(self,flag):
        if not flag:
            self.x-=1
    def draw(self,window):
        for i in range(len(self.blocks)):
            window.blit(self.IMGS[self.blocks[i]],(self.x+i*self.BLOCK_WIDTH,self.y))
    def collide(self,obj,flag2):
        obj_mask=obj.get_mask()
        platform_masks=[]
        for i in range(1,len(self.blocks)):
            platform_masks.append(pygame.mask.from_surface(self.IMGS[self.blocks[i]]))
        max_x=self.x+self.BLOCK_WIDTH*len(self.blocks)
        # check for collision
        for i in range(len(platform_masks)):
            offset=(round(self.x-obj.x),round(self.y-obj.y))
            collision_point=obj_mask.overlap(platform_masks[i],offset)
            if collision_point:
                if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                    self.x-=1
                    #no change in flag2
                elif obj.x+obj.WIDTH>self.x and obj.x<max_x and self.y+self.BLOCK_HEIGHT<=obj.y: #object is below platform
                    self.y-=1
                elif obj.x + obj.WIDTH > self.x and obj.x < max_x and self.y >= obj.y+obj.HEIGHT: #object is above platform
                    flag2=False
                elif obj.x>=max_x: #object is right to the platform
                    self.x+=1
        return flag2

class Base:
    IMGS=GROUND_BLOCK_IMGS
    WIDTH=GROUND_BLOCK_IMGS[0].get_width()
    HEIGHT=GROUND_BLOCK_IMGS[0].get_height()

    def __init__(self,x,y,total_width):
        self.x=x
        self.y=y
        self.total_width=total_width
    def draw(self,window):
        num_blocks=self.total_width/self.WIDTH+1
        num_vertical_blocks=(window.get_height()-self.y)/self.HEIGHT+1
        for i in range(num_blocks):
            for j in range(num_vertical_blocks):
                window.blit(self.IMGS[0],(self.x+i*self.WIDTH,self.y+j*self.HEIGHT))
    def collide(self,obj,flag2):
        obj_mask = obj.get_mask()
def draw_window(window,s_mario):
    s_mario.draw(window)
    pygame.display.update()
def main():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    s_mario=small_mario(200,200)
    while run:
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_window(window,s_mario)
main()
