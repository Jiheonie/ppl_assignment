import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program"""
        _input = """A"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 301))

    def test_decl_class_empty(self):
        _input = """class A{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 302))

    def test_declare_class_with_var_decl(self):
        _input = """class A{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 303))

    def test_decl_var(self):
        _input = """var width: int;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 304))

    def test_exp(self):
        _input = """a := 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 305))

    def test_attr_decl(self):
        _input = """var a: int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 306))

    def test_plus_exp(self):
        _input = """1 + 2"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 307))
