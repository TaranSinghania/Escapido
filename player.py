import arcade

class Player:

    def __init__(self, x, y, image_path, SPRITE_SCALING, speed):
        self.score = 0
        self.player_sprite = arcade.Sprite(image_path, SPRITE_SCALING)
        self.speed = speed
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def getSprite(self):
        return self.player_sprite

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def move(self, key):
        if key == arcade.key.UP:
            self.player_sprite.change_y += self.speed
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y += -self.speed
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x += -self.speed
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x += self.speed

    def stopMove(self):
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
