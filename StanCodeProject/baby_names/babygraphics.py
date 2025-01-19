"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt',
    'data/full/baby-2020.txt'
]
CANVAS_WIDTH = 1080
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010, 2020]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # 計算間隔
    x_gap = (width-GRAPH_MARGIN_SIZE*2)//len(YEARS)

    # 設定x座標
    x_coordinate = GRAPH_MARGIN_SIZE+x_gap*year_index

    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # create top and bottom horizontal line
    # x0,yo,x1,y1
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # create vertical line and add year
    # x0, y0, x1, y1
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        # vertical line
        canvas.create_line(x, GRAPH_MARGIN_SIZE, x, CANVAS_HEIGHT)
        # add year
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=str(YEARS[i]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_index = 0
    for name in lookup_names:
        # init x0, y0 for create line
        x0 = 0
        y0 = 0

        for i in range(len(YEARS)):
            x = get_x_coordinate(CANVAS_WIDTH, i)

            # 先取rank，再加入y軸
            if name in name_data and str(YEARS[i]) in name_data[name]:
                rank = name_data[name][str(YEARS[i])]
            else:
                rank = None

            # 計算 y 座標
            if rank is None:  # rank不在排名內(1000以上），將y放在最下面
                y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                rank_inf = f"{name} *"
            else:  # 有排名
                y = GRAPH_MARGIN_SIZE + (int(rank) / 1000) * (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)
                rank_inf = f"{name} {rank}"

            # create rank text
            canvas.create_text(x + TEXT_DX, y, text=rank_inf, anchor=tkinter.SW, fill=COLORS[color_index])

            # create line
            # x0, y0, x1, y1
            if i == 0:
                x0 = x
                y0 = y
            if i > 0:
                canvas.create_line(x0, y0, x, y, width=LINE_WIDTH, fill=COLORS[color_index])
                # update x0, y0
                x0 = x
                y0 = y

        # color index
        color_index = (color_index + 1) % len(COLORS)

        # main() code is provided, feel free to read through it but DO NOT MODIFY


def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
