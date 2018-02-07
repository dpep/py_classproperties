classproperty
======

#### Install
```pip install classproperties```


#### Usage
```
from classproperties import classproperty

class Foo:
  @classproperty
  def prop():
    return 'hi there'

  @classproperty
  def other(cls):
    return 'also works'


Foo.prop
Foo.other
```
