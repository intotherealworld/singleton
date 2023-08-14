# Singleton

This is a meta class which make a class as a singleton class

## Usage
```python
from singleton.singleton import Singleton

class Foo(metaclass=Singleton):
    ...

# foo and bar is the same instance
foo = Foo()
bar = Foo()
```