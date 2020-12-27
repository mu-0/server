#!/usr/bin/python3

import os
import subprocess
import fnmatch

debug = False

# a source and target path are passed to gen().
# that function causes a markdown file to be generated named index.html
# and then returns a path to that file.
# 0: file generated successfully
# 1: index file not generated for some reason

patterns = [
    "__*__",
    ".*"
]

def gen(source, target):
    global debug
    
    files = []
    with os.scandir(source) as it:
        for entry in it:
            if not any(fnmatch.fnmatch(entry.name, p) for p in patterns):
                if entry.is_dir():
                    files.append("[{}/]({}/)\n\n".format(entry.name, entry.name))
                else:
                    files.append("[{}]({})\n\n".format(entry.name, entry.name))
                    
    with open(target, 'w') as fout:
        for f in files:
            fout.write(f)
    
    if os.path.exists(target):
        return (0, target)
    else:
        return (1, 'index file not generated')


if __name__ == '__main__':
    debug = True
    gen('.', 'index.html')
