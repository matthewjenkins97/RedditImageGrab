#!/usr/bin/env python
import os
import sys
import time
import shutil
import subprocess


def get_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def win_picture_grabber(destination_path, subreddit):
    pass


def mac_picture_grabber(destination_path, subreddit):
    """the mac version of the picture downloader."""
    myfile = open('iteration', 'w+')
    myfile.write("1")
    num = 1
    while True:
        myfile.close()
        print("Current iteration is: " + str(num))
        # if num is 0, delete everything inside folder
        if num == 0:
            shutil.rmtree(destination_path)
        subprocess.Popen(["python", get_path() + "/redditdl.py", subreddit,
                         destination_path, "--sort-type", "topday", "--num",
                         "1", "--skipAlbums"])
        time.sleep(1740)
        # incrementing and modulo
        num += 1
        num %= 48
        myfile = open('iteration', 'r+')
        myfile.write(str(num))


def main():
    if len(sys.argv) != 3:
        print("USAGE: redditPictureGrabber.py destination_path subreddit")
    else:
        # dump argv into variables
        destination_path = sys.argv[1]
        subreddit = sys.argv[2]
        # checks if destination_path exists. if it does not, it quits.
        if os.path.exists(destination_path):
            # checking what OS is running and execute a function based off the
            # result
            if sys.platform == "darwin":
                mac_picture_grabber(destination_path, subreddit)
            elif sys.platform == "win32":
                win_picture_grabber(destination_path, subreddit)
            else:
                print("Currently only macOS and Windows are supported.")
                print("The program will now exit.")
                quit()
        else:
            print("The destination you provided does not exist.")
            print("The program will now exit.")
            quit()


main()
