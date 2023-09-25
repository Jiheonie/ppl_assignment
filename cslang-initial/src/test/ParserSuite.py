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
        _input = """class A <- B{var width: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 304))

    def test_decl_const(self):
        _input = """class A <- B{const width: int;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 305))

    def test_decl_multi(self):
        _input = """class Program{ const a, b: int = 3, 6;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 306))

    def test_decl_var_value(self):
        _input = """class A <- B{var delta: int = 3;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 307))

    def test_exp(self):
        _input = """class A <- B{const a :int = 1;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 308))

    def test_assign_stmt(self):
        _input = """class A <- B{a := 1 + 2;}"""
        expect = "Error on line 1 col 13: a"
        self.assertTrue(TestParser.test(_input, expect, 309))

    def test_attr_decl(self):
        _input = """class A <- B{var @a: bool = false;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 310))

    def test_plus_exp(self):
        _input = """1 + 2"""
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(_input, expect, 311))

    def test_wrong_constructor(self):
        _input = """class A <- B{func A() {}}"""
        expect = "Error on line 1 col 22: {"
        self.assertTrue(TestParser.test(_input, expect, 312))

    def test_func(self):
        _input = """class A <- B{func A(): int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 313))

    def test_func_params(self):
        _input = """class A <- B{func A(a: int, b: int): int {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 314))

    def test_static_func(self):
        _input = """class Program {func @main(): void {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 315))

    def test_class_static_func(self):
        _input = """
        class Program {
            func @main():void {
                var r, s: int;
                r := 2.0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 316))

    def test_long_prog1(self):
        _input = """
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea():int {
                return self.length * self.width;
            }
        }
        class Program {
            func @main():void {
                io.@writeInt(Shape.@numOfShape);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 317))

    def test_cmt_block(self):
        _input = """class A <- B{var a :int = 5;//this is a line comment}"""
        expect = "Error on line 1 col 53: <EOF>"
        self.assertTrue(TestParser.test(_input, expect, 318))

    def test_array(self):
        _input = """class A <- B{
            var a :int = 5;//this is a line comment
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 319))

    def test_decl_array(self):
        _input = """class A <- B{var a: [5]int = [1 + 2, 3, true, 1.2, "hwng", abc, [1, 2]];
        var b: [5]int = [];}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 320))

    def test_obj_decl(self):
        _input = """class A <- B{a := new X(1, a + b);}"""
        expect = "Error on line 1 col 13: a"
        self.assertTrue(TestParser.test(_input, expect, 321))

    def test_func_call(self):
        _input = """class A <- B{var x :int = A(1 + 2, 2 + 1);}"""
        expect = "Error on line 1 col 27: ("
        self.assertTrue(TestParser.test(_input, expect, 322))

    def test_arr_ele(self):
        _input = """class A <- B{var x :int = A[1];}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 323))

    def test_if_stmt(self):
        _input = """class A {if {i := 0;} j > i {j := j - 1;}}"""
        expect = "Error on line 1 col 9: if"
        self.assertTrue(TestParser.test(_input, expect, 324))
        
    def test_if_stmt2(self):
        _input = """class A <- B{func A(): int {if n == 0 {return 1;}
            else {return n * @fact(n - 1);}}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 325))

    def test_for_stmt(self):
        _input = """class A {for i := 0; i < 10; i := i + 1 {}}"""
        expect = "Error on line 1 col 9: for"
        self.assertTrue(TestParser.test(_input, expect, 326))

    def test_method_invocation(self):
        _input = """class A <- B{func A(): int {Shape.@getNumOfShape();}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 327))

    def test_return(self):
        _input = """return true;"""
        expect = "Error on line 1 col 0: return"
        self.assertTrue(TestParser.test(_input, expect, 328))

    def test_long_prog2(self):
        _input = """
        class Shape {
            var @numOfShape: int = 0;
            const immutableAttribute: int = 0;
            var length, width: int;
            func @getNumOfShape():int {
                return @numOfShape;
            }
        }
        class Shape <- Retangle {
            func getArea():int {
                return self.length * self.width;
            }
        }
        class Program {
            func @main():void {
                io.@writeInt(Shape.@numOfShape);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 329))

    def test_params_multiple(self):
        _input = """class A <- B{func functi(a,b,c: int, d: int): void {}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 330))

    def test_invalid_id(self):
        _input = """class A <- B{var 1abc: int = 1;}"""
        expect = "Error on line 1 col 17: 1"
        self.assertTrue(TestParser.test(_input, expect, 331))

    def test_arr_ele1(self):
        _input = """class A <- B{func X(): int {a[3+x.foo(2)] := a[b[2]] +3;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 332))

    def test_arr_ele2(self):
        _input = """class A <- B{func A(): int {x.b[2] := x.m()[3];}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 333))

    def test_attr_decl1(self):
        _input = """class A <- B{const My1stCons, My2ndCons: int = 1 + 5, 2;
        var @x, @y : int = 0, 0;}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 334))

    def test_class_with_self1(self):
        _input = """
        class Program {
            var a: int = 1;    
        
            func constructor() {
                x := self.a;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 335))

    def test_assign_stmt1(self):
        _input = """class A <- B{
            func X(): void {
                self.aPI := null;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 336))

    def test_if_stmt1(self):
        _input = """if {i := 0;} j > i {j := j - 1;} else {j := j + 1;}"""
        expect = "Error on line 1 col 0: if"
        self.assertTrue(TestParser.test(_input, expect, 337))
    
    def test_for_stmt1(self):
        _input = """for i := 0; i < 10; i := i + 1 {
        io.@writeInt(i);
        }"""
        expect = "Error on line 1 col 0: for"
        self.assertTrue(TestParser.test(_input, expect, 338))

    def test_break1(self):
        _input = """break;"""
        expect = "Error on line 1 col 0: break"
        self.assertTrue(TestParser.test(_input, expect, 339))

    def test_continue(self):
        _input = """continue;"""
        expect = "Error on line 1 col 0: continue"
        self.assertTrue(TestParser.test(_input, expect, 340))

    def test_block_stmt(self):
        _input = """class A {func constructor() {
        var r, s: int;
        r := 2.0;
        var a, b: [5]int;
        s := r * r * self.myPI;
        a[0] := s;
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 341))

    def test_program_234523(self):
        _input = """class Program {
      var x: int = 65;
      func @fact(n: int):int {
            if n == 0 {return 1;}
            else {return n * @fact(n - 1);}
        }
        func  @inc( n, delta: int):void {
            n := n + delta;
            return n;
        }
        func @main():void {
            var delta: int = @fact(3);
            @inc(self.x, delta);
            io.@writeInt(self.x);
        }}"""
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 342))

    def test_program_error_23445(self):
        _input = """
        class Program {
            var a,b,c:int
            func @main(n: int): int {}
        }
        """
        expect = "Error on line 4 col 12: func"
        self.assertTrue(TestParser.test(_input, expect, 343))

    def test_program_with_for_287249582(self):
        _input = """
        class Program {
            var a,b,c:int;
            func @main(): void {
                for i := 0; i < 10; i := i + 1 {
                    io.@writeInt(i);
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 344))

    def test_program_error_85974398257(self):
        _input = """
        class Program {
            var a,b,c,d:int = 1,2,3;
        }
        """
        expect = "Error on line 3 col 35: ;"
        self.assertTrue(TestParser.test(_input, expect, 345))

    def test_program_error_58492375(self):
        _input = """
        class A {
          func constructor() {
            numOfShape;
          }  
        }
        """
        expect = "Error on line 4 col 22: ;"
        self.assertTrue(TestParser.test(_input, expect, 346))
        
    def test_program_error_9028374592(self):
        _input = """
        class A {
          func constructor {
            numOfShape();
          }  
        }
        """
        expect = "Error on line 3 col 27: {"
        self.assertTrue(TestParser.test(_input, expect, 347))

    def test_program_error_5689370941(self):
        _input = """
        class A {
          func constructor() {
            x := numOfShape();
          }  
        }
        """
        expect = "Error on line 4 col 27: ("
        self.assertTrue(TestParser.test(_input, expect, 348))

    def test_program_error_5689370942(self):
        _input = """
        class A {
          func constructor() {
            x := @numOfShape();
          }  
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 349)) 
        
    def test_program_error_02983475(self):
        _input = """
        class A {
          func constructor() {
            a@x := @numOfShape();
          }  
        }
        """
        expect = "Error on line 4 col 13: @x"
        self.assertTrue(TestParser.test(_input, expect, 350)) 

    def test_invalid_main_123789401389(self):
        _input = """
        class A {
            func @main(): void {}
        }
        """
        expect = "Error on line 3 col 17: @main"
        self.assertTrue(TestParser.test(_input, expect, 351)) 
