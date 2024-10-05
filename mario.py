import neat
import pygame
import os
import copy

WIN_WIDTH=800
WIN_HEIGHT=800

RUN_CONSTANT=8
JUMP_BOOST=4

FRAME_RATE=20

local_dir=os.path.dirname(__file__)
images_dir=os.path.join(local_dir,"images")

COMMON_FACTOR=3
SMALL_MARIO_FACTOR=COMMON_FACTOR
BIG_MARIO_FACTOR=COMMON_FACTOR
PLATFORM_FACTOR=COMMON_FACTOR
KOOPA_FACTOR=COMMON_FACTOR
BG_FACTOR=COMMON_FACTOR
COIN_FACTOR=COMMON_FACTOR
MUSHROOM_FACTOR=COMMON_FACTOR
GOOMBA_FACTOR=COMMON_FACTOR
PIPE_FACTOR=COMMON_FACTOR
BLOCK_FACTOR=COMMON_FACTOR
CASTLE_FACTOR=COMMON_FACTOR
FLAG_FACTOR=COMMON_FACTOR

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

class Small_mario:
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
        self.orientation=1 #0 for left, 1 for right
        self.tick_co_ordinates=[(self.x,self.y)]
    def run_forward(self,flag): # flag is true if player is in left of screen else in right
        self.img_count+=1
        if flag:
            self.x+=RUN_CONSTANT
        else:
            #all other objects move to the left with -0.5
            pass
        if self.img_count<self.ANIMATION_TIME:
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
        self.orientation = 1
    def run_backward(self,flag):
        self.img_count += 1
        if flag:
            self.x -= RUN_CONSTANT
        if self.img_count < self.ANIMATION_TIME:
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
        self.orientation = 0
    def move(self,flag2): # flag2 gets off when we land on platform or land
        if flag2:
            self.tick_count += 1
            d = (-16.5) * self.tick_count + 2 * (self.tick_count) ** 2
            self.y += d
            if self.orientation==1:
                self.img=self.IMGS[1]
            else:
                self.img=pygame.transform.flip(self.IMGS[1],True,False)
            self.tick_co_ordinates.append((self.x,self.y))
        if not flag2:
            self.tick_count=0
            self.tick_co_ordinates=[(self.x,self.y)]
    def fall(self):
        self.tick_count += 1
        d = 14 * (self.tick_count) ** 2
        self.y += d
        if self.orientation == 1:
            self.img = self.IMGS[0]
        else:
            self.img = pygame.transform.flip(self.IMGS[0], True, False)
        self.tick_co_ordinates.append((self.x, self.y))
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
            self.x-=RUN_CONSTANT
    def move_reverse(self,flag):
        if not flag:
            self.x+=RUN_CONSTANT
    def draw(self,window):
        for i in range(len(self.blocks)):
            window.blit(self.IMGS[self.blocks[i]],(self.x+i*self.BLOCK_WIDTH,self.y))
    def collide(self,obj,flag2,flag_freefall):
        obj_mask=obj.get_mask()
        platform_masks=[]
        for i in range(len(self.blocks)):
            platform_masks.append(pygame.mask.from_surface(self.IMGS[self.blocks[i]]))
        max_x=self.x+self.BLOCK_WIDTH*len(self.blocks)
        # check for collision
        for i in range(len(platform_masks)):
            offset=(round(self.x+i*self.BLOCK_WIDTH-obj.x),round(self.y-obj.y))
            collision_point=obj_mask.overlap(platform_masks[i],offset)
            if collision_point:
                if len(obj.tick_co_ordinates)>=2:
                    if obj.tick_co_ordinates[0][1]+obj.HEIGHT<=self.y:
                        if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                            obj.x-=1
                            #no change in flag2
                        elif obj.x+obj.WIDTH>self.x and obj.x<max_x:
                            obj.y=self.y-obj.HEIGHT-1
                            flag2=False
                            flag_freefall=False
                            obj.tick_count = 0
                            obj.tick_co_ordinates = [(self.x, self.y)]
                            return flag2,flag_freefall
                        elif obj.x>=max_x:
                            obj.x+=1
                    elif obj.tick_co_ordinates[0][1]+obj.HEIGHT>self.y:
                        if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                            obj.x-=1
                            #no change in flag2
                        elif obj.x+obj.WIDTH>self.x and obj.x<max_x and obj.tick_co_ordinates[-2][1]+obj.HEIGHT>self.y:
                            obj.y=self.y+self.BLOCK_HEIGHT+1
                            # flag3=False
                            # print("========================")
                            # print(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                            # print(obj.x, obj.y, obj.WIDTH, obj.HEIGHT)
                            # print(max_x)
                            # print("========================")
                        elif obj.x+obj.WIDTH>self.x and obj.x<max_x and obj.tick_co_ordinates[-2][1]+obj.HEIGHT<=self.y:
                            obj.y=self.y-obj.HEIGHT-1
                            flag2=False
                            flag_freefall=False
                            obj.tick_count = 0
                            obj.tick_co_ordinates = [(obj.x, obj.y)]
                            return flag2,flag_freefall
                            # print("hi!!!!!!!!!!")
                            # print("========================")
                            # print(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                            # print(obj.x, obj.y, obj.WIDTH, obj.HEIGHT)
                            # print(max_x)
                            # print("========================")
                        elif obj.x>=max_x:
                            obj.x+=1
                else:
                    if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                        obj.x-=1
                        #no change in flag2
                    elif obj.x+obj.WIDTH>self.x and obj.x<max_x and self.y+self.BLOCK_HEIGHT<=obj.y: #object is below platform
                        obj.y-=1
                    elif obj.x + obj.WIDTH > self.x and obj.x < max_x and self.y >= obj.y+obj.HEIGHT: #object is above platform
                        obj.y = self.y-obj.HEIGHT-1
                        flag2=False
                        flag_freefall=False
                        obj.tick_count = 0
                        obj.tick_co_ordinates = [(obj.x, obj.y)]
                        return flag2,flag_freefall
                    elif obj.x>=max_x: #object is right to the platform
                        obj.x+=1
        return flag2,flag_freefall
    def fall_from_block(self,obj,flag_freefall):
        if obj.y<=self.y-obj.HEIGHT+2 and obj.y>=self.y-obj.HEIGHT-2:
            if obj.x<=self.x-obj.WIDTH and obj.x>=self.x-obj.WIDTH-RUN_CONSTANT-1:
                flag_freefall=True
            elif obj.x>=self.x+len(self.blocks)*self.BLOCK_WIDTH and obj.x<=self.x+len(self.blocks)*self.BLOCK_WIDTH+RUN_CONSTANT+1:
                flag_freefall=True
        return flag_freefall

