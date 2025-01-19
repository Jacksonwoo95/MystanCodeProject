"""
File: 
Name:吳禹
-------------------------
TODO:
make a switch gate,
if gate : close,not do click function
else : vy+=GRAVITY in every while loop
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
DELAY = 10
GRAVITY = 9.8
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

can_click = True
count_click = 3  # 3 times to click
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(drop_ball)


def drop_ball(event):
    global can_click, VX, count_click
    vy = 0
    if count_click > 0:
        if can_click:
            count_click -= 1
            can_click = False
            while ball.x < window.width:
                ball.move(VX, vy)
                if ball.y+ball.height > window.height-1 and vy > 0:
                    # make sure vy > 0 (upward)
                    vy = -vy*REDUCE
                else:
                    vy += GRAVITY
                pause(DELAY)

            # if ball.x out window, add ball at start
            window.add(ball, x=START_X, y=START_Y)
            can_click = True


if __name__ == "__main__":
    main()
