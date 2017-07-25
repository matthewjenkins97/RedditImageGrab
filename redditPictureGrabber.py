#!/usr/bin/env python
import os
import shutil
import time


def main():
    myfile = open('iteration', 'r+')
    numStr = myfile.read()
    num = int(numStr)
    while True:
        myfile.close()
        print("Current iteration is: " + str(num))
        # if num is 0, delete everything inside folder
        if num == 0:
            shutil.rmtree("/Users/z0diakos/Pictures/Wallpapers/")

        os.system('python ~/Developer/Miscellaneous\ Repositories/RedditImageGrab/redditdl.py --sort-type topday --num 1 --update --sfw --skipAlbums EarthPorn /Users/z0diakos/Pictures/Wallpapers/')
        time.sleep(1740)

        # incrementing and modulo
        num = num + 1
        num = num % 48
        myfile = open('iteration', 'r+')
        myfile.write(str(num))


main()
