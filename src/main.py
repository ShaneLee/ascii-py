#!/usr/bin/env python3
import math

from argparse import ArgumentParser
from PIL import Image

DENSITY = '@#0o*. '

class AsciiImage: 
    def __init__(self, path, density):
        self.path = path
        self.density = density
        self.density_len = len(density)

    def print(self):
        im = Image.open(self.path).convert('RGB').rotate(90)
        x, y = im.size
        pixels = im.load()
        text = ''
        for i in range(x):
            for j in range(y):
                text += self.find_char(self.mean(pixels[i, j]))
            text += '\n'
        
        print(text)

    def find_char(self, mean):
        return self.density[self.find_char_index(mean)] + ' '

    def find_char_index(self, mean):
        return math.floor(self.remap(mean, 0, 255, 0, self.density_len))

    def remap(self, n, start1, stop1, start2, stop2):
        return ((n-start1)/(stop1-start1))*(stop2-start2)+start2

    def mean(self, pixel):
        r = pixel[0]
        g = pixel[1]
        b = pixel[2]
        return (r+g+b) / 3

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-f', '--file', help='The file to convert')
    parser.add_argument('-c', '--chars')
    args = parser.parse_args()

    i = AsciiImage(args.file, args.chars)
    i.print()

