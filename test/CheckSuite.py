import unittest
from TestUtils import TestChecker
from AST import *
 
class CheckSuite(unittest.TestCase):

    # def test_no_entry_point(self):
    #     input = "class a{}"
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,600))    

    # def test_no_entry_point_success(self):
    #     input = "class Program{}"
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,601))

    # def test_nep_class(self):
    #     input = """class a {} class b {} class a {}"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,602))    

    # def test_no_main(self):
    #     input = """class a {} class b {} class a {} class Program{}"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,603))  

    # def test_redeclared_class(self):
    #     input = """class a {} class b {} class a {} class Program{func @main():void {}}"""
    #     expect = "Redeclared Class: a"
    #     self.assertTrue(TestChecker.test(input,expect,604)) 

    # def test_most_simple_program(self):
    #     input = """
    #     class Program {
    #         func @main():void {} 
    #         func @main():int {}   
    #     }""" 
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,605)) 

    # def test_no_entry_point_param(self):
    #     input = """class Program {
    #         func @main(a:int):void {}
    #     }"""
    #     expect = "No Entry Point"   
    #     self.assertTrue(TestChecker.test(input,expect,606)) 

    # def test_no_entry_point_type(self):
    #     input = """class a {} class b {} class a {} class Program{func @main():int {}}"""
    #     expect = "No Entry Point"
    #     self.assertTrue(TestChecker.test(input,expect,607)) 

    # def test_full_program(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         var a:int;
    #         var b:int;
    #         var a:int;
    #     }
    #     """
    #     expect = "Redeclared Attribute: a"
    #     self.assertTrue(TestChecker.test(input,expect,608)) 

    # def test_redeclared_var_xyz(self):
    #     input = """
    #     class A {
    #         var @abc:int;
    #         func xyz(): int {}
    #         var xyz:int;
    #     }

    #     class Program {
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Redeclared Attribute: xyz"
    #     self.assertTrue(TestChecker.test(input,expect,609)) 

    # def test_redeclared_method_main(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,610)) 

    # def test_redeclared_static_diff_class(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         var @x:int;
    #     }

    #     class A {
    #         var @x:int;
    #     }
    #     """
    #     expect = "Redeclared Attribute: @x"
    #     self.assertTrue(TestChecker.test(input,expect,611)) 

    # def test_redeclared_static_same_class(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         var @x:int;
    #         var @x:float;
    #     }
    #     """
    #     expect = "Redeclared Attribute: @x"
    #     self.assertTrue(TestChecker.test(input,expect,612)) 

    # def test_redeclared_io(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         var x:int;
    #     }
    #     class io {
    #         var x:int;
    #     }
    #     """
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input,expect,613)) 

    # def test_redeclared_io2(self):
    #     input = """
    #     class TestParent <- io {}
    #     class Program {
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Redeclared Class: io"
    #     self.assertTrue(TestChecker.test(input,expect,614)) 

    # def test_redeclared_main(self):
    #     input = """
    #     class Program {
    #         func @main():int {}  
    #         func @main():void {}
    #     }""" 
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,615)) 

    # def test_redeclared_constructor(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         func constructor() {}
    #         func constructor() {}
    #         func a():int {}
    #         func a():float {}
    #     }
    #     """
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,616)) 

    # def test_redeclared_constructor_2(self):
    #     input = """
    #     class Program {
    #         func @main():void {}
    #         func constructor() {}
    #         func constructor(x:int) {}
    #         func a():int {}
    #         func a():float {}
    #     }
    #     """
    #     expect = "Redeclared Method: a"
    #     self.assertTrue(TestChecker.test(input,expect,617))

    # def test_declared_main2(self):
    #     input = """
    #     class Program {
    #         func @main(a:int):void {}  
    #         func @main():void {}
    #     }""" 
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,618)) 

    # def test_declared_main3(self):
    #     input = """
    #     class Program {
    #         func @main(a:int):void {}  
    #         func @main():void {}
    #     }""" 
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,619)) 

    # def test_declared_main4(self):
    #     input = """
    #     class Program {
    #         var @main:int;  
    #         func @main():void {}
    #     }""" 
    #     expect = "Redeclared Method: @main"
    #     self.assertTrue(TestChecker.test(input,expect,620)) 

    # def test_redeclared_program(self):
    #     input = """
    #     class Program {}
    #     class Program {func @main():void {}}
    #     """
    #     expect = "Redeclared Class: Program"
    #     self.assertTrue(TestChecker.test(input,expect,621)) 

    # def test_decl_in_method(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:X;
    #             m.a();
    #         }
    #     }
    #     """
    #     expect = "Undeclared Class: X"
    #     self.assertTrue(TestChecker.test(input,expect,622)) 

    # def test_decl_in_method_with_parent(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:X;
    #             m.a();
    #         }
    #     }
    #     class X {
    #         var a: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
    #     self.assertTrue(TestChecker.test(input,expect,623)) 

    # def test_decl_in_method_with_parent2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:X;
    #             m.a();
    #         }
    #     }
    #     class X {
    #         func a():int {}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
    #     self.assertTrue(TestChecker.test(input,expect,624)) 

    # def test_decl_in_method_with_parent3(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:X;
    #             m.a();
    #         }
    #     }
    #     class Y <- X {}
    #     class Y {
    #         func a():int {}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
    #     self.assertTrue(TestChecker.test(input,expect,625))

    # def test_decl_in_method_with_parent4(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:X;
    #             k.a();
    #         }
    #         func k():void {}
    #     }
    #     class Y <- X {}
    #     class Y {
    #         func a():int {}
    #     }
    #     """
    #     expect = "Undeclared Identifier: k"
    #     self.assertTrue(TestChecker.test(input,expect,626))

    # def test_decl_in_method_with_wrong_type(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var m:int;
    #             m.a();
    #         }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(m),Id(a),[])"
    #     self.assertTrue(TestChecker.test(input,expect,627)) 

    # def test_attr_decl_with_class_type(self):
    #     input = """
    #     class Program {
    #         var m: X;
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Undeclared Class: X"
    #     self.assertTrue(TestChecker.test(input,expect,628)) 

    # def test_call_stmt6(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: B;
    #             x.@abc();
    #         }
    #         func @x():void {}
    #     } 
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc():void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(x),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,629)) 

    # def test_call_stmt5(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             x.@abcd();
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc():void {}
    #     }
    #     """
    #     expect = "Undeclared Method: @abcd"
    #     self.assertTrue(TestChecker.test(input,expect,630))

    # def test_call_stmt4(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             C.@abc();
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc():void {}
    #     }
    #     class C {}
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(C),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,631))

    # def test_call_stmt3(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc();
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         var @abc:int;
    #     }
    #     class C {}
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(B),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,632))

    # def test_call_stmt2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc();
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc():int {}
    #     }
    #     class C {}
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(B),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,633))

    # def test_array_type(self):
    #     input = """
    #     class Program {
    #         var x: [5]D;
    #         func @main():void {
    #         }
    #     }
    #     class B <- A {
    #     }
    #     class B {
    #     }
    #     class C {}
    #     """
    #     expect = "Undeclared Class: D"
    #     self.assertTrue(TestChecker.test(input,expect,634))

    # def test_call_stmt(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc();
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc(a:int):void {}
    #     }
    #     class C {}
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(B),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,635))

    # def test_call_stmt_param_1(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc(y);
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc(a:int):void {}
    #     }
    #     class C {}
    #     """
    #     expect = "Undeclared Identifier: y"
    #     self.assertTrue(TestChecker.test(input,expect,636))

    # def test_call_stmt_param_2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc(x);
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc(a:int):void {}
    #     }
    #     class C {}
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(B),Id(@abc),[Id(x)])"
    #     self.assertTrue(TestChecker.test(input,expect,637))

    # def test_method_decl_type_wrong(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x: A;
    #             B.@abc(x);
    #         }
    #         func @x():void {}
    #     }
    #     class B <- A {
    #         func @y():void {}
    #     }
    #     class B {
    #         func @abc(a:[4]D):void {}
    #     }
    #     class C {}
    #     """
    #     expect = "Undeclared Class: D"
    #     self.assertTrue(TestChecker.test(input,expect,638))

    # def test_assign(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             const x:int = 1;
    #             x := 1;
    #         }
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(Id(x),IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,639))
    
    # def test_assign2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             const x:A = new A();
    #             x.x := 1;
    #         }
    #     }
    #     class A {
    #         const x:int;
    #     }
    #     """
    #     expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Id(x),Id(x)),IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,640))

    # def test_assign3(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             const b:A = new A();
    #             b.x := "abc";
    #         }
    #     }
    #     class A {
    #         var x:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(FieldAccess(Id(b),Id(x)),StringLit(abc))"
    #     self.assertTrue(TestChecker.test(input,expect,641))

    # def test_call_stmt7(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var a:int;
    #             a.@abc();
    #         }
    #     }
    #     class A {
    #         func @abc():void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: Call(Id(a),Id(@abc),[])"
    #     self.assertTrue(TestChecker.test(input,expect,642))

    # def test_field_access(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:int;
    #             b.@x := 1;
    #         }
    #     }
    #     class A {
    #         var @x:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(b),Id(@x))"
    #     self.assertTrue(TestChecker.test(input,expect,643))

    # def test_field_access2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             b := A.@y;
    #         }
    #     }
    #     class A{
    #         var @x:int;
    #     }
    #     """
    #     expect = "Undeclared Attribute: @y"
    #     self.assertTrue(TestChecker.test(input,expect,644))

    # def test_field_access3(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := B.@x;
    #         }
    #     }
    #     class A{
    #         var @x:int;
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(B),Id(@x))"
    #     self.assertTrue(TestChecker.test(input,expect,645))

    # def test_field_access4(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := A.@x;
    #         }
    #     }
    #     class A{
    #         func @x():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(A),Id(@x))"
    #     self.assertTrue(TestChecker.test(input,expect,646))

    # def test_field_access5(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:string;
    #             x := b.x;
    #         }
    #         var b:int;
    #     }
    #     class A{
    #         var x:int;
    #     }
    #     class B{}
    #     """
    #     expect = "Undeclared Identifier: b"
    #     self.assertTrue(TestChecker.test(input,expect,647))

    # def test_field_access6(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:int;
    #             var x:string;
    #             x := b.x;
    #         }
    #     }
    #     class A{
    #         var x:int;
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(b),Id(x))"
    #     self.assertTrue(TestChecker.test(input,expect,648))

    # def test_field_access7(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := b.y;
    #         }
    #     }
    #     class A{
    #         var x:int;
    #     }
    #     class B{}
    #     """
    #     expect = "Undeclared Attribute: y"
    #     self.assertTrue(TestChecker.test(input,expect,649))

    # def test_field_access8(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := b.y;
    #         }
    #     }
    #     class A{
    #         func y():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: FieldAccess(Id(b),Id(y))"
    #     self.assertTrue(TestChecker.test(input,expect,650))

    # def test_call_expr(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := b.x();
    #         }
    #     }
    #     class A{
    #         func y():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Undeclared Method: x"
    #     self.assertTrue(TestChecker.test(input,expect,651))

    # def test_call_expr2(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := b.@x();
    #         }
    #     }
    #     class A{
    #         func y():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Undeclared Method: @x"
    #     self.assertTrue(TestChecker.test(input,expect,652))

    # def test_call_expr3(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := b.@x();
    #         }
    #     }
    #     class A{
    #         func @x():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(b),Id(@x),[])"
    #     self.assertTrue(TestChecker.test(input,expect,653))

    # def test_call_expr4(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := x.@x();
    #         }
    #     }
    #     class A{
    #         func @x():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(x),Id(@x),[])"
    #     self.assertTrue(TestChecker.test(input,expect,654))

    # def test_call_expr5(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := B.@x();
    #         }
    #     }
    #     class A{
    #         func @x():int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(B),Id(@x),[])"
    #     self.assertTrue(TestChecker.test(input,expect,655))

    # def test_call_expr6(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := A.@x();
    #         }
    #     }
    #     class A{
    #         var @x:int;
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(@x),[])"
    #     self.assertTrue(TestChecker.test(input,expect,656))

    # def test_call_expr7(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := A.@x();
    #         }
    #     }
    #     class A{
    #         func @x():void {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(@x),[])"
    #     self.assertTrue(TestChecker.test(input,expect,657))

    # def test_call_expr8(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := A.@x(x);
    #         }
    #     }
    #     class A{
    #         func @x(a:int, b:int):int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(@x),[Id(x)])"
    #     self.assertTrue(TestChecker.test(input,expect,658))

    # def test_call_expr9(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var b:A;
    #             var x:string;
    #             x := A.@x(x, b);
    #         }
    #     }
    #     class A{
    #         func @x(a:int, b:int):int {}
    #     }
    #     class B{}
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(A),Id(@x),[Id(x),Id(b)])"
    #     self.assertTrue(TestChecker.test(input,expect,659))

    # def test_call_expr10(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             x := a.b();
    #         }
    #     }
    #     class A {}
    #     """
    #     expect = "Undeclared Identifier: a"
    #     self.assertTrue(TestChecker.test(input,expect,660))

    # def test_call_expr11(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             var a:int;
    #             x := a.b();
    #         }
    #     }
    #     class A {
    #         func b():int {}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(b),[])"
    #     self.assertTrue(TestChecker.test(input,expect,661))

    # def test_call_expr12(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             var a:A;
    #             x := a.c();
    #         }
    #     }
    #     class A {
    #         func b():int {}
    #         var c:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(c),[])"
    #     self.assertTrue(TestChecker.test(input,expect,662))

    # def test_call_expr13(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             var a:A;
    #             x := a.b();
    #         }
    #     }
    #     class A {
    #         func b():void {}
    #         var c:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(b),[])"
    #     self.assertTrue(TestChecker.test(input,expect,663))

    # def test_call_expr14(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             var a:A;
    #             var y:string;
    #             var z:int;
    #             x := a.b(y);
    #         }
    #     }
    #     class A {
    #         func b(a:int, b:int):int {}
    #         var c:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(b),[Id(y)])"
    #     self.assertTrue(TestChecker.test(input,expect,664))

    # def test_call_expr15(self):
    #     input = """
    #     class Program {
    #         func @main():void {
    #             var x:int;
    #             var a:A;
    #             var y:string;
    #             var z:int;
    #             x := a.b(y, z);
    #         }
    #     }
    #     class A {
    #         func b(a:int, b:int):int {}
    #         var c:int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: CallExpr(Id(a),Id(b),[Id(y),Id(z)])"
    #     self.assertTrue(TestChecker.test(input,expect,665))

    # def test_var_decl_init(self):
    #     input = """
    #     class Program {
    #         var x:string = 1;
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(x),StringType,IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,666))

    # def test_const_decl_init(self):
    #     input = """
    #     class Program {
    #         const x:string = 1;
    #         func @main():void {}
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: ConstDecl(Id(x),StringType,IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,667))
    # def test_arr_decl(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [10]int = [1,2,3];
    #       }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(x),ArrayType(10,IntType),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,668))

    # def test_arr_decl2(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]string = [1,2,3];
    #       }
    #     }
    #     """
    #     expect = "Type Mismatch In Declaration: VarDecl(Id(x),ArrayType(3,StringType),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,669))

    # def test_new_expr(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var a: int;
    #         var b: string;
    #         var c: A = new A(b);
    #       }
    #     }
    #     class A {
    #       func constructor() {}
    #       func constructor(x:int) {}
    #       func constructor(x:int, y: string) {}
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: NewExpr(Id(A),[Id(b)])"
    #     self.assertTrue(TestChecker.test(input,expect,670))

    # def test_assign_ar1(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]string;
    #         x := [1];
    #       }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x),[IntLit(1)])"
    #     self.assertTrue(TestChecker.test(input,expect,671))

    # def test_assign_ar2(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]string;
    #         x := [1, 2, 3];
    #       }
    #     }
    #     """
    #     expect = "Type Mismatch In Statement: AssignStmt(Id(x),[IntLit(1),IntLit(2),IntLit(3)])"
    #     self.assertTrue(TestChecker.test(input,expect,672))

    # def test_assign_ar3(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]float;
    #         x := [1, 2, "hello"];
    #       }
    #     }
    #     """
    #     expect = "Illegal Array Literal: [IntLit(1),IntLit(2),StringLit(hello)]"
    #     self.assertTrue(TestChecker.test(input,expect,673))

    # def test_array_cell(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]float;
    #         var y: A = new A();
    #         y.a := [1, 2, 3.5];
    #         y.b[1] := 2;

    #       }
    #     }
    #     class A {
    #       var a: [3]int;
    #       var b: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(FieldAccess(Id(y),Id(b)),IntLit(1))"
    #     self.assertTrue(TestChecker.test(input,expect,674))

    # def test_array_cell2(self):
    #     input = """
    #     class Program {
    #       func @main():void {
    #         var x: [3]float;
    #         var y: A = new A();
    #         y.a := [1, 2, 3.5];
    #         y.a["hello"] := 2;

    #       }
    #     }
    #     class A {
    #       var a: [3]int;
    #       var b: int;
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: ArrayCell(FieldAccess(Id(y),Id(a)),StringLit(hello))"
    #     self.assertTrue(TestChecker.test(input,expect,675))

    # def test_binary_op(self):
    #     input = """
    #     class Program {
    #       func @main() :void {
    #         var x: int;
    #         var y: string;
    #         var z: int = x + y;
    #       }
    #     }
    #     """
    #     expect = "Type Mismatch In Expression: BinaryOp(+,Id(x),Id(y))"
    #     self.assertTrue(TestChecker.test(input,expect,676))