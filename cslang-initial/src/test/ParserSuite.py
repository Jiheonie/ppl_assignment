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
        _input = """var a: bool = false;"""
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

    def test_func_params(self):
        _input = """func A(a: int, b: int): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 314))

    def test_static_func(self):
        _input = """func @main(a: int, b: int): int {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 315))

    def test_class_static_func(self):
        _input = """
        class Program {
            func @main():int {
                var r, s: int;
                r := 2.0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 316))

    # def test_long_prog(self):
    #     _input = """
    #     class Shape {
    #         var @numOfShape: int = 0;
    #         const immutableAttribute: int = 0;
    #         var length, width: int;
    #         func @getNumOfShape():int {
    #             return @numOfShape;
    #         }
    #     }
    #     class Shape <- Retangle {
    #         func getArea():int {
    #             return self.length * self.width;
    #         }
    #     }
    #     class Program {
    #         func @main():void {
    #             io.@writeInt(Shape.@numOfShape);
    #         }
    #     }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(_input, expect, 317))

    def test_cmt_block(self):
        _input = """a := 5;//this is a line comment"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 318))

    def test_array(self):
        _input = """[1 + 2, 3, true, 1.2, "hwng", abc, [1, 2]]"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 319))

    def test_decl_array(self):
        _input = """var a: [5]int = [1 + 2, 3, true, 1.2, "hwng", abc, [1, 2]];"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 320))

    def test_obj_decl(self):
        _input = """a := new X();"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 321))