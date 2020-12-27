#!/usr/bin/python3

import os
import subprocess
import sys

# accept a file path
# if converted version exists and is newer than file, return converted version.
# otherwise, convert and return it.
# return is error code and either string or file
# 0: OK
# 4: requested file not created 

def gen(source, target):

    # determine behavior:
    if not os.path.exists(target) or (os.path.getmtime(target) < os.path.getmtime(source)):
        # cached file doesn't exist yet
        # or
        # cached exists but is out of date
        subprocess.run('pandoc --wrap=preserve -s -o {} {}'.format(target, source).split())
    else:
        # cached exists and is up to date
        pass

    # final sanity check
    if os.path.exists(target):
        return (0, target)
    else:
        return (4, 'file not created for unknown reason')

if __name__ == '__main__':
    source = sys.argv[1]
    target = sys.argv[1] + '.html'
    gen(source, target)
