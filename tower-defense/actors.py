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
