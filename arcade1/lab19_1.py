import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5
DEAD_ZONE = 0.02


# Map pyglet joystick buttons between ps4 and pyglet controller


def pyglet_raw_to_ps4_button_dict() -> dict[str, str]:
    """Convert raw button names to PS4 button names.
    Returns:
        dictionary mapping Pyglet raw button names to PS4 button names

    The "0x9:" prefix is omitted.
    In order to map the raw name to the PS4 name
    take the last character of the passed string, like

    raw_button_name = ...
    py2ps4 = pyglet_raw_to_ps4_button_dict()
    ps4_button_name = py2ps4[raw_button_name[-1]]
    """
    # All raw names start with the prefix "0x9:"
    # e.g. for the the 'circle' button the name is "0x9:3"
    pyglet_to_ps4_button = dict()
    pyglet_to_ps4_button["1"] = "square"
    pyglet_to_ps4_button["2"] = "cross"
    pyglet_to_ps4_button["3"] = "circle"
    pyglet_to_ps4_button["4"] = "triangle"
    pyglet_to_ps4_button["5"] = "L1"
    pyglet_to_ps4_button["6"] = "R1"
    pyglet_to_ps4_button["7"] = "L2"
    pyglet_to_ps4_button["8"] = "R2"
    pyglet_to_ps4_button["9"] = "share"
    pyglet_to_ps4_button["a"] = "options"
    pyglet_to_ps4_button["b"] = "L3"  # left stick button
    pyglet_to_ps4_button["c"] = "R3"  # right stick
    pyglet_to_ps4_button["d"] = "PS"  # Playstation button
    pyglet_to_ps4_button["e"] = "touchpad"  # touchpad button
    return pyglet_to_ps4_button


def ps4_to_pyglet_raw_button_dict() -> dict[str, str]:
    """Map PS4 button names to Pyglet raw button names.
    Returns:
        dictionary mapping PS4 button names to Pyglet raw names (0x9:*)
    """
    ps4_to_pyglet_button = dict()
    for v, k in pyglet_raw_to_ps4_button_dict().items():
        ps4_to_pyglet_button[k] = "0x9:" + v
    return ps4_to_pyglet_button


def pyglet_to_ps4_button_dict() -> dict[int, str]:
    """Map Pyglet button ids to PS4 button names.
    Returns:
        dictionary mapping Pyglet button id (int) to PS4 button name
    """
    pyglet_to_ps4_button = dict()
    pyglet_to_ps4_button[0] = "square"
    pyglet_to_ps4_button[1] = "cross"
    pyglet_to_ps4_button[2] = "circle"
    pyglet_to_ps4_button[3] = "triangle"
    pyglet_to_ps4_button[4] = "L1"
    pyglet_to_ps4_button[5] = "R1"
    pyglet_to_ps4_button[6] = "L2"
    pyglet_to_ps4_button[7] = "R2"
    pyglet_to_ps4_button[8] = "share"
    pyglet_to_ps4_button[9] = "options"
    pyglet_to_ps4_button[10] = "L3"  # left stick button
    pyglet_to_ps4_button[11] = "R3"  # right stick
    pyglet_to_ps4_button[12] = "PS"  # Playstation button
    pyglet_to_ps4_button[13] = "touchpad"  # touchpad button
    return pyglet_to_ps4_button


def ps4_to_pyglet_button_dict() -> dict[str, int]:
    """Map PS4 button names to Pyglet integer button ids.
    Returns:
        dictionary mapping PS4 button names to Pyglet button ids.
    """
    ps4_to_pyglet_button = dict()
    for v, k in pyglet_raw_to_ps4_button_dict().items():
        ps4_to_pyglet_button[k] = "0x9:" + v
    return ps4_to_pyglet_button


pyglet_to_ps4 = pyglet_raw_to_ps4_button_dict()
ps4_buttons = pyglet_to_ps4_button_dict()


class Ball:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """Draw the balls with the instance variables we have."""
        arcade.draw_circle_filled(
            self.position_x, self.position_y, self.radius, self.color
        )

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title, capture_events=False):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # If true joystick end joyhat vents are captures by this object.
        self.capture_events = capture_events

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 0, 0, 15, arcade.color.AUBURN)

        # Get a list of all the game controllers that are plugged in
        joysticks = arcade.get_joysticks()

        # If we have a game controller plugged in, grab it and
        # make an instance variable out of it.
        if joysticks:
            self.joystick = joysticks[0]
            # Register the object that will receive all events.
            # all the on_* methods will be called after registering.
            if self.capture_evernts:
                self.joystick.push_handlers(self)
            self.joystick.open()
            print(self.joystick)
        else:
            print("There are no joysticks.")

    # noinspection PyMethodMayBeStatic
    def on_joybutton_press(self, joystick, button):
        """Handle button-down event for the joystick"""
        print(f"Button {button} down; PS4 name: {ps4_buttons[button]}")

    # noinspection PyMethodMayBeStatic
    def on_joybutton_release(self, _joystick, button):
        """Handle button-up event for the joystick"""
        print("Button {} up".format(button))

    # noinspection PyMethodMayBeStatic
    def on_joyhat_motion(self, _joystick, hat_x, hat_y):
        """Handle hat events"""
        print("Hat ({}, {})".format(hat_x, hat_y))

    def on_joyaxis_motion(self, j, ax, v):
        d = 10 * v
        if ax == "x":
            if abs(j.x + d) < DEAD_ZONE:
                self.ball.change_x = 0
            else:
                self.ball.change_x = d
        else:
            if abs(j.y - d) < DEAD_ZONE:
                self.ball.change_y = 0
            else:
                self.ball.change_x = -d
        self.ball.update()
        self.ball.change_x, self.ball.change_y = (0, 0)

    def on_draw(self):
        """Called whenever we need to draw the window."""
        arcade.start_render()
        self.ball.draw()

    def update(self, delta_time):

        if not self.capture_events:
            # Update the position according to the game controller
            if self.joystick:

                # Set a "dead zone" to prevent drive from a centered joystick
                if abs(self.joystick.x) < DEAD_ZONE:
                    self.ball.change_x = 0
                else:
                    self.ball.change_x = self.joystick.x * MOVEMENT_SPEED

                # Set a "dead zone" to prevent drive from a centered joystick
                if abs(self.joystick.y) < DEAD_ZONE:
                    self.ball.change_y = 0
                else:
                    self.ball.change_y = -self.joystick.y * MOVEMENT_SPEED

                self.ball.update()


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
