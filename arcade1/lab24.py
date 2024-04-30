"""
Sprite Bullets

Simple program to show basic sprite usage.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_bullets
"""
import math
import os
import random

import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
SPRITE_SCALING_LASER = 0.8
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites and Bullets Example"

BULLET_SPEED = 5


class Coin(arcade.Sprite):

    def __init__(self):
        """Constructor."""
        filename = ":resources:images/items/coinGold.png"
        sprite_scaling = 0.5/3  # SPRITE_SCALING_COIN
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def on_update(self, delta_time: float = 1 / 60) -> None:
        """Update the ball's position."""
        # Calculate a new x, y
        self.center_x = (
            self.circle_radius *
            math.sin(self.circle_angle) + self.circle_center_x
        )
        self.center_y = (
            self.circle_radius *
            math.cos(self.circle_angle) + self.circle_center_y
        )

        # Increase the angle in prep for the next round.
        self.circle_angle += self.circle_speed


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Variables that will hold sprite lists
        self.player_list = None
        self.coin_list = None
        self.bullet_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Load sounds. Sounds from kenney.nl
        self.gun_sound = arcade.load_sound(":resources:sounds/hurt5.wav")
        self.hit_sound = arcade.load_sound(":resources:sounds/hit5.wav")

        arcade.set_background_color = None
        self.background = None

    def position_coins(self):
        for c in self.coin_list:

            # Create the coin instance
            # Coin image from kenney.nl
            # Position the coin
            c.circle_center_x = random.randrange(SCREEN_WIDTH)
            c.circle_center_y = random.randrange(120, SCREEN_HEIGHT)

            # Random radius from 10 to 200
            c.circle_radius = random.randrange(10, SCREEN_WIDTH // 4)

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.background = arcade.load_texture("5.png")
        assert self.background
        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite(":resources:images/space_shooter/"
                                           "playerShip1_blue.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # Create the coins
        for i in range(COIN_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin()
            # Position the coin
            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(120, SCREEN_HEIGHT)

            # Random radius from 10 to 200
            coin.circle_radius = random.randrange(10, SCREEN_WIDTH // 4)

            # Random start angle from 0 to 2pi
            coin.circle_angle = random.random() * 2 * math.pi
            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        """
        Render the screen.
        """
        # This command has to happen before we start drawing
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

        # Draw all the sprites.
        self.coin_list.draw()
        self.bullet_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10,
                         20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """
        Called whenever the mouse moves.
        """
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        # Gunshot sound
        arcade.play_sound(self.gun_sound)
        # Create a bullet
        bullet = arcade.Sprite(
            ":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        bullet.angle = 90

        # Give the bullet a speed
        bullet.change_y = BULLET_SPEED

        # Position the bullet
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        # Add the bullet to the appropriate lists
        self.bullet_list.append(bullet)

    def on_key_press(self, key, modifier):
        if key == arcade.key.F:
            # User hits f. Flip between full and not full screen.
            self.set_fullscreen(not self.fullscreen)

            # Get the window coordinates. Match viewport to window coordinates
            # so there is a one-to-one mapping.
            global SCREEN_WIDTH
            global SCREEN_HEIGHT
            SCREEN_WIDTH, SCREEN_HEIGHT = self.get_size()
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)
            self.position_coins()

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on bullet sprites
        self.bullet_list.update()
        self.coin_list.on_update(delta_time)

        # Loop through each bullet
        for bullet in self.bullet_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(
                bullet, self.coin_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for coin in hit_list:
                coin.remove_from_sprite_lists()
                self.score += 1

                # Hit Sound
                arcade.play_sound(self.hit_sound)

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.coin_list)

        if len(hit_list) > 0:
            arcade.play_sound(self.hit_sound)
            print("YOU WERE HIT! GAME OVER")
            self.close()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
