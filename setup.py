#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ast
from io import open
import os.path as osp
from setuptools import setup


HERE = osp.abspath(osp.dirname(__file__))
NAME = 'pibooth_extra_lights_vim4'

# Read the version and the description without importing the plugin, which
# imports pibooth: the package must build where pibooth is not installed.
with open(osp.join(HERE, NAME + '.py'), encoding='utf-8') as fp:
    MODULE = ast.parse(fp.read())
DESCRIPTION = ast.get_docstring(MODULE)
VERSION = next(node.value.value for node in MODULE.body if isinstance(node, ast.Assign)
               and any(getattr(target, 'id', None) == '__version__' for target in node.targets))


def main():
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=open(osp.join(HERE, 'README.rst'), encoding='utf-8').read(),
        long_description_content_type='text/x-rst',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Other Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Natural Language :: English',
            'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
        ],
        author="Vincent Verdeil, Antoine Rousseaux, Christophe (ceeeeb)",
        url="https://github.com/ceeeeb/pibooth-extra-lights-vim4",
        download_url="https://github.com/ceeeeb/pibooth-extra-lights-vim4/archive/{}.tar.gz".format(VERSION),
        license='GPLv3',
        platforms=['unix', 'linux'],
        keywords=[
            'Raspberry Pi',
            'camera',
            'photobooth'
        ],
        py_modules=['pibooth_extra_lights_vim4'],
        python_requires=">=3.6",
        install_requires=[
            'pibooth-ceeeeb>=2.0.9',
        ],
        zip_safe=False,  # Don't install the lib as an .egg zipfile
        entry_points={'pibooth': ["pibooth_extra_lights_vim4 = pibooth_extra_lights_vim4"]},
    )


if __name__ == '__main__':
    main()
