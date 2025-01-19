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
    graphics.life_label.text = f'Life: {live}'

    # Add the animation loop here!
    while True:
        # ball move
        if graphics.can_ball_move:
            graphics.ball.move(vx, vy)

        # edge
        if graphics.ball.y <= 0 or \
                graphics.ball.y+graphics.ball.height >= graphics.window.height:
            vy = -vy
        if graphics.ball.x <= 0 or \
                graphics.ball.x+graphics.ball.width >= graphics.window.width:
            vx = -vx

        # if ball out reset ball
        if graphics.ball.y+graphics.ball.height >= graphics.window.height:
            graphics.ball_reset()
            live -= 1
            graphics.life_label.text = f'Life: {live}'

        # remove brick
        graphics.get_object(graphics.ball.x, graphics.ball.y)
        if graphics.is_object_get:
            if graphics.ball.y+graphics.ball.height >= graphics.paddle.y+graphics.paddle.height/2:
                vx = -vx
            else:
                vy = -vy
            graphics.remove_brick()

        # if ball is moving
        ball_x2 = graphics.ball.x
        ball_y2 = graphics.ball.y
        if ball_x2 == ball_x1 and ball_y2 == ball_y1:
            graphics.can_click = True
        else:
            # ball is moving
            ball_x1 = ball_x2
            ball_y1 = ball_y2

        # break point
        if live < 1 or \
                graphics.score >= graphics.get_brick_row()*graphics.get_brick_col():
            break

        # pause
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
