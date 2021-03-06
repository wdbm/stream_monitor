#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import setuptools

def main():

    setuptools.setup(
        name             = "stream_monitor",
        version          = "2018.08.26.1543",
        description      = "monitoring and alerting program for data streams such as recording files that update regularly",
        long_description = long_description(),
        url              = "https://github.com/wdbm/stream_monitor",
        author           = "Will Breaden Madden",
        author_email     = "wbm@protonmail.ch",
        license          = "GPLv3",
        packages         = setuptools.find_packages(),
        install_requires = [
                           "docopt",
                           "lock",
                           "scalar",
                           "technicolor",
                           "tonescale"
                           ],
        python_requires  = ">=3",
        entry_points     = {
                           "console_scripts": ("stream_monitor = stream_monitor.__init__:main")
                           },
        zip_safe         = False
    )

def long_description(
    filename = "README.md"
    ):

    if os.path.isfile(os.path.expandvars(filename)):
        try:
            import pypandoc
            long_description = pypandoc.convert_file(filename, "rst")
        except ImportError:
            long_description = open(filename).read()
    else:
        long_description = ""
    return long_description

if __name__ == "__main__":
    main()
