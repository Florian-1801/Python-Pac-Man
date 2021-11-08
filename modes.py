from constants import *

class ModeController(object):
    def __init__(self, entity):
        self.timer = 0
        self.time = 0
        self.mainmode = MainMode()
        self.current = self.mainmode.mode
        self.entity = entity 

    def update(self, dt):
        self.mainmode.update(dt)
        if self.current is FREIGHT:
            self.timer += dt
            if self.timer >= self.time:
                self.time = 0
                self.entity.normalMode()
                self.current = self.mainmode.mode
        elif self.current in [SCATTER, CHASE]:
            self.current = self.mainmode.mode

        if self.current is SPAWN:
            if self.entity.node == self.entity.spawnNode:
                self.entity.normalMode()
                self.current = self.mainmode.mode

    def setSpawnMode(self):
        if self.current is FREIGHT:
           self.current = SPAWN

    def setFreightMode(self):
        if self.current in [SCATTER, CHASE]:
            self.timer = 0
            self.time = 7
            self.current = FREIGHT
            #print('Freight')
        elif self.current is FREIGHT:
            self.timer = 0 

class MainMode(object):
    def __init__(self):
        self.timer = 0
        self.scatter()

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.time:
            if self.mode is SCATTER:
                self.chase()
            elif self.mode is CHASE:
                self.scatter() 

    def scatter(self):
        self.mode = SCATTER
        self.time = 7
        self.timer = 0
        #print('Scatter')

    def chase(self):
        self.mode = CHASE
        self.time = 20
        self.timer = 0
        #print('Chase')
 
 