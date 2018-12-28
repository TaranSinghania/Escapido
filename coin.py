import arcade
import random
from wall import Wall

class Coin:

    coin_list = arcade.SpriteList()

    def __init__(self, x, y, image_path, SPRITE_SCALING):
        self.x = x
        self.y = y
        self.coin_sprite = arcade.Sprite(image_path, SPRITE_SCALING)
        self.coin_sprite.center_x = self.x
        self.coin_sprite.center_y = self.y

    def getSprite(self):
        return self.coin_sprite


    def placeCoins(NUMBER_OF_COINS):
        for i in range(NUMBER_OF_COINS):

            coin = Coin(0, 0, "images\\coin.png", 1)

            # Boolean variable if we successfully placed the coin
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.getSprite().center_x = random.randrange(800)
                coin.getSprite().center_y = random.randrange(600)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin.getSprite(), Wall.wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin.getSprite(), Coin.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            Coin.coin_list.append(coin.getSprite())