class Pipe:
    IMGS=PIPE_IMGS
    BLOCK_WIDTH=PIPE_IMGS[0].get_width()
    BLOCK_HEIGHT=PIPE_IMGS[0].get_height()

    def __init__(self,x,y,blocks):
        self.x=x
        self.y=y
        self.blocks=blocks #list of numbers: i represents PLATFORM_BLOCK_IMGS
    def move(self,flag):
        if not flag:
            self.x-=RUN_CONSTANT
    def move_reverse(self,flag):
        if not flag:
            self.x+=RUN_CONSTANT
    def draw(self,window):
        for i in range(len(self.blocks)):
            window.blit(self.IMGS[self.blocks[i]],(self.x,self.y-(i+1)*self.BLOCK_HEIGHT))
    def collide(self,obj,flag2,flag_freefall):
        obj_mask=obj.get_mask()
        platform_masks=[]
        for i in range(len(self.blocks)):
            platform_masks.append(pygame.mask.from_surface(self.IMGS[self.blocks[i]]))
        max_y=self.y-self.BLOCK_HEIGHT*len(self.blocks)
        # check for collision
        for i in range(len(platform_masks)):
            offset=(round(self.x-obj.x),round(self.y-(i+1)*self.BLOCK_HEIGHT-obj.y))
            collision_point=obj_mask.overlap(platform_masks[i],offset)
            if collision_point:
                # print("wow")
                if len(obj.tick_co_ordinates)>=2:
                    if obj.tick_co_ordinates[0][1]+obj.HEIGHT<=max_y:
                        if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                            obj.x=self.x-obj.WIDTH-1
                            #no change in flag2
                        elif obj.x+obj.WIDTH>self.x and obj.x<self.x+self.BLOCK_WIDTH:
                            obj.y=max_y-obj.HEIGHT-1
                            flag2=False
                            flag_freefall=False
                            obj.tick_count = 0
                            obj.tick_co_ordinates = [(obj.x, obj.y)]
                            return flag2,flag_freefall
                        elif obj.x>=self.x+self.BLOCK_WIDTH:
                            obj.x=self.x+self.BLOCK_WIDTH+1
                    elif obj.tick_co_ordinates[0][1]+obj.HEIGHT>max_y:
                        if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                            obj.x=self.x-obj.WIDTH-1
                            #no change in flag2

                        elif obj.x + obj.WIDTH > self.x and obj.x < self.x + self.BLOCK_WIDTH // 2 and max_y < obj.y + obj.HEIGHT and obj.tick_co_ordinates[-2][1]+obj.HEIGHT>max_y:
                            obj.x=self.x-obj.WIDTH-1
                        elif obj.x + obj.WIDTH > self.x and obj.x > self.x + self.BLOCK_WIDTH // 2 and obj.x < self.x + self.BLOCK_WIDTH and max_y < obj.y + obj.HEIGHT and obj.tick_co_ordinates[-2][1]+obj.HEIGHT>max_y:
                            obj.x=self.x+self.BLOCK_WIDTH+1
                        elif obj.x+obj.WIDTH>self.x and obj.x<self.x+self.BLOCK_WIDTH and obj.tick_co_ordinates[-2][1]+obj.HEIGHT<=max_y:
                            obj.y=max_y-obj.HEIGHT-1
                            flag2=False
                            flag_freefall=False
                            obj.tick_count = 0
                            obj.tick_co_ordinates = [(obj.x, obj.y)]
                            return flag2,flag_freefall
                            # print("hi!!!!!!!!!!")
                            # print("========================")
                            # print(self.x, self.y, self.BLOCK_WIDTH, self.BLOCK_HEIGHT)
                            # print(obj.x, obj.y, obj.WIDTH, obj.HEIGHT)
                            # print(max_x)
                            # print("========================")
                        elif obj.x>=self.x+self.BLOCK_WIDTH:
                            obj.x=self.x+self.BLOCK_WIDTH+1
                else:
                    # print("wow")
                    if self.x>=obj.x+obj.WIDTH: #object is left to the platform
                        obj.x=self.x-obj.WIDTH-1
                        #no change in flag2
                    # elif obj.x+obj.WIDTH>self.x and obj.x<self.x+self.BLOCK_WIDTH and max_y<=obj.y+obj.HEIGHT: #object is below platform
                    #     obj.y-=1
                    elif obj.x + obj.WIDTH > self.x and obj.x < self.x+self.BLOCK_WIDTH and max_y >= obj.y+obj.HEIGHT: #object is above platform
                        obj.y = max_y - obj.HEIGHT - 1
                        flag2=False
                        flag_freefall=False
                        obj.tick_count = 0
                        obj.tick_co_ordinates = [(self.x, self.y)]
                        return flag2,flag_freefall
                    elif obj.x + obj.WIDTH > self.x and obj.x < self.x+self.BLOCK_WIDTH//2 and max_y < obj.y+obj.HEIGHT:
                        obj.x=self.x-obj.WIDTH-1
                        # obj.y = max_y - obj.HEIGHT - 1
                        # flag2=False
                        # flag_freefall=False
                        # obj.tick_count = 0
                        # obj.tick_co_ordinates = [(self.x, self.y)]
                        # return flag2,flag_freefall
                    elif obj.x + obj.WIDTH > self.x and obj.x > self.x + self.BLOCK_WIDTH // 2 and obj.x < self.x + self.BLOCK_WIDTH and max_y < obj.y + obj.HEIGHT:
                        obj.x=self.x+self.BLOCK_WIDTH+1
                    elif obj.x>=self.x+self.BLOCK_WIDTH: #object is right to the platform
                        obj.x=self.x+self.BLOCK_WIDTH+1
        return flag2,flag_freefall
    def fall_from_block(self,obj,flag_freefall):
        max_y = self.y - self.BLOCK_HEIGHT * len(self.blocks)
        if obj.y<=max_y-obj.HEIGHT+2 and obj.y>=max_y-obj.HEIGHT-2:
            if obj.x<=self.x-obj.WIDTH and obj.x>=self.x-obj.WIDTH-RUN_CONSTANT-1:
                flag_freefall=True
            elif obj.x>=self.x+self.BLOCK_WIDTH and obj.x<=self.x+self.BLOCK_WIDTH+RUN_CONSTANT+1:
                flag_freefall=True
        return flag_freefall

