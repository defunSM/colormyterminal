#!/usr/bin/env python
import sys, os, math


green = "\033[1;32;40m"
red = "\033[1;31;40m"
yellow = "\033[1;33;40m"
purple = "\033[1;35;40m"
cyan = "\033[1;36;40m"
white = "\033[1;37;40m"

c = [green, red, yellow, purple, cyan, white]

def display_colors():

    for i in range(len(c)):
        print(c[i], "Color -", i)

def ctext(style, textcolor, bgcolor):

    return "\033[" + str(style) + ";" + str(textcolor) + ";" + str(bgcolor) + "m"

def main():
    pass

if __name__=="__main__":
    main()
