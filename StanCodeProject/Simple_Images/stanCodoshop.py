"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    color_distance = ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    pixel_list = []  # store [r,g,b] and return
    pixel_count = 0
    red_pixel_sum = 0
    green_pixel_sum = 0
    blue_pixel_sum = 0
    for pixel in pixels:
        red_pixel_sum += pixel.red
        green_pixel_sum += pixel.green
        blue_pixel_sum += pixel.blue
        pixel_count += 1

    # pixel_list append
    pixel_list.append(red_pixel_sum//pixel_count)  # red = [0]
    pixel_list.append(green_pixel_sum // pixel_count)  # green = [1]
    pixel_list.append(blue_pixel_sum // pixel_count)  # blue = [2]

    return pixel_list


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance",
    which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_pixel = get_average(pixels)  # return avg[r,g,b]
    min_color_dist = 255*3
    best_pixel = any(pixels)  # 不知道要怎麼設定初始值，不太確定能這樣寫

    # find minima_dist pixel
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, avg_pixel[0], avg_pixel[1], avg_pixel[2])
        if pixel_dist < min_color_dist:
            min_color_dist = pixel_dist
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # milestone.1
    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # milestone.2
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # milestone.3
    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # milestone.4
    for x in range(width-1):
        for y in range(height-1):
            pixels = []  # 取出相同位置pixel，放進list
            for image in images:
                pixel = image.get_pixel(x, y)
                pixels.append(pixel)

            # get best pixel and replace
            best_pixel = get_best_pixel(pixels)
            result_pixel = result.get_pixel(x, y)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    # return result

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []  # 先創造filenames櫃子，存list
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))

            # test
            # print("jpg_in_dir: ", filenames)

    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []  # 創造images櫃子 存Simple Image list
    jpgs = jpgs_in_dir(dir)  # jpgs = filenames[]
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        # image.show()
        images.append(image)  # images[] 加入SimpleImage(filename), 照片形式存到 images[]
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]

    # test
    # print(f'sys.argv[0]: {sys.argv[0]}')  # sys.argv[0] = filename.py
    # print('args: ', args)  # [hoover]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])  # 丟[hoover]進去, return 照片形式images[]
    solve(images)


if __name__ == '__main__':
    main()