class Base:
    IMGS=GROUND_BLOCK_IMGS
    WIDTH=GROUND_BLOCK_IMGS[0].get_width()
    HEIGHT=GROUND_BLOCK_IMGS[0].get_height()

    def __init__(self,x,y,total_width):
        self.x=x
        self.y=y
        self.total_width=total_width
    def draw(self,window):
        num_blocks=int(self.total_width/self.WIDTH)+1
        num_vertical_blocks=int((window.get_height()-self.y)/self.HEIGHT)+1
        for i in range(num_blocks):
            for j in range(num_vertical_blocks):
                window.blit(self.IMGS[0],(self.x+i*self.WIDTH,self.y+j*self.HEIGHT))
                # pygame.draw.rect(window, (0, 255, 0),
                #                  (self.x+i*self.WIDTH, self.y+j*self.HEIGHT, self.WIDTH+(i+1)*self.WIDTH, self.HEIGHT+(j+1)*self.HEIGHT),
                #                  2)  # Green for base
    def collide(self,obj,flag2,flag_freefall):
        max_x=self.x+(int(self.total_width/self.WIDTH)+1)*self.WIDTH
        for i in range(int(self.total_width / self.WIDTH) + 1):
            if obj.x+obj.WIDTH>self.x and obj.x<max_x and obj.y+obj.HEIGHT>self.y+1:
                obj.y=self.y-obj.HEIGHT-1
                flag2=False
                flag_freefall=False
                obj.tick_count = 0
                obj.tick_co_ordinates = [(self.x, self.y)]
                return flag2,flag_freefall
        # print("bye")
        return flag2,flag_freefall
        # obj_mask = obj.get_mask()
        # base_mask=pygame.mask.from_surface(self.IMGS[0])
        # for i in range(int(self.total_width/self.WIDTH)+1):
        #     offset=(round(self.x+i*self.WIDTH-obj.x),round(self.y-obj.y))
        #     collision_point = obj_mask.overlap(base_mask, offset)
        #     if flag2:
        #         print(offset)
        #     if collision_point:
        #         flag2=False
        #         print("hi")
        #         if obj.y+obj.HEIGHT>=self.y:
        #             obj.y=self.y-obj.HEIGHT-1
        #         return flag2
        # return flag2
    def move(self,flag):
        if not flag:
            self.x-=RUN_CONSTANT
    def move_reverse(self,flag):
        if not flag:
            self.x+=RUN_CONSTANT

