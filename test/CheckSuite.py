import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):

    def test_no_entry_point(self):
        input = "class a{}"
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,400))    

    def test_no_entry_point_success(self):
        input = "class Program{}"
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_nep_class(self):
        input = """class a {} class b {} class a {}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,402))    

    def test_no_main(self):
        input = """class a {} class b {} class a {} class Program{}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,403))  

    def test_redeclared_class(self):
        input = """class a {} class b {} class a {} class Program{func @main():void {}}"""
        expect = "Redeclared Class: a"
        self.assertTrue(TestChecker.test(input,expect,404)) 

    def test_most_simple_program(self):
        input = """
        class Program {
            func @main():void {} 
            func @main():int {}   
        }""" 
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,405)) 

    def test_no_entry_point_param(self):
        input = """class Program {
            func @main(a:int):void {}
        }"""
        expect = "No Entry Point"   
        self.assertTrue(TestChecker.test(input,expect,406)) 

    def test_no_entry_point_type(self):
        input = """class a {} class b {} class a {} class Program{func @main():int {}}"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,407)) 

    def test_full_program(self):
        input = """
        class Program {
            func @main():void {}
            var a:int;
            var b:int;
            var a:int;
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,408)) 

    def test_redeclared_var_xyz(self):
        input = """
        class A {
            var @abc:int;
            func xyz(): int {}
            var xyz:int;
        }

        class Program {
            func @main():void {}
        }
        """
        expect = "Redeclared Attribute: xyz"
        self.assertTrue(TestChecker.test(input,expect,409)) 

    def test_redeclared_method_main(self):
        input = """
        class Program {
            func @main():void {}
            func @main():void {}
        }
        """
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,410)) 

    def test_redeclared_static_diff_class(self):
        input = """
        class Program {
            func @main():void {}
            var @x:int;
        }

        class A {
            var @x:int;
        }
        """
        expect = "Redeclared Attribute: @x"
        self.assertTrue(TestChecker.test(input,expect,411)) 

    def test_redeclared_static_same_class(self):
        input = """
        class Program {
            func @main():void {}
            var @x:int;
            var @x:float;
        }
        """
        expect = "Redeclared Attribute: @x"
        self.assertTrue(TestChecker.test(input,expect,412)) 

    def test_redeclared_io(self):
        input = """
        class Program {
            func @main():void {}
            var x:int;
        }
        class io {
            var x:int;
        }
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,413)) 

    def test_redeclared_io2(self):
        input = """
        class TestParent <- io {}
        class Program {
            func @main():void {}
        }
        """
        expect = "Redeclared Class: io"
        self.assertTrue(TestChecker.test(input,expect,414)) 

    def test_redeclared_main(self):
        input = """
        class Program {
            func @main():int {}  
            func @main():void {}
        }""" 
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,415)) 

    def test_redeclared_constructor(self):
        input = """
        class Program {
            func @main():void {}
            func constructor() {}
            func constructor() {}
            func a():int {}
            func a():float {}
        }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,416)) 

    def test_redeclared_constructor_2(self):
        input = """
        class Program {
            func @main():void {}
            func constructor() {}
            func constructor(x:int) {}
            func a():int {}
            func a():float {}
        }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_declared_main2(self):
        input = """
        class Program {
            func @main(a:int):void {}  
            func @main():void {}
        }""" 
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,418)) 

    def test_declared_main3(self):
        input = """
        class Program {
            func @main(a:int):void {}  
            func @main():void {}
        }""" 
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,419)) 

    def test_declared_main4(self):
        input = """
        class Program {
            var @main:int;  
            func @main():void {}
        }""" 
        expect = "Redeclared Method: @main"
        self.assertTrue(TestChecker.test(input,expect,420)) 

    def test_redeclared_program(self):
        input = """
        class Program {}
        class Program {func @main():void {}}
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input,expect,421)) 

    def test_decl_in_method(self):
        input = """
        class Program {
            func @main():void {
                var m:X;
                m.a();
            }
        }
        """
        expect = "Undeclared Class: X"
        self.assertTrue(TestChecker.test(input,expect,422)) 

    def test_decl_in_method_with_parent(self):
        input = """
        class Program {
            func @main():void {
                var m:X;
                m.a();
            }
        }
        class X {
            var a: int;
        }
        """
        expect = "Undeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,423)) 

    def test_decl_in_method_with_parent2(self):
        input = """
        class Program {
            func @main():void {
                var m:X;
                m.a();
            }
        }
        class X {
            func a():int {}
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
        self.assertTrue(TestChecker.test(input,expect,424)) 

    def test_decl_in_method_with_parent3(self):
        input = """
        class Program {
            func @main():void {
                var m:X;
                m.a();
            }
        }
        class Y <- X {}
        class Y {
            func a():int {}
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
        self.assertTrue(TestChecker.test(input,expect,425))