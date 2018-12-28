#Importing all packages
import arcade
import random
import os
import time
from player import Player
from wall import Wall
from coin import Coin

SPRITE_SCALING = 0.5
SPRITE_SCALING_COIN = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

NUMBER_OF_COINS = 50

MOVEMENT_SPEED = 10
print("Welcome to level 1! Collect all the coins to proceed.")

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):

        super().__init__(width, height)

        # Set up the Player
        self.player = Player(100, 120, "images\\pokisprite.png", SPRITE_SCALING, MOVEMENT_SPEED)
        self.physics_engine = None

    def setup(self):
        # -- Set up the walls
        # Create a series of horizontal walls
        Wall.generateWalls()
        # -- Randomly place coins where there are no walls
        # Create the coins
        Coin.placeCoins(NUMBER_OF_COINS)

        # check collision b/w player and wall
        self.physics_engine = arcade.PhysicsEngineSimple(self.player.getSprite(), Wall.wall_list)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        # This command has to happen before we start drawing
        arcade.start_render()
        # Draw all the sprites.
        Wall.wall_list.draw()
        Coin.coin_list.draw()
        self.player.getSprite().draw()

        output = f"Score: {self.player.getScore()}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 15)

    def on_key_press(self, key, modifiers):
        self.player.move(key)

    def on_key_release(self, key, modifiers):
        self.player.stopMove()


    def update(self, delta_time):
        """ Movement and game logic """
        self.physics_engine.update()

        # check if player collects coin
        player_coin_hit_list = arcade.check_for_collision_with_list(self.player.getSprite(), Coin.coin_list)

        for coin in player_coin_hit_list:
            coin.kill()
            self.player.setScore(self.player.getScore() + 1)

            if self.player.getScore()==50:
                print('Congratulation on collecting all the coins. Please close the window to continue.')
                os._exit(1)

        # end of where player collects coin


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
        main()
