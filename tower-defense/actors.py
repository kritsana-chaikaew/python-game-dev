import cocos.sprite
import cocos.euclid as eu
import cocos.collision_model as cm

class Actor(cocos.sprite.Sprite):
    def __init__(self, img, x, y):
        super(Actor, self).__init__(img, position=(x, y))
        self._cshape = cm.CicleShape(sefl.position, self.width/2)

    @property
    def cshape(self):
        self._cshape.center = eu.Vector2(self.x, self.y)
        return self._cshape

class Turret(Actor):
    def __init__(self, x, y):
        super(Turret, self).__init__('turret.png', x, y)
        self.add(cocos.sprite.Sprite('rang.png', opacity=50, scale=5))
        self.cshape.r = 125.0
        self.target = None
        self.period = 2.0
        self.reload = 0.0
        self.schedule(self._shoot)
