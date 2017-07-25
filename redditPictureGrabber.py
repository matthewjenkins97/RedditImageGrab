#!/usr/bin/env python
import os
import sys
import time
import shutil
import subprocess


def get_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def picture_grabber(destination_path, subreddit, sleep_time=1740):
    try:
        myfile = open('iteration', 'r+')
        num_str = myfile.read()
        num = int(num_str)
    except IOError:
        myfile = open('iteration', 'w+')
        myfile.write("1")
        num = 1
    while True:
        myfile.close()
        print("Current iteration is: " + str(num))
        # if num is 0, delete everything inside folder
        if num == 0:
            shutil.rmtree(destination_path)
        if sys.platform == "darwin" or sys.platform == "linux" or \
        sys.playform == "linux2" or sys.platform == "cygwin":
            subprocess.Popen(["python", get_path() + "/redditdl.py", subreddit,
                             destination_path, "--sort-type", "topday", "--num",
                             "1", "--skipAlbums"])
        else:
            subprocess.Popen(["python", get_path() + "\\redditdl.py", subreddit,
                             destination_path, "--sort-type", "topday", "--num",
                             "1", "--skipAlbums"])            
        time.sleep(sleep_time)
        # incrementing and modulo
        num += 1
        num %= 48
        myfile = open('iteration', 'r+')
        myfile.write(str(num))


def main():
    if len(sys.argv) != 3:
        print("USAGE: redditPictureGrabber.py destination_path subreddit")
        quit()
    else:
        # dump argv into variables
        destination_path = sys.argv[1]
        subreddit = sys.argv[2]
        # checks if destination_path exists. if it does not, it quits because
        # i'd rather not create any weird folders if the user types something
        # wrong.
        if os.path.exists(destination_path):
            picture_grabber(destination_path, subreddit)
        else:
            print("The destination you provided does not exist.")
            print("The program will now exit.")
            quit()


main()
