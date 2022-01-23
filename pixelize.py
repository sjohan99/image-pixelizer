from PIL import Image


TEST_IMAGE_PATH = 'images/mario.png'


def get_rows_cols(width, height, pixel_size):
    width -= width % pixel_size
    height -= height % pixel_size
    rows = width // pixel_size
    cols = height // pixel_size
    return rows, cols


def average_color(rgba_values: list):
    avg = {'red': 0, 'green': 0, 'blue': 0, 'count': 0}
    has_transparency = (len(rgba_values[0]) == 4)
    for RGBA in rgba_values:
        if not has_transparency or RGBA[3]:
            avg['red'] += RGBA[0]
            avg['green'] += RGBA[1]
            avg['blue'] += RGBA[2]
            avg['count'] += 1

    if avg['count'] == 0:
        return None

    def avg_of(color):
        return round(avg[color] / avg['count'])

    return avg_of('red'), avg_of('green'), avg_of('blue'), 255


def do(pixel_size, image_path):
    with Image.open(image_path) as my_image:
        rows, cols = get_rows_cols(my_image.width, my_image.height, pixel_size=pixel_size)
        for i in range(rows):
            for j in range(cols):
                colors = []
                for pixel in loop_over_chunk(i, j, pixel_size):
                    colors.append(my_image.getpixel(pixel))
                new_color = average_color(colors)
                if new_color:
                    for pixel in loop_over_chunk(i, j, pixel_size):
                        my_image.putpixel(pixel, new_color)
            yield percent(i, rows)
        my_image = my_image.crop((0, 0, rows*pixel_size, cols*pixel_size))

        my_image.show()


def loop_over_chunk(i, j, pixel_size):
    for top in range(pixel_size):
        for left in range(pixel_size):
            yield (i * pixel_size) + top, (j * pixel_size) + left


def percent(part, whole):
    return round((part / whole) * 100, 1)


if __name__ == '__main__':
    for completion in do(5, 'images/mario.png'):
        print(f"{completion}% finished")
    # do(5, 'images/furnaceman.png')








