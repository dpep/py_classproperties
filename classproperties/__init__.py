__author__ = 'dpepper'
__version__ = '0.2.0'

import sys


class classproperty(object):
  def __init__(self, func):
    self.func = func

  def __get__(self, obj, objtype):
    args = []

    if sys.version_info[0] == 2:
      code = self.func.func_code
    else:
      code = self.func.__code__

    if code.co_argcount > 0:
      args.append(objtype)

    return self.func(*args)
