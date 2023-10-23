import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,500))

    def test_class_with_one_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,501))
    
    def test_class_with_two_decl_program(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,502))
   
    def test_class_with_long_decl_program(self):
        input = """class main {var x, y, z: int = 1, 2, 3;}"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("x"),IntType(),IntLiteral(1))),
             AttributeDecl(VarDecl(Id("y"),IntType(),IntLiteral(2))),
             AttributeDecl(VarDecl(Id("z"),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,503))

    def test_class_with_both_var_and_const_decl_program(self):
        input = """class object<-main{ const x, y, z: int = 1, 2, 3;
                    var a, b: float;}"""
        expect = str(Program([ClassDecl(Id("main"),
                    [AttributeDecl(ConstDecl(Id("x"),IntType(),IntLiteral(1))),
                     AttributeDecl(ConstDecl(Id("y"),IntType(),IntLiteral(2))),
                     AttributeDecl(ConstDecl(Id("z"),IntType(),IntLiteral(3))),
                     AttributeDecl(VarDecl(Id("a"),FloatType())),
                     AttributeDecl(VarDecl(Id("b"),FloatType()))], 
                    Id("object"))]))
        self.assertTrue(TestAST.test(input,expect,504))

    def test_class_with_method_decl_program(self):
        input = """class main{ func a(): void {}}"""
        expect = str(Program(
                [ClassDecl(Id("main"),
                    [MethodDecl(Id("a"),[],VoidType(),Block([]))]
                )]))
        self.assertTrue(TestAST.test(input,expect,505))
        
    def test_class_with_method_decl_main_program(self):
        input = """class main{
        func foo  (a: int, b: float):void {}

        func @main():void{
            io.printInt(4);
        }}"""
        expect = str(Program([ClassDecl(Id("main"),
                    [MethodDecl(
                        Id("foo"),
                        [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],
                        VoidType(),Block([])),
                    MethodDecl(
                        Id("@main"),
                        [],
                        VoidType(),Block(
                            [CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,506))

    def test_decl_class_empty(self):
        _input = """class A{}"""
        expect = str(Program([ClassDecl(Id("A"),[])]))
        self.assertTrue(TestAST.test(_input, expect, 507))

    def test_declare_class_with_var_decl(self):
        _input = """class A{var delta: int = 3;}"""
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(VarDecl(Id("delta"),IntType(),IntLiteral(3)))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 508))

    def test_decl_class_inherit(self):
        _input = """class A <- B{var delta: int = 3;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("delta"),IntType(),IntLiteral(3)))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 509))

    def test_decl_var(self):
        _input = """class A <- B{var width: int;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("width"),IntType()))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 510))

    def test_func(self):
        _input = """class A <- B{func A(): int {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 511))

    def test_func_params(self):
        _input = """class A <- B{func A(a: int, b: int): int {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType())
                ],IntType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 512))
    
    def test_static_func(self):
        _input = """class Program {func @main(): void {}}"""
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 513))

    def test_class_static_func(self):
        _input = """
        class Program {
            func @main():void {
                var r, s: int;
                r := 2.0;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    VarDecl(Id("r"),IntType()),
                    VarDecl(Id("s"),IntType()),
                    Assign(Id("r"),FloatLiteral(2.0))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 514))

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
        expect = str(Program([
            ClassDecl(Id("Shape"),[
                AttributeDecl(VarDecl(Id("@numOfShape"),IntType(),IntLiteral(0))),
                AttributeDecl(ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("length"),IntType())),
                AttributeDecl(VarDecl(Id("width"),IntType())),
                MethodDecl(Id("@getNumOfShape"),[],IntType(),Block([
                    Return(FieldAccess(None, Id("@numOfShape")))
                ]))
            ]),
            ClassDecl(Id("Retangle"),[
                MethodDecl(Id("getArea"),[],IntType(),Block([
                    Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))
                ]))
            ],Id("Shape")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    CallStmt(None, Id("@writeInt"),[
                        FieldAccess(None, Id("@numOfShape"))
                    ])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 515))

    def test_cmt_block(self):
        _input = """class A <- B{
            var a :int = 5;//this is a line comment
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(5)))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 516))

    def test_arr_ele(self):
        _input = """class A <- B{var x :int = A[1];}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("x"),IntType(),ArrayCell(Id("A"),IntLiteral(1))))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 517))

    def test_if_stmt2(self):
        _input = """class A <- B{
            func A(): int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    If(
                        BinaryOp("==",Id("n"),IntLiteral(0)),
                        Block([Return(IntLiteral(1))]),
                        None,
                        Block([Return(BinaryOp(
                            "*",
                            Id("n"),
                            CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])
                        ))])
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 518))

    def test_method_invocation(self):
        _input = """class A <- B{func A(): int {Shape.@getNumOfShape();}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    CallStmt(None,Id("@getNumOfShape"),[])
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 519))

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
        expect = str(Program([
            ClassDecl(Id("Shape"),[
                AttributeDecl(VarDecl(Id("@numOfShape"),IntType(),IntLiteral(0))),
                AttributeDecl(ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("length"),IntType())),
                AttributeDecl(VarDecl(Id("width"),IntType())),
                MethodDecl(Id("@getNumOfShape"),[],IntType(),Block([
                    Return(FieldAccess(None, Id("@numOfShape")))
                ]))
            ]),
            ClassDecl(Id("Retangle"),[
                MethodDecl(Id("getArea"),[],IntType(),Block([
                    Return(BinaryOp(
                        "*",
                        FieldAccess(SelfLiteral(),Id("length")),
                        FieldAccess(SelfLiteral(),Id("width"))
                    ))
                ]))
            ],Id("Shape")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    CallStmt(None,Id("@writeInt"),[
                        FieldAccess(None, Id("@numOfShape"))
                    ])
                ]))
            ]),
        ]))
        self.assertTrue(TestAST.test(_input, expect, 520))

    def test_params_multiple(self):
        _input = """class A <- B{func functi(a,b,c: int, d: bool): void {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("functi"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),IntType()),
                    VarDecl(Id("d"),BoolType()),
                ],VoidType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 521))

    def test_arr_ele1(self):
        _input = """class A <- B{func X(): int {a[3+x.foo(2)] := a[b[2]] +3;}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("X"),[],IntType(),Block([
                    Assign(
                        ArrayCell(
                            Id("a"),
                            BinaryOp("+",
                                IntLiteral(3),
                                CallExpr(Id("x"),Id("foo"),[IntLiteral(2)])
                            )
                        ),
                        BinaryOp(
                            "+",
                            ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),
                            IntLiteral(3)
                        )
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 522))

    def test_arr_ele2(self):
        _input = """class A <- B{func A(): int {x.b[2] := x.m()[3];}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    Assign(
                        ArrayCell(FieldAccess(Id("x"),Id("b")),IntLiteral(2)),
                        ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 523))

    def test_attr_decl1(self):
        _input = """class A <- B{const My1stCons, My2ndCons: int = 1 + 5, "abc";
        var @x, @y : int = 0, false;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(ConstDecl(Id("My1stCons"),IntType(),BinaryOp(
                    "+",IntLiteral(1),IntLiteral(5)
                ))),
                AttributeDecl(ConstDecl(Id("My2ndCons"),IntType(),StringLiteral("abc"))),
                AttributeDecl(VarDecl(Id("@x"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("@y"),IntType(),BooleanLiteral(False))),
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 524))

    def test_class_with_self1(self):
        _input = """
        class Program {
            var a: int = 1;    
        
            func constructor() {
                x := self.a;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),
                MethodDecl(Id("constructor"),[],VoidType(),Block([
                    Assign(Id("x"),FieldAccess(SelfLiteral(),Id("a")))
                ]))
            ])
        ]))   
        self.assertTrue(TestAST.test(_input, expect, 525))

    def test_assign_stmt1(self):
        _input = """class A <- B{
            func X(): void {
                self.aPI := null;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("X"),[],VoidType(),Block([
                    Assign(FieldAccess(SelfLiteral(),Id("aPI")),NullLiteral()),
                    Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),
                    Assign(ArrayCell(Id("l"),IntLiteral(3)),BinaryOp("*",Id("value"),IntLiteral(2)))
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 526))

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
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("a"),IntType())),
                AttributeDecl(VarDecl(Id("b"),IntType())),
                AttributeDecl(VarDecl(Id("c"),IntType())),
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    For(
                        Assign(Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            CallStmt(None,Id("@writeInt"),[Id("i")])
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 527))

    def test_continue_in_for(self):
        _input = """
        class A {
            func @main(a:int, b:int, c:bool): int {
                for i := a; i < b; i := i + 1 {
                    if @isChecked(a) == c {
                        continue;
                    }
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                MethodDecl(Id("@main"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),BoolType()),
                ],IntType(),Block([
                    For(
                        Assign(Id("i"),Id("a")),
                        BinaryOp("<",Id("i"),Id("b")),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp("==",CallExpr(None,Id("@isChecked"),[Id("a")]),Id("c")),
                                Block([
                                    Continue()
                                ])
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 528))

    def test_continue_in_for_with_cmt_and_break(self):
        _input = """
        class A {
            func @main(a:int, b:int, c:bool): int {
                for i := a; i < b; i := i + 1 {
                    if @isChecked(a) == c {
                        continue;
                    }
                    /* add 
                    here */
                    io.@writeStr("Press 1 to exit: ");
                    if input==1 {
                        break; // terminate loop
                    }
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                MethodDecl(Id("@main"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),BoolType()),
                ],IntType(),Block([
                    For(
                        Assign(Id("i"),Id("a")),
                        BinaryOp("<",Id("i"),Id("b")),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp("==",CallExpr(None,Id("@isChecked"),[Id("a")]),Id("c")),
                                Block([
                                    Continue()
                                ])
                            ),
                            CallStmt(None,Id("@writeStr"),[StringLiteral("Press 1 to exit: ")]),
                            If(
                                BinaryOp("==",Id("input"),IntLiteral(1)),
                                Block([
                                    Break()
                                ])
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 529))

    def test_program_with_logic_754829(self):
        _input = """
        class Program {
            func @main():int {
                io.@writeBool(!(10 == 5)); // boolean
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    CallStmt(None,Id("@writeBool"),[
                        UnaryOp("!",BinaryOp("==",IntLiteral(10),IntLiteral(5)))
                    ])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 530))

    def test_program_with_logic_78011902343819(self):
        _input = """
        class Program {
            func @main():int {
                str := "Hello " ^ "World!";
                io.@writeStr(str);

                var escapeStr : string = "First Line"; 
                io.@writeStr(escapeStr);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(Id("str"),BinaryOp("^",StringLiteral("Hello "),StringLiteral("World!"))),
                    CallStmt(None,Id("@writeStr"),[Id("str")]),
                    VarDecl(Id("escapeStr"),StringType(),StringLiteral("First Line")),
                    CallStmt(None,Id("@writeStr"),[Id("escapeStr")])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 531))

    def test_obj_cre_798342504(self):
        _input = """
        class Program {
            func @main():int {
                var myObj : NewObj = new NewObj();
                myObj.a := null;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("myObj"),ClassType(Id("NewObj")),NewExpr(Id("NewObj"),[])),
                    Assign(FieldAccess(Id("myObj"),Id("a")),NullLiteral())
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 532))

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
        expect = str(Program([
            ClassDecl(Id("Animal"),[
                AttributeDecl(VarDecl(Id("sound"),StringType(),StringLiteral("sound")))
            ]),
            ClassDecl(Id("Dog"),[
                AttributeDecl(VarDecl(Id("sound"),StringType(),StringLiteral("Gau")))
            ],Id("Animal")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("hwng"),ClassType(Id("Animal")),NewExpr(Id("Dog"),[])),
                    CallStmt(None,Id("@writeStr"),[FieldAccess(Id("hwng"),Id("sound"))])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 533))

    def test_exp_509483753957938295(self):
        _input = """
        class Program {
            func @main():int {
                @ip.num[0] := -(123 + 456 / 2);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        ArrayCell(FieldAccess(FieldAccess(None,Id("@ip")),Id("num")),IntLiteral(0)),
                        UnaryOp("-",BinaryOp("+",IntLiteral(123),BinaryOp("/",IntLiteral(456),IntLiteral(2))))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 534))

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
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("s"),ArrayType(10,IntType())),
                    VarDecl(Id("a"),ArrayType(20,IntType()),CallExpr(
                        None,
                        Id("@changeText"),
                        [
                            ArrayCell(Id("s"),IntLiteral(0)),
                            ArrayCell(Id("a"),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),
                            BinaryOp("^",StringLiteral("a"),StringLiteral("b"))
                        ]
                    )),
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 535))

    def test_exp_239485098700202(self):
        _input = """
        class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@text")),
                        UnaryOp("!",BinaryOp("&&",Id("a"),Id("b")))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 536))

    def test_exp_9823475928(self):
        _input = """
        class Program {
            func @main():int {
                @isSth := !a.x[1] && b [2];
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@isSth")),
                        BinaryOp("&&",UnaryOp("!",ArrayCell(FieldAccess(Id("a"),Id("x")),IntLiteral(1))),ArrayCell(Id("b"),IntLiteral(2)))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 537))

    def test_exp_75849320(self):
        _input = """
        class Program {
            func @main():int {
                @text := a + b * c / d;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(FieldAccess(None,Id("@text")),BinaryOp("+",Id("a"),BinaryOp("/",BinaryOp("*",Id("b"),Id("c")),Id("d"))))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 538))

    def test_exp_47923842(self):
        _input = """
        class Program {
            func @main():int {
                @text := a[x.m()[5]];
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@text")),
                        ArrayCell(Id("a"),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(5)))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 539))

    def test_type_74234878872329851238514(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): Abc {
                string1 := 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(Id("a"),StringType(),IntLiteral(1))),
                MethodDecl(Id("main"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 540))

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
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(Id("a"),ArrayType(5,ClassType(Id("A"))),IntLiteral(1))),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 541))

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
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(
                    Id("a"),
                    ArrayType(5,ClassType(Id("A"))),
                    ArrayLiteral([IntLiteral(1),IntLiteral(2)])
                )),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 542))

    def test_arr_74245412382423914(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = [1, 2];

            func X(): Abc {
                string1 := 1;
                return;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(
                    Id("a"),
                    ArrayType(5,ClassType(Id("A"))),
                    ArrayLiteral([IntLiteral(1),IntLiteral(2)])
                )),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1)),
                    Return(None)
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 543))

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
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(ConstDecl(Id("hello"),StringType(),StringLiteral("hello")))
            ]),
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("@a"),ClassType(Id("A")),NewExpr(Id("A"),[]))),
                MethodDecl(Id("@X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),FieldAccess(Id("A"),Id("hello")))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 544))

    def test_arr_ele_28479(self):
        _input = """
        class B <- A {
            var lst : [5]int = [1, 2, 3];

            func lst(a:int):void {
                var x:int = self.lst[0];
                io.@writeInt(x);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(VarDecl(Id("lst"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),
                MethodDecl(Id("lst"),[VarDecl(Id("a"),IntType())],VoidType(),Block([
                    VarDecl(Id("x"),IntType(),ArrayCell(FieldAccess(SelfLiteral(),Id("lst")),IntLiteral(0))),
                    CallStmt(None,Id("@writeInt"),[Id("x")])
                ]))
            ],Id("B"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 545))

    def test_array_lit(self):
        _input = """
        class A {
            var lst: [5]int = [1,2,3];
            func constructor() {
                io.@writeInt(self.lst);
            }
        }
        class Program {
            func @main():int {
                var obj : A = new A();
                io.@writeInt(obj.lst);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(VarDecl(Id("lst"),ArrayType(5, IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),
                MethodDecl(Id("constructor"),[],VoidType(),Block([
                    CallStmt(None,Id("@writeInt"),[FieldAccess(SelfLiteral(),Id("lst"))])
                ]))
            ]),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("obj"),ClassType(Id("A")),NewExpr(Id("A"),[])),
                    CallStmt(None,Id("@writeInt"),[FieldAccess(Id("obj"),Id("lst"))])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 546))

    def test_fun_1(self):
        _input = """class A{}"""
        expect = str(Program([
            ClassDecl(Id("A"),[])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 547))

    def test_fun_2(self):
        _input = """class A <- B{var a:int=1+2;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("a"),IntType(),BinaryOp("+",IntLiteral(1),IntLiteral(2))))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 548))

    def test_fun_3(self):
        _input = """class A <- B{func A(a: int, b: int): int {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                ],IntType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 549))

    def test_fun_4(self):
        _input = """class Program {func @main(): void {}}"""
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 550))

    def test_attr_const_decl_none(self):
        _input = """
        class A {
            const A:int;
            func B():void {}
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(ConstDecl(Id("A"),IntType(),None)),
                MethodDecl(Id("B"),[],VoidType(),Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 551))

    def test_return_none(self):
        _input = """
        class A {
            const C:int;
            func B():void {
                return;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(ConstDecl(Id("C"),IntType(),None)),
                MethodDecl(Id("B"),[],VoidType(),Block([
                    Return(None)
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 552))

    def test_const_decl_in_func(self):
        _input = """
        class A{
            func B(): void {
                const C: int;
                return;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                MethodDecl(Id("B"),[],VoidType(),Block([
                    ConstDecl(Id("C"),IntType(),None),
                    Return(None)
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 553))

    def test_simple_program_cp(self):
        """Simple program: class main {} """
        input = """class main {}"""
        expect = str(Program([ClassDecl(Id("main"),[])]))
        self.assertTrue(TestAST.test(input,expect,554))

    def test_class_with_one_decl_program_cp(self):
        """More complex program"""
        input = """class main {
            var a:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),[AttributeDecl(VarDecl(Id("a"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,555))
    
    def test_class_with_two_decl_program_cp(self):
        """More complex program"""
        input = """class main {
            var a:int;
            var b:int;
        }"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("a"),IntType())),
             AttributeDecl(VarDecl(Id("b"),IntType()))])]))
        self.assertTrue(TestAST.test(input,expect,556))
   
    def test_class_with_long_decl_program_cp(self):
        input = """class main {var x, y, z: int = 1, 2, 3;}"""
        expect = str(Program([ClassDecl(Id("main"),
            [AttributeDecl(VarDecl(Id("x"),IntType(),IntLiteral(1))),
             AttributeDecl(VarDecl(Id("y"),IntType(),IntLiteral(2))),
             AttributeDecl(VarDecl(Id("z"),IntType(),IntLiteral(3)))])]))
        self.assertTrue(TestAST.test(input,expect,557))

    def test_class_with_both_var_and_const_decl_program_cp(self):
        input = """class object<-main{ const x, y, z: int = 1, 2, 3;
                    var a, b: float;}"""
        expect = str(Program([ClassDecl(Id("main"),
                    [AttributeDecl(ConstDecl(Id("x"),IntType(),IntLiteral(1))),
                     AttributeDecl(ConstDecl(Id("y"),IntType(),IntLiteral(2))),
                     AttributeDecl(ConstDecl(Id("z"),IntType(),IntLiteral(3))),
                     AttributeDecl(VarDecl(Id("a"),FloatType())),
                     AttributeDecl(VarDecl(Id("b"),FloatType()))], 
                    Id("object"))]))
        self.assertTrue(TestAST.test(input,expect,558))

    def test_class_with_method_decl_program_cp(self):
        input = """class main{ func a(): void {}}"""
        expect = str(Program(
                [ClassDecl(Id("main"),
                    [MethodDecl(Id("a"),[],VoidType(),Block([]))]
                )]))
        self.assertTrue(TestAST.test(input,expect,559))
        
    def test_class_with_method_decl_main_program_cp(self):
        input = """class main{
        func foo  (a: int, b: float):void {}

        func @main():void{
            io.printInt(4);
        }}"""
        expect = str(Program([ClassDecl(Id("main"),
                    [MethodDecl(
                        Id("foo"),
                        [VarDecl(Id("a"),IntType()),VarDecl(Id("b"),FloatType())],
                        VoidType(),Block([])),
                    MethodDecl(
                        Id("@main"),
                        [],
                        VoidType(),Block(
                            [CallStmt(Id("io"),Id("printInt"),[IntLiteral(4)])]))])]))
        self.assertTrue(TestAST.test(input,expect,560))

    def test_decl_class_empty_cp(self):
        _input = """class A{}"""
        expect = str(Program([ClassDecl(Id("A"),[])]))
        self.assertTrue(TestAST.test(_input, expect, 561))

    def test_declare_class_with_var_decl_cp(self):
        _input = """class A{var delta: int = 3;}"""
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(VarDecl(Id("delta"),IntType(),IntLiteral(3)))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 562))

    def test_decl_class_inherit_cp(self):
        _input = """class A <- B{var delta: int = 3;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("delta"),IntType(),IntLiteral(3)))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 563))

    def test_decl_var_cp(self):
        _input = """class A <- B{var width: int;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("width"),IntType()))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 564))

    def test_func_cp(self):
        _input = """class A <- B{func A(): int {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 565))

    def test_func_params_cp(self):
        _input = """class A <- B{func A(a: int, b: int): int {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType())
                ],IntType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 566))
    
    def test_static_func_cp(self):
        _input = """class Program {func @main(): void {}}"""
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 567))

    def test_class_static_func_cp(self):
        _input = """
        class Program {
            func @main():void {
                var r, s: int;
                r := 2.0;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    VarDecl(Id("r"),IntType()),
                    VarDecl(Id("s"),IntType()),
                    Assign(Id("r"),FloatLiteral(2.0))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 568))

    def test_long_prog1_cp(self):
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
        expect = str(Program([
            ClassDecl(Id("Shape"),[
                AttributeDecl(VarDecl(Id("@numOfShape"),IntType(),IntLiteral(0))),
                AttributeDecl(ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("length"),IntType())),
                AttributeDecl(VarDecl(Id("width"),IntType())),
                MethodDecl(Id("@getNumOfShape"),[],IntType(),Block([
                    Return(FieldAccess(None, Id("@numOfShape")))
                ]))
            ]),
            ClassDecl(Id("Retangle"),[
                MethodDecl(Id("getArea"),[],IntType(),Block([
                    Return(BinaryOp("*",FieldAccess(SelfLiteral(),Id("length")),FieldAccess(SelfLiteral(),Id("width"))))
                ]))
            ],Id("Shape")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    CallStmt(None, Id("@writeInt"),[
                        FieldAccess(None, Id("@numOfShape"))
                    ])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 569))

    def test_cmt_block_cp(self):
        _input = """class A <- B{
            var a :int = 5;//this is a line comment
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(5)))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 570))

    def test_arr_ele_cp(self):
        _input = """class A <- B{var x :int = A[1];}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(VarDecl(Id("x"),IntType(),ArrayCell(Id("A"),IntLiteral(1))))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 571))

    def test_if_stmt2_cp(self):
        _input = """class A <- B{
            func A(): int {
                if n == 0 {return 1;}
                else {return n * @fact(n - 1);}
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    If(
                        BinaryOp("==",Id("n"),IntLiteral(0)),
                        Block([Return(IntLiteral(1))]),
                        None,
                        Block([Return(BinaryOp(
                            "*",
                            Id("n"),
                            CallExpr(None,Id("@fact"),[BinaryOp("-",Id("n"),IntLiteral(1))])
                        ))])
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 572))

    def test_method_invocation_cp(self):
        _input = """class A <- B{func A(): int {Shape.@getNumOfShape();}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    CallStmt(None,Id("@getNumOfShape"),[])
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 573))

    def test_long_prog2_cp(self):
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
        expect = str(Program([
            ClassDecl(Id("Shape"),[
                AttributeDecl(VarDecl(Id("@numOfShape"),IntType(),IntLiteral(0))),
                AttributeDecl(ConstDecl(Id("immutableAttribute"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("length"),IntType())),
                AttributeDecl(VarDecl(Id("width"),IntType())),
                MethodDecl(Id("@getNumOfShape"),[],IntType(),Block([
                    Return(FieldAccess(None, Id("@numOfShape")))
                ]))
            ]),
            ClassDecl(Id("Retangle"),[
                MethodDecl(Id("getArea"),[],IntType(),Block([
                    Return(BinaryOp(
                        "*",
                        FieldAccess(SelfLiteral(),Id("length")),
                        FieldAccess(SelfLiteral(),Id("width"))
                    ))
                ]))
            ],Id("Shape")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    CallStmt(None,Id("@writeInt"),[
                        FieldAccess(None, Id("@numOfShape"))
                    ])
                ]))
            ]),
        ]))
        self.assertTrue(TestAST.test(_input, expect, 574))

    def test_params_multiple_cp(self):
        _input = """class A <- B{func functi(a,b,c: int, d: bool): void {}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("functi"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),IntType()),
                    VarDecl(Id("d"),BoolType()),
                ],VoidType(),Block([]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 575))

    def test_arr_ele1_cp(self):
        _input = """class A <- B{func X(): int {a[3+x.foo(2)] := a[b[2]] +3;}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("X"),[],IntType(),Block([
                    Assign(
                        ArrayCell(
                            Id("a"),
                            BinaryOp("+",
                                IntLiteral(3),
                                CallExpr(Id("x"),Id("foo"),[IntLiteral(2)])
                            )
                        ),
                        BinaryOp(
                            "+",
                            ArrayCell(Id("a"),ArrayCell(Id("b"),IntLiteral(2))),
                            IntLiteral(3)
                        )
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 576))

    def test_arr_ele2_cp(self):
        _input = """class A <- B{func A(): int {x.b[2] := x.m()[3];}}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("A"),[],IntType(),Block([
                    Assign(
                        ArrayCell(FieldAccess(Id("x"),Id("b")),IntLiteral(2)),
                        ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(3))
                    )
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 577))

    def test_attr_decl1_cp(self):
        _input = """class A <- B{const My1stCons, My2ndCons: int = 1 + 5, "abc";
        var @x, @y : int = 0, false;}"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                AttributeDecl(ConstDecl(Id("My1stCons"),IntType(),BinaryOp(
                    "+",IntLiteral(1),IntLiteral(5)
                ))),
                AttributeDecl(ConstDecl(Id("My2ndCons"),IntType(),StringLiteral("abc"))),
                AttributeDecl(VarDecl(Id("@x"),IntType(),IntLiteral(0))),
                AttributeDecl(VarDecl(Id("@y"),IntType(),BooleanLiteral(False))),
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 578))

    def test_class_with_self1_cp(self):
        _input = """
        class Program {
            var a: int = 1;    
        
            func constructor() {
                x := self.a;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("a"),IntType(),IntLiteral(1))),
                MethodDecl(Id("constructor"),[],VoidType(),Block([
                    Assign(Id("x"),FieldAccess(SelfLiteral(),Id("a")))
                ]))
            ])
        ]))   
        self.assertTrue(TestAST.test(_input, expect, 579))

    def test_assign_stmt1_cp(self):
        _input = """class A <- B{
            func X(): void {
                self.aPI := null;
                value := x.foo(5);
                l[3] := value * 2;
            }
        }"""
        expect = str(Program([
            ClassDecl(Id("B"),[
                MethodDecl(Id("X"),[],VoidType(),Block([
                    Assign(FieldAccess(SelfLiteral(),Id("aPI")),NullLiteral()),
                    Assign(Id("value"),CallExpr(Id("x"),Id("foo"),[IntLiteral(5)])),
                    Assign(ArrayCell(Id("l"),IntLiteral(3)),BinaryOp("*",Id("value"),IntLiteral(2)))
                ]))
            ],Id("A"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 580))

    def test_program_with_for_287249582_cp(self):
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
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("a"),IntType())),
                AttributeDecl(VarDecl(Id("b"),IntType())),
                AttributeDecl(VarDecl(Id("c"),IntType())),
                MethodDecl(Id("@main"),[],VoidType(),Block([
                    For(
                        Assign(Id("i"),IntLiteral(0)),
                        BinaryOp("<",Id("i"),IntLiteral(10)),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            CallStmt(None,Id("@writeInt"),[Id("i")])
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 581))

    def test_continue_in_for_cp(self):
        _input = """
        class A {
            func @main(a:int, b:int, c:bool): int {
                for i := a; i < b; i := i + 1 {
                    if @isChecked(a) == c {
                        continue;
                    }
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                MethodDecl(Id("@main"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),BoolType()),
                ],IntType(),Block([
                    For(
                        Assign(Id("i"),Id("a")),
                        BinaryOp("<",Id("i"),Id("b")),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp("==",CallExpr(None,Id("@isChecked"),[Id("a")]),Id("c")),
                                Block([
                                    Continue()
                                ])
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 582))

    def test_continue_in_for_with_cmt_and_break_cp(self):
        _input = """
        class A {
            func @main(a:int, b:int, c:bool): int {
                for i := a; i < b; i := i + 1 {
                    if @isChecked(a) == c {
                        continue;
                    }
                    /* add 
                    here */
                    io.@writeStr("Press 1 to exit: ");
                    if input==1 {
                        break; // terminate loop
                    }
                }
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                MethodDecl(Id("@main"),[
                    VarDecl(Id("a"),IntType()),
                    VarDecl(Id("b"),IntType()),
                    VarDecl(Id("c"),BoolType()),
                ],IntType(),Block([
                    For(
                        Assign(Id("i"),Id("a")),
                        BinaryOp("<",Id("i"),Id("b")),
                        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1))),
                        Block([
                            If(
                                BinaryOp("==",CallExpr(None,Id("@isChecked"),[Id("a")]),Id("c")),
                                Block([
                                    Continue()
                                ])
                            ),
                            CallStmt(None,Id("@writeStr"),[StringLiteral("Press 1 to exit: ")]),
                            If(
                                BinaryOp("==",Id("input"),IntLiteral(1)),
                                Block([
                                    Break()
                                ])
                            )
                        ])
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 583))

    def test_program_with_logic_754829_cp(self):
        _input = """
        class Program {
            func @main():int {
                io.@writeBool(!(10 == 5)); // boolean
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    CallStmt(None,Id("@writeBool"),[
                        UnaryOp("!",BinaryOp("==",IntLiteral(10),IntLiteral(5)))
                    ])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 584))

    def test_program_with_logic_78011902343819_cp(self):
        _input = """
        class Program {
            func @main():int {
                str := "Hello " ^ "World!";
                io.@writeStr(str);

                var escapeStr : string = "First Line"; 
                io.@writeStr(escapeStr);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(Id("str"),BinaryOp("^",StringLiteral("Hello "),StringLiteral("World!"))),
                    CallStmt(None,Id("@writeStr"),[Id("str")]),
                    VarDecl(Id("escapeStr"),StringType(),StringLiteral("First Line")),
                    CallStmt(None,Id("@writeStr"),[Id("escapeStr")])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 585))

    def test_obj_cre_798342504_cp(self):
        _input = """
        class Program {
            func @main():int {
                var myObj : NewObj = new NewObj();
                myObj.a := null;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("myObj"),ClassType(Id("NewObj")),NewExpr(Id("NewObj"),[])),
                    Assign(FieldAccess(Id("myObj"),Id("a")),NullLiteral())
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 586))

    def test_obj_cre_192843232345435457_cp(self):
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
        expect = str(Program([
            ClassDecl(Id("Animal"),[
                AttributeDecl(VarDecl(Id("sound"),StringType(),StringLiteral("sound")))
            ]),
            ClassDecl(Id("Dog"),[
                AttributeDecl(VarDecl(Id("sound"),StringType(),StringLiteral("Gau")))
            ],Id("Animal")),
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("hwng"),ClassType(Id("Animal")),NewExpr(Id("Dog"),[])),
                    CallStmt(None,Id("@writeStr"),[FieldAccess(Id("hwng"),Id("sound"))])
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 587))

    def test_exp_509483753957938295_cp(self):
        _input = """
        class Program {
            func @main():int {
                @ip.num[0] := -(123 + 456 / 2);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        ArrayCell(FieldAccess(FieldAccess(None,Id("@ip")),Id("num")),IntLiteral(0)),
                        UnaryOp("-",BinaryOp("+",IntLiteral(123),BinaryOp("/",IntLiteral(456),IntLiteral(2))))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 588))

    def test_exp_928347598_cp(self):
        _input = """
        class Program {
            func @main():int {
                var s: [10]int;
                var a: [20]int = 
                @changeText(s[0], a[a[1+2]], "a" ^ "b");
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    VarDecl(Id("s"),ArrayType(10,IntType())),
                    VarDecl(Id("a"),ArrayType(20,IntType()),CallExpr(
                        None,
                        Id("@changeText"),
                        [
                            ArrayCell(Id("s"),IntLiteral(0)),
                            ArrayCell(Id("a"),ArrayCell(Id("a"),BinaryOp("+",IntLiteral(1),IntLiteral(2)))),
                            BinaryOp("^",StringLiteral("a"),StringLiteral("b"))
                        ]
                    )),
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 589))

    def test_exp_239485098700202_cp(self):
        _input = """
        class Program {
            func @main():int {
                @text := !(a && b);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@text")),
                        UnaryOp("!",BinaryOp("&&",Id("a"),Id("b")))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 590))

    def test_exp_9823475928_cp(self):
        _input = """
        class Program {
            func @main():int {
                @isSth := !a.x[1] && b [2];
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@isSth")),
                        BinaryOp("&&",UnaryOp("!",ArrayCell(FieldAccess(Id("a"),Id("x")),IntLiteral(1))),ArrayCell(Id("b"),IntLiteral(2)))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 591))

    def test_exp_75849320_cp(self):
        _input = """
        class Program {
            func @main():int {
                @text := a + b * c / d;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(FieldAccess(None,Id("@text")),BinaryOp("+",Id("a"),BinaryOp("/",BinaryOp("*",Id("b"),Id("c")),Id("d"))))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 592))

    def test_exp_47923842_cp(self):
        _input = """
        class Program {
            func @main():int {
                @text := a[x.m()[5]];
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                MethodDecl(Id("@main"),[],IntType(),Block([
                    Assign(
                        FieldAccess(None,Id("@text")),
                        ArrayCell(Id("a"),ArrayCell(CallExpr(Id("x"),Id("m"),[]),IntLiteral(5)))
                    )
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 593))

    def test_type_74234878872329851238514_cp(self):
        _input = """
        class Program {
            const a: string = 1;

            func main(): Abc {
                string1 := 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(Id("a"),StringType(),IntLiteral(1))),
                MethodDecl(Id("main"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 594))

    def test_arr_742454123894514_cp(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = 1;

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(Id("a"),ArrayType(5,ClassType(Id("A"))),IntLiteral(1))),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 595))

    def test_arr_7424541238942342514_cp(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = [1, 2];

            func X(): Abc {
                string1 := 1;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(
                    Id("a"),
                    ArrayType(5,ClassType(Id("A"))),
                    ArrayLiteral([IntLiteral(1),IntLiteral(2)])
                )),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 596))

    def test_arr_74245412382423914_cp(self):
        _input = """
        class A {}

        class Program {
            const a: [5]A = [1, 2];

            func X(): Abc {
                string1 := 1;
                return;
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[]),
            ClassDecl(Id("Program"),[
                AttributeDecl(ConstDecl(
                    Id("a"),
                    ArrayType(5,ClassType(Id("A"))),
                    ArrayLiteral([IntLiteral(1),IntLiteral(2)])
                )),
                MethodDecl(Id("X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),IntLiteral(1)),
                    Return(None)
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 597))

    def test_program_127413545842344_cp(self):
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
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(ConstDecl(Id("hello"),StringType(),StringLiteral("hello")))
            ]),
            ClassDecl(Id("Program"),[
                AttributeDecl(VarDecl(Id("@a"),ClassType(Id("A")),NewExpr(Id("A"),[]))),
                MethodDecl(Id("@X"),[],ClassType(Id("Abc")),Block([
                    Assign(Id("string1"),FieldAccess(Id("A"),Id("hello")))
                ]))
            ])
        ]))
        self.assertTrue(TestAST.test(_input, expect, 598))

    def test_arr_ele_28479_cp(self):
        _input = """
        class B <- A {
            var lst : [5]int = [1, 2, 3];

            func lst(a:int):void {
                var x:int = self.lst[0];
                io.@writeInt(x);
            }
        }
        """
        expect = str(Program([
            ClassDecl(Id("A"),[
                AttributeDecl(VarDecl(Id("lst"),ArrayType(5,IntType()),ArrayLiteral([IntLiteral(1),IntLiteral(2),IntLiteral(3)]))),
                MethodDecl(Id("lst"),[VarDecl(Id("a"),IntType())],VoidType(),Block([
                    VarDecl(Id("x"),IntType(),ArrayCell(FieldAccess(SelfLiteral(),Id("lst")),IntLiteral(0))),
                    CallStmt(None,Id("@writeInt"),[Id("x")])
                ]))
            ],Id("B"))
        ]))
        self.assertTrue(TestAST.test(_input, expect, 599))
