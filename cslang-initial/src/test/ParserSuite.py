import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_decl_class_empty(self):
        _input = """class A{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 301))

    def test_declare_class_with_var_decl(self):
        _input = """class A{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 302))

    def test_decl_class_inherit(self):
        _input = """class A <- B{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 303))

    def test_decl_var(self):
        _input = """var width: int;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 304))

    def test_decl_const(self):
        _input = """const width: int;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 305))

    def test_decl_multi(self):
        _input = """class Program{ const a, b: int = 3, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 306))

    def test_decl_var_value(self):
        _input = """var delta: int = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 307))

    def test_exp(self):
        _input = """a := 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 308))

    def test_assign_stmt(self):
        _input = """a := 1 + 2;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 309))

    def test_attr_decl(self):
        _input = """var a: int = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 310))

    def test_plus_exp(self):
        _input = """1 + 2"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 311))

    def test_constructor(self):
        _input = """func A() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 312))

    def test_func(self):
        _input = """func A(): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 313))

    def test_func_param(self):
        _input = """func A(a: int): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 314))

    def test_func_params(self):
        _input = """func A(a: int, b: int): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 315))

    def test_static_func(self):
        _input = """func @main(a: int, b: int): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 316))

    def test_static_func(self):
        _input = """class Program {func @main():int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 316))
