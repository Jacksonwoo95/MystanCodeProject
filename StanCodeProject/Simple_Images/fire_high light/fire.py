"""
File: fire.py
Name:吳禹
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def main():
    """
    do pixel.red = 255 when big fire
    else do grayscale
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


def highlight_fires(filename):
    """
    :param filename: png filepath
    :return: png, highlight the big fire pixel
    """
    highlight_img = SimpleImage(filename)
    for x in range(highlight_img.width):
        for y in range(highlight_img.height):
            pixel = highlight_img.get_pixel(x, y)
            avg = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > avg * HURDLE_FACTOR:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = avg
                pixel.green = avg
                pixel.blue = avg
    return highlight_img


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
