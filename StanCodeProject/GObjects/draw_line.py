"""
File: 
Name:吳禹
-------------------------
TODO:
make a gate to switch oval an line, when click
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

is_oval = True  # switch gate
window = GWindow()
SIZE = 20  # oval size
get_x = 0  # oval.x, start with 0
get_y = 0  # oval.y, start with 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(make_oval_line)


def make_oval_line(mouse):
    global get_x, get_y, is_oval
    do_oval = GOval(SIZE, SIZE)
    if is_oval:
        window.add(do_oval, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        get_x = mouse.x  # record  x0
        get_y = mouse.y  # record  y0
        is_oval = False  # gate close
    else:
        # delete oval first
        maybe_oval = window.get_object_at(get_x, get_y)
        if maybe_oval is not None:
            window.remove(maybe_oval)

        do_line = GLine(x0=get_x, y0=get_y, x1=mouse.x, y1=mouse.y)
        window.add(do_line)
        is_oval = True  # gate open


if __name__ == "__main__":
    main()
