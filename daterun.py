#!/usr/bin/python3

import datetime
import os
import sys


args = [datetime.datetime.now().strftime(x) for x in sys.argv[1:]]
os.execvp(args[0], args)
