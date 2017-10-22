"""
Compiles *.ui files in the 'ui' directory, and saves them into 'python/qtLearn'.

Usage (PyQt4):
$ cd <project root>
$ python compileUI.py

Usage (PySide - Maya):
$ cd <project root>
$ mayapy compileUI.py

"""
import sys
import os
try:
    from pysideuic import compileUi
except ImportError:
    from PyQt4.uic import compileUi


def compile_file(in_path, out_path):
    if not os.path.isfile(in_path):
        print 'Warning: Skipping', in_path
        return
    in_dir, in_name = os.path.split(in_path)
    out_dir, out_name = os.path.split(out_path)

    print 'Compiling:', in_name, '->', out_name
    try:
        f = open(out_path, 'w')
        compileUi(in_path, f, False, 4, False)
        f.close()
    except Exception, e:
        print 'Warning: File did not compile, %r' % in_path
        # print e
        raise
    return


def compile_directory(in_path_dir, out_path_dir):
    in_path_dir = os.path.abspath(in_path_dir)
    out_path_dir = os.path.abspath(out_path_dir)
    in_paths = sorted(os.listdir(in_path_dir))
    for in_name in in_paths:
        in_fullpath = os.path.join(in_path_dir, in_name)
        if not os.path.isfile(in_fullpath):
            continue
        out_name = 'ui_' + in_name.replace('.ui', '.py')
        out_fullpath = os.path.join(out_path_dir, out_name)
        compile_file(in_fullpath, out_fullpath)


if __name__ == '__main__':
    # Compile base Windows
    in_windows_dir = './ui/windows'
    out_windows_dir = './python/qtLearn/windows'
    compile_directory(in_windows_dir, out_windows_dir)

    # Compile each Window folder (and each Form)
    for name in sorted(os.listdir(in_windows_dir)):
        in_dir = os.path.join(in_windows_dir, name)
        if not os.path.isdir(in_dir):
            continue
        out_dir = os.path.join(out_windows_dir, name)
        compile_directory(in_dir, out_dir)

        # Compile Forms sub-folder.
        in_dir = os.path.join(in_windows_dir, name, 'forms')
        if not os.path.isdir(in_dir):
            continue
        out_dir = os.path.join(out_windows_dir, name, 'forms')
        compile_directory(in_dir, out_dir)

    # Compile base Widgets
    in_widgets_dir = './ui/widgets'
    out_widgets_dir = './python/qtLearn/widgets'
    compile_directory(in_widgets_dir, out_widgets_dir)

    # Compile each Widget folder
    for name in sorted(os.listdir(in_widgets_dir)):
        in_dir = os.path.join(in_widgets_dir, name)
        if not os.path.isdir(in_dir):
            continue
        out_dir = os.path.join(out_widgets_dir, name)
        compile_directory(in_dir, out_dir)

    # Top level UI files
    compile_directory('./ui', './python/qtLearn')
    exit()
