import cocos
import cocos.actions as ac

if __name__ == '__main__':
    cocos.director.director.init(caption='Actions')

    layer = cocos.layer.Layer()
    sprite = cocos.sprite.Sprite('tank.png', position=(200, 200))
    sprite.do(ac.MoveTo((250, 300), 3))
    layer.add(sprite)

    scene = cocos.scene.Scene(layer)
    cocos.director.director.run(scene)
