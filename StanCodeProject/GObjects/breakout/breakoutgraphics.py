"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 2.5 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.y = self.window.height-self.paddle.height-1-paddle_offset
        self.paddle.x = (self.window.width-self.paddle.width)/2
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.x = (self.window.width-self.ball.width)/2
        self.ball.y = (self.window.height-self.ball.height)/2
        self.ball.filled = True
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.ball_velocity()

        # Initialize our mouse listeners
        # onmouseclicked()
        self.can_ball_move = False
        self.can_click = True
        onmouseclicked(self.ball_move_switch)
        # onmousemoved()
        onmousemoved(self.paddle_move)

        # Draw bricks
        brick_x = 0
        brick_y = brick_offset
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.x = brick_x
                self.brick.y = brick_y
                if j < 2:
                    self.brick.fill_color = "red"
                elif 2 <= j < 4:
                    self.brick.fill_color = "green"
                elif 4 <= j < 6:
                    self.brick.fill_color = "yellow"
                elif 6 <= j < 8:
                    self.brick.fill_color = "brown"
                else:
                    self.brick.fill_color = "blue"
                self.window.add(self.brick)
                brick_y += self.brick.height+brick_spacing
            brick_x += self.brick.width+brick_spacing
            brick_y = brick_offset

        # get_object
        self.get_brick = False
        self.is_object_get = False
        self.is_brick_removed = False
        self.ball_2r = self.ball.width
        self.maybe_brick1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.maybe_brick2 = self.window.get_object_at(self.ball.x+self.ball_2r, self.ball.y)
        self.maybe_brick3 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball_2r)
        self.maybe_brick4 = self.window.get_object_at(self.ball.x+self.ball_2r, self.ball.y+self.ball_2r)

        # create score GLabel
        self.score = 0
        self.score_label = GLabel(f'Score: {self.score}', y=self.window.height)
        self.score_label.font = '-20'
        self.window.add(self.score_label)

        # create life label
        self.life_label = GLabel(f'Life: ')
        self.life_label.font = '-20'
        self.life_label.x = self.window.width-self.life_label.width*1.5
        self.life_label.y = self.window.height
        self.window.add(self.life_label)

    def paddle_move(self, mouse):
        if mouse.x-self.paddle.width/2 >= 0 and mouse.x < self.window.width-self.paddle.width/2:
            self.paddle.x = mouse.x-self.paddle.width/2

    def ball_move_switch(self, mouse):
        if self.can_click:
            self.can_ball_move = True
            self.can_click = False

    def ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = self.__dx * -1

    def get_dx(self):
        self.ball_velocity()
        return self.__dx

    def get_dy(self):
        return self.__dy

    def ball_reset(self):
        self.can_ball_move = False
        self.can_click = True
        self.ball.x = (self.window.width - self.ball.width) / 2
        self.ball.y = (self.window.height - self.ball.height) / 2

    def remove_brick(self):
        if self.maybe_brick1 is not None and self.maybe_brick1 is not self.paddle \
                and self.maybe_brick1 is not self.score_label\
                and self.maybe_brick1 is not self.life_label:
            self.get_brick = True
            self.window.remove(self.maybe_brick1)
        elif self.maybe_brick2 is not None and self.maybe_brick2 is not self.paddle\
                and self.maybe_brick2 is not self.score_label\
                and self.maybe_brick2 is not self.life_label:
            self.get_brick = True
            self.window.remove(self.maybe_brick2)
        elif self.maybe_brick3 is not None and self.maybe_brick3 is not self.paddle\
                and self.maybe_brick3 is not self.score_label\
                and self.maybe_brick3 is not self.life_label:
            self.get_brick = True
            self.window.remove(self.maybe_brick3)
        elif self.maybe_brick4 is not None and self.maybe_brick4 is not self.paddle\
                and self.maybe_brick4 is not self.score_label\
                and self.maybe_brick4 is not self.life_label:
            self.get_brick = True
            self.window.remove(self.maybe_brick4)
        else:
            self.get_brick = False

        # if break brick score +1
        if self.get_brick:
            self.score += 1
            self.score_label.text = f'Score: {self.score}'

    def get_object(self, ball_x, ball_y):
        self.maybe_brick1 = self.window.get_object_at(ball_x, ball_y)
        self.maybe_brick2 = self.window.get_object_at(ball_x+self.ball_2r, ball_y)
        self.maybe_brick3 = self.window.get_object_at(ball_x, ball_y+self.ball_2r)
        self.maybe_brick4 = self.window.get_object_at(ball_x+self.ball_2r, ball_y+self.ball_2r)
        if self.maybe_brick1 is not None:
            self.is_object_get = True
            # return self.maybe_brick1
        elif self.maybe_brick2 is not None:
            self.is_object_get = True
            # return self.maybe_brick2
        elif self.maybe_brick3 is not None:
            self.is_object_get = True
            # return self.maybe_brick3
        elif self.maybe_brick4 is not None:
            self.is_object_get = True
            # return self.maybe_brick4
        else:
            self.is_object_get = False

    def add_life_label(self):
        self.window.add(self.life_label)

    @staticmethod
    def get_brick_row():
        return BRICK_ROWS

    @staticmethod
    def get_brick_col():
        return BRICK_COLS
