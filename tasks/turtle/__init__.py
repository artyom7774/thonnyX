def color(color):
    color = list(color)

    color[0] = (color[0] + 2 * 255) // 3
    color[1] = (color[1] + 2 * 255) // 3
    color[2] = (color[2] + 2 * 255) // 3

    return color