STANDARD_BASE=Base(0,600,WIN_WIDTH)
STANDARD_PLATFORM=Platform(350,500,[0,0,0,1,0])
STANDARD_PLATFORM2=Platform(650,400,[0,0,0,1,0,1])
STANDARD_PIPE=Pipe(200,600,[0,0,1])
def draw_window(window,small_marios,platforms,bases,pipes):
    window.fill((0,0,0))
    for small_mario in small_marios:
        small_mario.draw(window)
        pygame.draw.rect(window, (255, 0, 0), (small_mario.x, small_mario.y, small_mario.WIDTH, small_mario.HEIGHT), 2)  # Red for obj
    for platform in platforms:
        platform.draw(window)
    for base in bases:
        base.draw(window)
    for pipe in pipes:
        pipe.draw(window)
    pygame.display.update()

def callibrate(obj,platforms,bases,pipes,flag):
    if not flag:
        d=int(WIN_WIDTH//2)-obj.x
        for platform in platforms:
            platform.x+=d
        for base in bases:
            base.x+=d
        for pipe in pipes:
            pipe.x+=d
        obj.x+=d

def main():
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    run = True
    s_mario=Small_mario(100,600-SMALL_MARIO_IMGS[0].get_height())
    platforms=[STANDARD_PLATFORM,STANDARD_PLATFORM2]
    bases=[STANDARD_BASE]
    pipes=[STANDARD_PIPE]
    s_marios=[s_mario]
    flag=True
    flag2=False
    flag_freefall=False
    t=0
    while run:
        t+=1
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        # flag2_earlier=copy.deepcopy(flag2)
        # flag_freefall_earlier=copy.deepcopy(flag_freefall)
        if keys[pygame.K_UP]:
            flag2=s_mario.jump()
            # if keys[pygame.K_LEFT]:
            #     s_mario.x-=JUMP_BOOST
            #     for base in bases:
            #         base.x+=JUMP_BOOST
            #     for platform in platforms:
            #         platform.x+=JUMP_BOOST
            # elif keys[pygame.K_RIGHT]:
            #     s_mario.x+=JUMP_BOOST
            #     for base in bases:
            #         base.x-=JUMP_BOOST
            #     for platform in platforms:
            #         platform.x-=JUMP_BOOST
        if keys[pygame.K_LEFT]:
            s_mario.run_backward(flag)
            for base in bases:
                base.move_reverse(flag)
            for platform in platforms:
                platform.move_reverse(flag)
            for pipe in pipes:
                pipe.move_reverse(flag)
        if s_mario.x>int(WIN_WIDTH/2):
            flag=False
        if keys[pygame.K_RIGHT]:
            # print(s_mario.img_count)
            s_mario.run_forward(flag)
            for base in bases:
                base.move(flag)
            for platform in platforms:
                platform.move(flag)
            for pipe in pipes:
                pipe.move(flag)
        s_mario.move(flag2)
        if flag_freefall:
            s_mario.fall()
        for platform in platforms:
            flag_freefall = platform.fall_from_block(s_mario, flag_freefall)
            if flag_freefall:
                break
        for pipe in pipes:
            flag_freefall = pipe.fall_from_block(s_mario, flag_freefall)
            if flag_freefall:
                break
        for platform in platforms:
            new_flag,flag_freefall1=platform.collide(s_mario, flag2,flag_freefall)
            if not new_flag:
                flag2=new_flag
                # if s_mario.orientation == 1:
                #     print("no no")
                #     s_mario.img = s_mario.IMGS[0]
                # else:
                #     s_mario.img = pygame.transform.flip(s_mario.IMGS[0], True, False)
                flag_freefall=flag_freefall1
        for base in bases:
            new_flag2, flag_freefall2 = base.collide(s_mario, flag2, flag_freefall)
            if not new_flag2:
                flag2 = new_flag2
                flag_freefall = flag_freefall2
        for pipe in pipes:
            new_flag,flag_freefall1=pipe.collide(s_mario, flag2,flag_freefall)
            if not new_flag:
                flag2=new_flag
                flag_freefall=flag_freefall1
        callibrate(s_mario, platforms, bases, pipes, flag)
        draw_window(window, s_marios, platforms, bases,pipes)


main()
