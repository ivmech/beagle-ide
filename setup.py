#!/usr/bin/python

import os
import sys
import shutil

def usage():
    print """
Beagleboard IDE
Usage: ./setup.py [ install | clean | cleanall ]
"""
    sys.exit(0)

def install_needs():
    os.system("sudo apt-get install $(cat Dependencies.txt)")
    os.system("sudo pip install -r Requirements.txt")

def manage_syncdb():
    os.chdir("beagle")
    os.system("./manage.py syncdb")

def clean():
    ans = raw_input("Are you sure want to clean?[y/N]:")
    if ans == "y":
        os.system("pyclean ./")
        return True
    else:
        return False

def cleanall():
    if clean():
        try:
            shutil.rmtree("files")
        except:
            pass

def install():
    #install_needs()
    manage_syncdb()

if __name__ == "__main__":
    PATH = os.path.dirname(os.path.realpath(__file__))
    os.chdir(PATH)
    if len(sys.argv) > 1:
        opt = sys.argv[1]
        if opt == "install":
            install()
        elif opt == "clean":
            clean()
        elif opt == "cleanall":
            cleanall()
        else:
            usage()
    else:
        usage()
