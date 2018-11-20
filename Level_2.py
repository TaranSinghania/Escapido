#Importing all the required libraries
import arcade
import math
import os
import random

#File handling for reading inital text
f=open("Level_2.txt")
for i in f.readlines():
    print(i.strip())
f.close()

#difficulty choosing
difficulty=int(input('Type in the option number you wish to choose: '))
if difficulty==1:
    BULLET_SPEED = 10
    fr=60
elif difficulty==2:
    BULLET_SPEED = 15
    fr=40
else:
    BULLET_SPEED=25
    fr=25

#Defining dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#Additonal background
def draw_star(x, y):
    arcade.draw_circle_filled(x, y, 2, arcade.color.WHITE)

#Defining class
class MyGame(arcade.Window):
    """ Main application class """


    def __init__(self, width, height):
        super().__init__(width, height)

        # Optional
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        #Background
        arcade.set_background_color(arcade.color.BLACK)

        self.frame_count = 0

        self.enemy_list = None
        self.bullet_list = None
        self.player_list = None
        self.player_sprite = None
        self.score=100

    def setup(self):
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        self.score = 100
        # Add player ship
        self.player_sprite = arcade.Sprite("images\p_ship.png", 0.4)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Add tbottom-left enemy ship
        enemy = arcade.Sprite("images\e_ship.png", 0.5)
        enemy.center_x = 120
        enemy.center_y = 120
        enemy.angle = 180
        self.enemy_list.append(enemy)

        # Add bottom-right enemy ship
        enemy = arcade.Sprite("images\e_ship.png", 0.5)
        enemy.center_x = 680
        enemy.center_y = 120
        enemy.angle = 180
        self.enemy_list.append(enemy)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        for i in range(20):
            draw_star(random.randrange(800),random.randrange(600))
        self.enemy_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        self.frame_count += 1

        # Loop through each enemy that we have
        for enemy in self.enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = enemy.center_x
            start_y = enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            enemy.angle = math.degrees(angle)-90

            # Shoot every 'fr' frames change of shooting each frame
            if self.frame_count % 10 == 0:
                bullet = arcade.Sprite("bullet.jpg",0.2)
                bullet.center_x = start_x
                bullet.center_y = start_y

                # Angle the bullet sprite
                bullet.angle = math.degrees(angle)

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet.change_x = math.cos(angle) * BULLET_SPEED
                bullet.change_y = math.sin(angle) * BULLET_SPEED

                self.bullet_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.kill()

        self.bullet_list.update()

        bullet_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bullet_list)

        # Loop through each colliding sprite, and update score
        for bullet in bullet_hit_list:
            bullet.kill()
            self.score -= 1
        if self.score==0:
                print("--- %s seconds ---" % (time.time() - start_time))
                print('PS-YOU HAD NO CHANCE OF SURVIVING')
                os._exit(1)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """Called whenever the mouse moves. """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    
    import time
    start_time = time.time()
    main()
    

