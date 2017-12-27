#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)

sys.path.append('')

from app import app as application
