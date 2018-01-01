#!/usr/bin/python
import sys
import logging

logging.basicConfig(stream=sys.stderr)

sys.path.append('')

from middleware import app as application
from middleware import views
