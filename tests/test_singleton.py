import unittest
from unittest import TestCase

from singleton.singleton import Singleton


class TestSingleton(TestCase):
    def test(self):
        foo = Foo()
        bar = Foo()
        self.assertTrue(foo is bar)


class Foo(metaclass=Singleton):
    def __init__(self):
        self.name = "singleton test"


if __name__ == '__main__':
    unittest.main()
