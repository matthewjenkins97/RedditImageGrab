#!/usr/bin/env python
import os
import sys
import time
import shutil
import subprocess


def get_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))


def picture_grabber(destination_path, subreddit, sleep_time=1740):
    # checks to see whether a file called iteration exists, and then reads from
    # it if it does. if it does not, it is created and instantiated with the
    # number 1.
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
        # checks if num == 0, if it does, it purges the folder
        if num == 0:
            shutil.rmtree(destination_path)
        # runs redditdl.py through subprocess
        if sys.platform == "darwin" or sys.platform == "linux" or \
        sys.platform == "linux2" or sys.platform == "cygwin":
            subprocess.Popen(["python", get_path() + "/redditdl.py", subreddit,
                             destination_path, "--sort-type", "topday", "--num",
                             "1", "--skipAlbums"])
        else:
            subprocess.Popen(["python", get_path() + "\\redditdl.py", subreddit,
                             destination_path, "--sort-type", "topday", "--num",
                             "1", "--skipAlbums"])            
        # sleeps for 29 minutes
        # TODO: allow user to specify sleep time
        time.sleep(sleep_time)
        # increments num by 1 and takes the remainder of it, then writes that
        # number to iteration
        num += 1
        num %= 48
        myfile = open('iteration', 'r+')
        myfile.write(str(num))


def main():
    """runs when the user executes the program"""
    # checks to make sure the argument list is exactly 3
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
