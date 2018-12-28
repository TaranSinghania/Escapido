import arcade

class Wall:

    wall_list = arcade.SpriteList()

    def __init__(self, x, y, image_path, SPRITE_SCALING):
        self.x = x
        self.y = y
        self.wall_sprite = arcade.Sprite(image_path, SPRITE_SCALING)
        self.wall_sprite.center_x = self.x
        self.wall_sprite.center_y = self.y

    def getSprite(self):
        return self.wall_sprite

    def generateWalls():
        for y in range(0, 800, 200):
            for x in range(100, 700, 64):
                wall = Wall(x, y, "images\\box.png", 0.5)
                Wall.wall_list.append(wall.getSprite())
