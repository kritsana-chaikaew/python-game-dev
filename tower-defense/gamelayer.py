import random

from cocos.director import director
from cocos.scene.transitions import SplitColsTransition, FadeTransition
import cocos.layer
import cocos.scene
import cocos.text
import cocos.actions as ac
import cocos.collision_model as cm

import mainmenu

def game_over():
    w, h = director.get_window_size()
    layer = cocos.layer.Layer()
    text = cocos.text.Label('Game Over', position=(w/2, h/2),
            font_name='Oswald', font_size=72,
            anchor_x='center',
            anchor_y='center')
    layer.add(text)
    scene = cocos.scene.Scene(layer)
    new_scene = FadeTransition(mainmenu.new_menu())
    func = lambda: director.replace(new_scene)
    scene.do(ac.Delay(3)+ac.CallFunc(func))
    return scene

class GameLayer(cocos.layer.Layer):
    def __init__(self, hud, scenario):
        super(GameLayer, self).__init__()
        self.hud = hud
        self.scenario = scenario
        self.score = self._score = 0
        self.points = self._points = 40
        self.turrets = []

        w, h = director.get_window_size()
        cell_size = 32
