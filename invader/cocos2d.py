import cocos

from collections import defaultdict
from pyglet.window import key

class MainLayer(cocos.layer.Layer):
    is_event_handler = True
    def __init__(self):
        super(MainLayer, self).__init__()
        self.player = cocos.sprite.Sprite('ball.png')
        self.player.color = (0, 0, 255)
        self.player.position = (320, 240)
        self.add(self.player)

        self.speed = 100.0
        self.pressed = defaultdict(int)
        self.schedule(self.update)

    def on_key_press(self, k, m):
        self.pressed[k] = 1

    def on_key_release(self, k, m):
        self.pressed[k] = 0

    def update(self, dt):
        x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
        y = self.pressed[key.UP] - self.pressed[key.DOWN]
        if x != 0 or y != 0:
            pos = self.player.position
            new_x = pos[0] + (self.speed * x * dt)
            new_y = pos[1] + (self.speed * y * dt)
            self.player.position = (new_x, new_y)

if __name__ == '__main__':
    cocos.director.director.init(caption='Hello, Cocos')
    layer = MainLayer()
    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
