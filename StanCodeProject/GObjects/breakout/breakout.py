"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    vx = graphics.get_dx()
    vy = graphics.get_dy()
    ball_x1 = graphics.ball.x
    ball_y1 = graphics.ball.y
    live = NUM_LIVES
    brick_num = 0

    # Add the animation loop here!
    while True:
        # ball move
        if graphics.can_ball_move:
            graphics.ball.move(vx, vy)
        # if ball is moving
        ball_x2 = graphics.ball.x
        ball_y2 = graphics.ball.y
        if ball_x2 == ball_x1 and ball_y2 == ball_y1:
            graphics.can_click = True
        else:
            # ball is moving
            ball_x1 = ball_x2
            ball_y1 = ball_y2

        # edge
        if graphics.ball.y <= 0 or \
                graphics.ball.y+graphics.ball.height >= graphics.window.height:
            vy = -vy
        if graphics.ball.x <= 0 or \
                graphics.ball.x+graphics.ball.width >= graphics.window.width:
            vx = -vx

        # remove brick
        lx = graphics.ball.x
        rx = graphics.ball.x + graphics.ball.width
        ty = graphics.ball.y
        by = graphics.ball.y + graphics.ball.height
        maybe_ball_tl = graphics.window.get_object_at(lx, ty)
        maybe_ball_tr = graphics.window.get_object_at(rx, ty)
        maybe_ball_bl = graphics.window.get_object_at(lx, by)
        maybe_ball_br = graphics.window.get_object_at(rx, by)
        if maybe_ball_tl is not None:
            vy = -vy
            if maybe_ball_tl is not graphics.paddle:
                graphics.window.remove(maybe_ball_tl)
                brick_num += 1
        elif maybe_ball_tr is not None:
            vy = -vy
            if maybe_ball_tr is not graphics.paddle:
                graphics.window.remove(maybe_ball_tr)
                brick_num += 1
        elif maybe_ball_bl is not None:
            vy = -vy
            if maybe_ball_bl is not graphics.paddle:
                graphics.window.remove(maybe_ball_bl)
                brick_num += 1
        elif maybe_ball_br is not None:
            vy = -vy
            if maybe_ball_br is not graphics.paddle:
                graphics.window.remove(maybe_ball_br)
                brick_num += 1

        # if ball out reset ball
        if graphics.ball.y+graphics.ball.height >= graphics.window.height:
            graphics.ball_reset()
            live -= 1

        # break point
        if live < 1 or brick_num >= graphics.get_brick_col()*graphics.get_brick_row():
            break

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
