import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # def test_simple_program(self):
    #     """Simple program"""
    #     input = """program"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 301))

    def test_decl_class_empty(self):
        input="""class A{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_declare_class_with_var_decl(self):
        input = """class A{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_decl_var(self):
        input="""var width: int;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_exp(self):
        input= """a == 1"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))

    # def text_decl(self):
    #     input = """a = 1"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 306))
