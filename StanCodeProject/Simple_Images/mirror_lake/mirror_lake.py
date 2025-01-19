"""
File: mirror_lake.py
Name:吳禹
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: jpg filepath
    :return: SimpleImage jpg, a mirrored jpg
    """
    img = SimpleImage(filename)
    mirror_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            m_pixel = mirror_img.get_pixel(x, y)
            m_pixel.red = pixel.red
            m_pixel.green = pixel.green
            m_pixel.blue = pixel.blue

            m_pixel2 = mirror_img.get_pixel(x, mirror_img.height - 1 - y)
            m_pixel2.red = pixel.red
            m_pixel2.green = pixel.green
            m_pixel2.blue = pixel.blue
    return mirror_img


def main():
    """
    make a function, that do mirror the lake
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
