import cocos
from cocos.menu import *
from cocos.director import director
import pyglet.app
import cocos.actions as ac

class MainMenu(cocos.menu.Menu):
    def __init__(self):
        super(MainMenu, self).__init__('Tower Defense')

        self.font_title['font_name'] = 'Oswald'
        self.font_item['font_name'] = 'Oswald'
        self.font_item_selected['font_name'] = 'Oswald'

        self.menu_anchor_y = 'center'
        self.menu_anchor_x = 'center'

        item = list()
        item.append(MenuItem('New Game', self.on_new_game))
        item.append(ToggleMenuItem('Show FPS: ', self.show_fps,
                director.show_FPS))
        items.append(MenuItem('Quit', pyglet.app.exit))
        self.create_menu(item, ac.ScaleTo(1.25, duration=0.25),
                ac.ScaleTo(1.0, duration=0.25))
