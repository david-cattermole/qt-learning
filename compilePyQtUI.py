#!/bin/env python
import sys
import os
import pprint
from PyQt4.uic import compileUi


def main(in_path_dir, out_path_dir):
    in_path_dir = os.path.abspath(in_path_dir)
    out_path_dir = os.path.abspath(out_path_dir)
    in_paths = os.listdir(in_path_dir)
    for in_name in in_paths:
        in_fullpath = os.path.join(in_path_dir, in_name)
        out_name = 'ui_' + in_name.replace('.ui', '.py')
        out_fullpath = os.path.join(out_path_dir, out_name)
        print 'Compiling:', in_name, '->', out_name
        f = open(out_fullpath, 'w')
        compileUi(in_fullpath, f, False, 4, False)
        f.close()


if __name__ == '__main__':
    # Compile
    in_path_dir = './ui'
    out_path_dir = './python/qtTests'
    main(in_path_dir, out_path_dir)
    exit()