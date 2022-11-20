#!/usr/bin/env python
import sys
from distutils.core import setup

setup(name='RaiPlaysound',
      version='1.0',
      description='RaiPlaySound - Podcast Feed generator',
      author='timendum',
      url='https://github.com/timendum/raiplaysound',
      package_dir={'raiplaysound': ''},
      packages=['raiplaysound'],
      data_files=[(sys.prefix + '/share/raiplaysound', ['index.template'])]
     )
