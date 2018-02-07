#!/usr/bin/python

import os
import sys
import unittest

sys.path = [ os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')) ] + sys.path
from classproperties import classproperty


class ArrayTest(unittest.TestCase):
    def test_basic(self):
        class Foo:
            a = 'a'

            @staticmethod
            def b():
                return 'b'

            @classmethod
            def c(cls):
                return 'c'

            def d(self):
                return 'd'

            @classproperty
            def p(cls):
                return 'p'


        self.assertEquals(
            Foo.a,
            'a'
        )

        self.assertEquals(
            Foo.b(),
            'b'
        )

        self.assertEquals(
            Foo.c(),
            'c'
        )

        self.assertEquals(
            Foo().d(),
            'd'
        )

        self.assertEquals(
            Foo.p,
            'p'
        )

        self.assertEquals(
            Foo().p,
            'p'
        )


if __name__ == '__main__':
    unittest.main()
