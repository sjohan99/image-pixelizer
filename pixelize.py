def make_matrix(width, height, pixel_size):
    width -= width % pixel_size
    height -= height % pixel_size
    rows = width // pixel_size
    cols = height // pixel_size
    return rows, cols


def average_color(rgba_values: list):
    avg = {'red': 0, 'green': 0, 'blue': 0, 'count': 0}
    for RGBA in rgba_values:
        if RGBA[3]:
            avg['red'] += RGBA[0]
            avg['green'] += RGBA[1]
            avg['blue'] += RGBA[2]
            avg['count'] += 1

    def avg_of(color):
        return round(avg[color] / avg['count'])

    return avg_of('red'), avg_of('green'), avg_of('blue'), 255


