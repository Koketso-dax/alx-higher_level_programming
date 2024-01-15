#!/usr/bin/python3
""" Base Class Unit Test """

import unittest
from models.base import Base

class TestBaseModel(unittest.TestCase, Base):
    """ Unit Tests for Base Class """

    def test_id_indexing(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_assign_id(self):
        id_base = Base(42)
        self.assertEqual(id_base.id, 42)

    def test_negative_id(self):
        neg_id = Base(-12)
        self.assertEqual(neg_id.id, -12)

    def test_custom_ids(self):
        b1 = Base()
        b2 = Base()
        id_base = Base(100)
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(id_base.id, 100)
        self.assertEqual(b3.id, 3)

if __name__ == '__main__':
    unittest.main()
