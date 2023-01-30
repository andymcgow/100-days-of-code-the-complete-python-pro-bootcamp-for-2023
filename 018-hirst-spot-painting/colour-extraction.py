# This file takes an image and extracts a colour pallete that can be used to randomly drive the pen colour in the turtle module.

import colorgram

colours = colorgram.extract("image.jpg", 30)
rgb_colours = []

for colour in colours:
    r = colour.rgb.r
    g = colour.rgb.g
    b = colour.rgb.b
    rgb_colours.append((r, g, b))

print(rgb_colours)