__author__ = 'dpepper'
__version__ = '0.1.3'


class classproperty(object):
  def __init__(self, func):
    self.func = func

  def __get__(self, obj, owner):
    args = []

    if self.func.func_code.co_argcount > 0:
      args.append(owner)

    return self.func(*args)
