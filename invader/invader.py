import cocos
import cocos.collision_model as cm
import cocos.euclid as eu
import cocos.layer

from collections import defaultdict
from pyglet.window import key
from pyglet.image import load, ImageGrid, Animation

class Actor(cocos.sprite.Sprite):
    def __init__(self, image, x, y):
        super(Actor, self).__init__(image)
        self.position = eu.Vector2(x, y)
        self.cshape = cm.AARectShape(self.position,
                self.width/2, self.height/2)

    def move(self, offset):
        self.position += offset
        self.cshape.center += offset

    def update(self, elapsed):
        pass

    def collide(self, other):
        pass

class PlayerCannon(Actor):
    KEY_PRESSED = defaultdict(int)

    def __init__(self, x, y):
        super(PlayerCannon, self).__init__('img/cannon.png', x, y)
        self.speed = eu.Vector2(200, 0)

    def update(self, elapsed):
        pressed = PlayerCannon.KEY_PRESSED
        movement = pressed[key.RIGHT] - pressed[key.LEFT]
        w = self.width / 2
        if movement != 0 and w <= self.x <= self.parent.width - w:
            self.move(self.speed * movement * elapsed)

    def collide(self, other):
        other.kill()
        self.kill()

class Alien(Actor):
    def load_animation(image):
        seq = ImageGrid(load(image), 2, 1)
        return Animation.from_image_sequence(seq, 0.5)
    TYPES = {
            '1': (load_animation('img/alien1.png'), 40),
            '2': (load_animation('img/alien2.png'), 20),
            '3': (load_animation('img/alien3.png'), 10)
    }

    def form_type(x, y, alien_type, column):
        animation, score = Alien.TYPE[alien_type]
        return Alien(animation, x, y, score, column)

    def __init__(self, img, x, y, score, column=None):
        super(Alien, self).__init__(img, x, y)
        self.score = score
        self.column = column

    def on_exit(self):
        super(Alien, self).on_exit()
        if self.column:
            self.column.remove(self)

class AlienColum(object):
    def __init__(self, x, y):
        alien_types = enumerate(['3', '3', '2', '2', '1'])
        self.aliens = [Alien.from_type(x, y+i*60, alien, self)
                for i, alien in alien_types]

    def remove(self, alien):
        self.aliens.remove(alien)

    def shoot(self):
        pass

    def should_turn(self, d):
        if len(self.aliens) == 0:
            return False
        alien = self.aliens[0]
        x = alien.x
        width = self.parent.width
        return x >= width - 50 and d == 1 \
                or x <= 50 and d == -1

class GameLayer(cocos.layer.Layer):
    is_event_handler = True

    def on_key_press(self, k, _):
        PlayerCannon.KEY_PRESSED[k] = 1

    def on_key_release(self, k, _):
        PlayerCannon.KEY_PRESSED[k] = 0

    def __init__(self):
        super(GameLayer, self).__init__()
        w, h = cocos.director.director.get_window_size()
        self.width = w
        self.height = h
        self.lives = 3
        self.score = 0
        self.create_player()
        self.create_alien_group(100, 300)
        cell = 1.25 * 50
        self.collman = cm.CollisionManagerGrid(0, w, 0, h, cell, cell)
        self.schedule(self.update)

    def create_player(self):
        self.player = PlayerCannon(self.width/2, 50)
        self.add(self.player)

    def update_score(self, score=0):
        self.score += score

    def create_alien_group(self, x, y):
        pass

    def update(self, dt):
        self.collman.clear()
        for _, node in self.children:
            self.collman.add(node)
            if not self.collman.knows(node):
                self.remove(node)
        for _, node in self.children:
            node.update(dt)

    def collide(delf, node):
        if node is not None:
            for other in self.collman.iter_colliding(node):
                node.collide(other)
                return True
        return False

if __name__ == '__main__':
    cocos.director.director.init(caption='Cocos Invaders',
            width=800, height=600)
    game_layer =GameLayer()
    main_scene = cocos.scene.Scene(game_layer)
    cocos.director.director.run(main_scene)
