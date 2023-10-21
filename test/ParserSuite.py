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
        expect = "Error on line 1 col 32: +"
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
            func @main(): int {}
        }
        """
        # expect = "Error on line 3 col 17: @main"
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 351)) 

    def test_program_with_cmt_9573918(self):
        _input = """
        class Overload {
            func print(s: string): void {
                io.@writeStr(s);
            }
            
            func print(i: int): void {
                io.@writeInt(i);
                io.@writeStr("Enter an integer: ");
                var input : int = io.@readInt();
                io.@writeInt(input); // Echo input
            }
        }
        // ehllo
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 352)) 

    def test_program_with_cmt_479253(self):
        _input = """
        class Overload {
            func print(s: string): void {
                io.@writeStr(s);
                for i:=0; i<5; i:=i+1 { // for loop
                    if i==3 { 
                        continue; // skip rest of loop
                    }
                    io.@writeInt(i); 
                }

                io.@writeStr("Press 1 to exit: ");
                if input==1 {
                    break; // terminate loop
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 353)) 

    def test_program_with_logic_754829(self):
        _input = """
        class Program {
            func @main():int {
                io.@writeBool(!(10 == 5)); // boolean
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 354)) 

    def test_program_with_logic_7548212(self):
        _input = """
        class Program {
            func @main():int {
                var a:int = 1 + (2 + 3);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 355)) 

    def test_program_with_logic_78011902343819(self):
        _input = """
        class Program {
            func @main():int {
                str := "Hello " ^ "World!";
                io.@writeStr(str);

                var escapeStr : string = "First Line\nSecond Line"; 
                io.@writeStr(escapeStr);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 356)) 

    def test_obj_cre_798342504(self):
        _input = """
        class Program {
            func @main():int {
                var myObj : NewObj = new NewObj();
                myObj.a := null;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 357)) 

    def test_obj_cre_1928347(self):
        _input = """
        class Animal {
            var sound: string = "sound"
        }

        class Animal <- Dog {
            var sound: string = "Gau";
        }

        class Program {
            func @main():int {
                var hwng : Animal = new Dog();
                print(hwng.sound);
            }
        }
        """
        expect = "Error on line 4 col 8: }"
        self.assertTrue(TestParser.test(_input, expect, 358)) 

    def test_obj_cre_19284323457(self):
        _input = """
        class Animal {
            var sound: string = "sound";
        }

        class Animal <- Dog {
            var sound: string = "Gau";
        }

        class Program {
            func @main():int {
                var hwng : Animal = new Dog();
                print(hwng.sound);
            }
        }
        """
        expect = "Error on line 13 col 21: ("
        self.assertTrue(TestParser.test(_input, expect, 359)) 

    def test_obj_cre_192843232345435457(self):
        _input = """
        class Animal {
            var sound: string = "sound";
        }

        class Animal <- Dog {
            var sound: string = "Gau";
        }

        class Program {
            func @main():int {
                var hwng : Animal = new Dog();
                @writeStr(hwng.sound);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 360)) 

    def test_exp_509483753957938295(self):
        _input = """
        class Program {
            func @main():int {
                @ip.num[0] := -(123 + 456 / 2);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 361)) 

    def test_exp_509489284579515(self):
        _input = """
        class Program {
            func @main():int {
                @changeText(s[0], a[a[1+2]], "a" ^ "b");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 362)) 

    def test_exp_928347598(self):
        _input = """
        class Program {
            func @main():int {
                var s: [10]int;
                var a: [20]int = 
                @changeText(s[0], a[a[1+2]], "a" ^ "b");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 363)) 

    def test_exp_239485098700202(self):
        _input = """
        class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 364)) 

    def test_exp_9823475928(self):
        _input = """
        class Program {
            func @main():int {
                @isSth := !a.x[1] && b [2];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 365)) 

    def test_exp_548792834(self):
        _input = """
        class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 366))

    def test_exp_75849320(self):
        _input = """
        class Program {
            func @main():int {
                @text := a + b * c / d;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 367)) 

    def test_exp_47923842(self):
        _input = """
        class Program {
            func @main():int {
                @text := a[x.m()[5]];
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 368)) 

    def test_var_32745237(self):
        _input = """
        class Program {
            func @main():int {
                string := 1;
            }
        }
        """
        expect = "Error on line 4 col 16: string"
        self.assertTrue(TestParser.test(_input, expect, 369)) 

    def test_var_473234723424(self):
        _input = """
        class Program {
            func @main():int {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 370)) 

    def test_var_7423423879785451(self):
        _input = """
        class Program {
            var a: void = 1;

            func @main():int {
                string1 := 1;
            }
        }
        """
        expect = "Error on line 3 col 19: void"
        self.assertTrue(TestParser.test(_input, expect, 371)) 

    def test_var_74234238797854512(self):
        _input = """
        class Program {
            var a: void1 = 1;

            func @main():int {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 372)) 

    def test_var_74234238797854513(self):
        _input = """
        class Program {
            var a: if = 1;

            func @main():int {
                string1 := 1;
            }
        }
        """
        expect = "Error on line 3 col 19: if"
        self.assertTrue(TestParser.test(_input, expect, 373)) 

    def test_var_74234238797854514(self):
        _input = """
        class Program {
            int a: string = 1;

            func @main():int {
                string1 := 1;
            }
        }
        """
        expect = "Error on line 3 col 12: int"
        self.assertTrue(TestParser.test(_input, expect, 374)) 

    def test_main__type7423438717854514(self):
        _input = """
        class Program {
            const a: string = 1;

            func @main(): string {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 375)) 

    def test_main_742348789785454514(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): void {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 376)) 

    def test_type_74234878879851238514(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): int {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 377)) 

    def test_main_742348788798514564238514(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): string {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 378)) 

    def test_type_74234878872329851238514(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): Abc {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 379)) 

    def test_arr_74234878794514(self):
        _input = """
        class Program {
            const a: [n]int = 1;

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = "Error on line 3 col 22: n"
        self.assertTrue(TestParser.test(_input, expect, 380)) 

    def test_arr_742454123894514(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = 1;

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 381)) 

    def test_arr_7424541238942342514(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = [1, 2];

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 382))

    def test_program_541468142344(self):
        _input = """
        class A {}

        class Program {
            var @a: [5]A = 1;

            func X(): Abc {
                string1 := 1;
            }
        }

        @a := 1;
        """
        expect = "Error on line 12 col 8: @a"
        self.assertTrue(TestParser.test(_input, expect, 383))

    def test_program_81789451242344(self):
        _input = """
        class A {}

        class Program {
            var @a: [5]A = 1;

            func @X(): Abc {
                string1 := 1;
            }
        }

        @X();
        """
        expect = "Error on line 12 col 8: @X"
        self.assertTrue(TestParser.test(_input, expect, 384))

    def test_program_127413545842344(self):
        _input = """
        class A {
            const hello: string = "hello";      
        }

        class Program {
            var @a: A = new A();

            func @X(): Abc {
                string1 := A.hello;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 385))

    def test_program_1423428(self):
        _input = """
        class A {
            const hello: string = "hello";  
            func +(a:int, b: int) : int {
                return a + b;
            }
        }

        class Program {
            var @a: A = new A();

            func @X(): Abc {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.+(x, y);
            }
        }
        """
        expect = "Error on line 4 col 17: +"
        self.assertTrue(TestParser.test(_input, expect, 386))

    def test_program_12741212156344(self):
        _input = """
        class A {
            const hello: string = "hello";  
            func plus(a:int, b: int) : int {
                return a + b;
            }
        }

        class Program {
            var @a: A = new A();

            func @X(): Abc {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 387))

    def test_program_1271236344(self):
        _input = """
        class A {
            const hello: string = "hello";  
            func plus(a:int, b: int) : int {
                return a + b;
            }
        }

        class Program {
            var @a: A = new A();

            func @X(): int {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }

            func @main() : int {
                @writeInt("asdfasd");
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 388))

    def test_program_7489123948(self):
        _input = """
        class Program {
            var @a: A = new A();

            func @X(@abc: int): int {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }

            func @main() : int {
                @writeInt("asdfasd");
            }
        }
        """
        expect = "Error on line 5 col 20: @abc"
        self.assertTrue(TestParser.test(_input, expect, 389))

    def test_program_74891934248(self):
        _input = """
        class Program {
            var @a: A = new A();

            func @X(@abc, c,d: int): int {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }

            func @main() : int {
                @writeInt("asdfasd");
            }
        }
        """
        expect = "Error on line 5 col 20: @abc"
        self.assertTrue(TestParser.test(_input, expect, 390))

    def test_program_74546524248(self):
        _input = """
        class Program {
            var @a: A = new A();

            func @X(@abc, c,d: int): int {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }

            func @main() : int {
                X.a() :== @toString(1 + 2 * 3 \\ 5);
            }
        }
        """
        expect = "Error on line 5 col 20: @abc"
        self.assertTrue(TestParser.test(_input, expect, 391))

    def test_program_7234234248(self):
        _input = """
        class Program {
            var @a: A = new A();

            func @X(abc, c,d: int): int {
                string1 := A.hello;
                var x :int = 1;
                var y : int = 2;
                return A.plus(x, y);
            }

            func @main() : int {
                X.a() := @toString(1 + 2 * 3 \\ 5);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 392))

    def test_program_6347562374(self):
        _input = """
        class Program {
            def abd {
                string := "hello";
            }
        }
        """
        expect = "Error on line 3 col 12: def"
        self.assertTrue(TestParser.test(_input, expect, 393))

    def test_program_634512874(self):
        _input = """
        class Program {
            func double(lst: int): int {
                if @len(lst) == 0 {
                    return [];
                }
                var i:int = lst[0];
                return ([2*i] + self.double(lst[12]));
            }
        }
        """
        expect = "Error on line 5 col 28: ]"
        self.assertTrue(TestParser.test(_input, expect, 394))

    def test_program_473829428(self):
        _input = """
        class Program {
            func doubFunc(a:int):int {
                return 2*a;
            }
            
            func double1(lst: int): int {
                return @list(@map(doubFunc, lst));
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 395))

    def test_program_8347129348(self):
        _input = """
        class Program {
            func @main(a:int):int {
                for i > 0; i < 10; i < 1 {
                    io.@writeInt(i);
                }
            }
        }
        """
        expect = "Error on line 4 col 22: >"
        self.assertTrue(TestParser.test(_input, expect, 396))

    def test_program_4738191238(self):
        _input = """
        class Program {
            func @main():int {
                for i > 0; i < 10; i < 1 {
                    io.@writeInt(i);
                }
            }
        }
        """
        expect = "Error on line 4 col 22: >"
        self.assertTrue(TestParser.test(_input, expect, 397))

    def test_program_412983491238(self):
        _input = """
        class Program {
            func @main():int {
                for i := 0; i < 10; i < 1 {
                    io.@writeInt(i);
                }
            }
        }
        """
        expect = "Error on line 4 col 38: <"
        self.assertTrue(TestParser.test(_input, expect, 398))

    def test_program_634384574(self):
        _input = """
        class Program {
            func double(lst: int): int {
                if @len(lst) == 1 {
                    return lst;
                }
                var i:int = lst[0];
                return ([2*i] + self.double(lst[12]));
            }
        }
        """
        expect = "Error on line 8 col 26: *"
        self.assertTrue(TestParser.test(_input, expect, 399))

    def test_program_62839474574(self):
        _input = """
        class Program {
            func double(lst: int): int {
                if @len(lst) == 1 {
                    return lst;
                }
                var i:int = lst[0] * 2;
                return (@list(i) + self.double(lst[12]));
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 400))

    def test_program_384791471(self):
        _input = """
        class Program{
            func railfence(ciphertext: string, key: integer):string {
            if key <= 1
                {return ciphertext;}
            
            var matrix: [15] string;
            for i:=0 ; i<15 ; i:=i+1 {
                var matrix_a: [15]string;
            }
            /* 
                15 for each row
                maxium 15 rows
            */

            var dir: bool = true;
            // true for down, false for up

            var row, col: int= 0, 0;

            for i := 0; i < @length(ciphertext); i:=i + 1 {
                if row == 0 {dir := true;}
                if row == key - 1 {dir := false;}
                rail[row] := null;
                
                col := col + 1;
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }

            var index: int = 0;
            for i := 0; i < key; i:=i + 1 {
                for j := 0; j < @length(ciphertext);j:= j + 1{
                    if matrix[i] == null && (index < @length(ciphertext)) {
                        matrix[i] := ciphertext[index];
                        index := index + 1;
                    }}
            
            row := 0; col := 0;
            var result: string;
            for i:=0; i< @length(ciphertext);i:= i + 1 
            {
                // check the direction of flow
                if row == 0
                    {dir := true;}
                if row == key - 1
                    {dir := false;}
 
                // place the marker
                if rail[row] != "*"
                    {result := result.rail[col];}
                col := col + 1;
 
                // find the next row using direction flag
                if dir
                    {row := row + 1;}
                else {row := row - 1;}
            }
            return result;
        }
        }}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(_input, expect, 401))

    def test_program_384791(self):
        _input = """
        class Program {
            var a: [2]int = [2,"why not"];
            func @main():void{
            a[1],a[2] := [1,2] ,[2,3];
        }}
        """
        expect = "Error on line 5 col 16: ,"
        self.assertTrue(TestParser.test(_input, expect, 402))