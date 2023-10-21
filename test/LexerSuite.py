import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test1_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc", "abc,<EOF>", 101))

    def test2_float(self):
        """test float"""
        self.assertTrue(TestLexer.test("7.10E-5", "7.10E-5,<EOF>", 102))

    def test3_unclose_string1(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"this is an unclosed string", "Unclosed String: this is an unclosed string", 103))

    def test4_unclose_string2(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"this is an unclosed string \\f", "Unclosed String: this is an unclosed string \\f", 104))

    def test5_comment(self):
        """test string"""
        self.assertTrue(TestLexer.test("/*comment test test*/", "<EOF>", 105))

    def test6_illegal_string1(self):
        """test string"""
        self.assertTrue(TestLexer.test("\"illegally escapsed\\a", "Unclosed String: illegally escapsed\\a", 106))

    def test7_test_bool(self):
        """test string"""
        self.assertTrue(TestLexer.test("true", "true,<EOF>", 107))

    def test8_test_int(self):
        """test string"""
        self.assertTrue(TestLexer.test("1234233332222", "1234233332222,<EOF>", 108))

    def test9_int_array(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("break function", "break,function,<EOF>", 109))

    def test10_type_auto(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("auto", "auto,<EOF>", 110))

    def test11_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John?\\\"\"", "He asked me: \\\"Where is John?\\\",<EOF>", 111)) 

    def test12_int(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("01234", "1234,<EOF>", 112))   

    def test13_errortoken(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("@#", "Error Token @", 113))   

    ## Testcase nay k hieu tai sao
    def test14_float(self): 
        """test identifiers"""
        self.assertTrue(TestLexer.test("128e++42", "128,e,+,+,42,<EOF>", 114))
    
    def test15_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"test string\\\"", "Unclosed String: test string\\\"", 115))

    def test16_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\b\"", "this is a string \\b,<EOF>", 116))

    def test17_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\r\"", "this is a string \\r,<EOF>", 117))

    def test18_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\f\"", "this is a string \\f,<EOF>", 118))    
    
    def test19_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("\"this is a string \\'\"", "Illegal Escape In String: this is a string \\'", 119))

    def test20_string(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test(" \"this is a string \\\\\" ", "Unclosed String: this is a string \\\\\" ", 120))

    def test21_float(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("23.12E-231", "23.12E-231,<EOF>", 121))

    def test22_random(self):
        self.assertTrue(TestLexer.test("ab.5e3c", "ab,.,5e3,c,<EOF>", 122))
    
    def test23_random(self):
        self.assertTrue(TestLexer.test("^bc_t", "^,bc_t,<EOF>", 123))
    
    def test24_random(self):
        self.assertTrue(TestLexer.test("abc&d", "abc,Error Token &", 124))
    
    def test25_random(self):
        self.assertTrue(TestLexer.test("3e=4", "3,e,=,4,<EOF>", 125))

    def test26_random(self):
        self.assertTrue(TestLexer.test("\"hello#llo", "Unclosed String: hello#llo", 126))

    def test27_random(self):
        self.assertTrue(TestLexer.test("a432.2e8bc", "a432,.,2e8,bc,<EOF>", 127))
    
    def test28_random(self):
        self.assertTrue(TestLexer.test("a,32.43eabc", "a,,,32.43,eabc,<EOF>", 128))

    def test29_random(self):
        self.assertTrue(TestLexer.test("king@123", "king,@123,<EOF>", 129))
    
    def test30_random(self):
        self.assertTrue(TestLexer.test("a&&bc b-3=2", "a,&&,bc,b,-,3,=,2,<EOF>", 130))
    
    def test31_random18(self):
        self.assertTrue(TestLexer.test("[3*2]+3###", "[,3,*,2,],+,3,Error Token #", 131))
    
    def test32_random19(self):
        self.assertTrue(TestLexer.test("b=\"\\nhello\"", "b,=,\\nhello,<EOF>", 132))

    def test33_random20(self):
        self.assertTrue(TestLexer.test("b2=\"\\'hello\"", "b2,=,Illegal Escape In String: \\\'", 133))

    def test34_random21(self):
        self.assertTrue(TestLexer.test("integer2323", "integer2323,<EOF>", 134))
    
    def test35_random22(self):
        self.assertTrue(TestLexer.test("stringAbc", "stringAbc,<EOF>", 135))
    
    def test36_random(self):
        self.assertTrue(TestLexer.test("\\thello", "\,thello,<EOF>", 136))
    
    def test37_random(self):
        self.assertTrue(TestLexer.test("\"hello \\\"ahaha\\n\\t\\f\"", "hello \\\"ahaha\\n\\t\\f,<EOF>", 137))
        
    def test38_random(self):
        self.assertTrue(TestLexer.test("abc __32 = 3 .4 .2e3", "abc,__32,=,3,.,4,.,2e3,<EOF>", 138))
        
    def test39_random(self):
        self.assertTrue(TestLexer.test("printInteger(a,b,c);", "printInteger,(,a,,,b,,,c,),;,<EOF>", 139))
        
    def test40_random(self):
        self.assertTrue(TestLexer.test("writeln(\"Hello World\\n\\t\");", "writeln,(,Hello World\\n\\t,),;,<EOF>", 140))

    def test41_random(self):
        self.assertTrue(TestLexer.test("while (a==3) a ++;", "while,(,a,==,3,),a,+,+,;,<EOF>", 141))
        
    def test42_random(self):
        self.assertTrue(TestLexer.test("for(i=1,i!=b,i+4)", "for,(,i,=,1,,,i,!=,b,,,i,+,4,),<EOF>", 142))
        
    def test43_random(self):
        self.assertTrue(TestLexer.test("a,b,c :boolean = 3,2,1;", "a,,,b,,,c,:,boolean,=,3,,,2,,,1,;,<EOF>", 143))
        
    def test44_random(self):
        self.assertTrue(TestLexer.test("ab'c", "ab,Error Token '", 144))
        
    def test45_random(self):
        self.assertTrue(TestLexer.test("/*hello*/a=b=c", "a,=,b,=,c,<EOF>", 145))
        
    def test46_random(self):
        self.assertTrue(TestLexer.test("3^2", "3,^,2,<EOF>", 146))

    def test47_random(self):
        self.assertTrue(TestLexer.test(".e-0", ".,e,-,0,<EOF>", 147))
        
    def test48_random(self):
        self.assertTrue(TestLexer.test("3!212", "3,!,212,<EOF>", 148))
        
    def test49_random(self):
        self.assertTrue(TestLexer.test("3_3", "3,_3,<EOF>", 149))
        
    def test50_random(self):
        self.assertTrue(TestLexer.test("ping999", "ping999,<EOF>", 150))

    def test51_random(self):
        self.assertTrue(TestLexer.test("a~b", "a,Error Token ~", 151))
        
    def test52_random(self):
        self.assertTrue(TestLexer.test("\"a~b\"", "a~b,<EOF>", 152))
        
    def test53_random(self):
        self.assertTrue(TestLexer.test("hello_32.3", "hello_32,.,3,<EOF>", 153))
        
    def test54_random(self):
        self.assertTrue(TestLexer.test("T_T", "T_T,<EOF>", 154))
        
    def test55_random(self):
        self.assertTrue(TestLexer.test(")(&&@", "),(,&&,Error Token @", 155))

    def test56_random(self):
        self.assertTrue(TestLexer.test("\"hello\\\"world\"", "hello\\\"world,<EOF>", 156))

    def test57_random(self):
        self.assertTrue(TestLexer.test("\"hello\\\'world\"", "Illegal Escape In String: hello\\\'", 157))

    def test58_random(self):
        self.assertTrue(TestLexer.test("\"hello\\bworld\"", "hello\\bworld,<EOF>", 158))

    def test59_random(self):
        self.assertTrue(TestLexer.test("\"hello\\fworld\"", "hello\\fworld,<EOF>", 159))

    def test60_random(self):
        self.assertTrue(TestLexer.test(".1e+10", ".,1e+10,<EOF>", 160))

    def test61_random(self):
        self.assertTrue(TestLexer.test(".E-10", ".,E,-,10,<EOF>", 161))

    def test62_random(self):
        self.assertTrue(TestLexer.test("1.00E", "1.00,E,<EOF>", 162))

    def test63_random(self):
        self.assertTrue(TestLexer.test("1.00E +123", "1.00,E,+,123,<EOF>", 163))

    def test64_random(self):
        self.assertTrue(TestLexer.test("1_111.11e11", "1,_111,.,11e11,<EOF>", 164))

    def test65_random(self):
        self.assertTrue(TestLexer.test("abc//de", "abc,<EOF>", 165))

    def test66_random(self):
        self.assertTrue(TestLexer.test("abc//abc\r\nABC", "abc,ABC,<EOF>", 166))

    def test67_random(self):
        self.assertTrue(TestLexer.test("123//456//789", "123,<EOF>", 167))

    def test68_random(self):
        self.assertTrue(TestLexer.test("/*hello*/*hello*/", "*,hello,*,/,<EOF>", 168))

    def test69_random(self):
        self.assertTrue(TestLexer.test("a[1,0]", "a,[,1,,,0,],<EOF>", 169))

    def test70_random(self):
        self.assertTrue(TestLexer.test("a[1, 0]", "a,[,1,,,0,],<EOF>", 170))  

    def test71_random(self):
        self.assertTrue(TestLexer.test("inherit out _a1 : integer", "inherit,out,_a1,:,integer,<EOF>", 171))
    
    def test72_random(self):
        self.assertTrue(TestLexer.test("    {\"Na\", \"Sa\", \"Sa\"}", "{,Na,,,Sa,,,Sa,},<EOF>", 172))

    def test73_random(self):
        self.assertTrue(TestLexer.test("a,b:array [5, 5] of integer", "a,,,b,:,array,[,5,,,5,],of,integer,<EOF>", 173))

    def test74_random(self):
        self.assertTrue(TestLexer.test("2:2", "2,:,2,<EOF>", 174))
        
    def test75_random(self):
        self.assertTrue(TestLexer.test("&&&", "&&,Error Token &", 175))

    def test76_random(self):
        self.assertTrue(TestLexer.test("|||", "||,Error Token |", 176))

    def test77_random(self):
        self.assertTrue(TestLexer.test("<><>>><", "<,>,<,>,>,>,<,<EOF>", 177))

    def test78_random(self):
        """test error token"""
        self.assertTrue(TestLexer.test("hello`world", "hello,Error Token `", 178))

    def test79_random(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a&b", "a,Error Token &", 179))

    def test80_random(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a|b", "a,Error Token |", 180))

    def test81_random(self):
        """test error token"""
        self.assertTrue(TestLexer.test("a.b", "a,.,b,<EOF>", 181))

    def test82_random(self):
        self.assertTrue(TestLexer.test("\"hello\\bworld\"", "hello\\bworld,<EOF>", 182))

    def test83_random(self):
        self.assertTrue(TestLexer.test("\"hello\\fworld\"", "hello\\fworld,<EOF>", 183))

    def test84_random(self):
        self.assertTrue(TestLexer.test("\"hello\\rworld\"", "hello\\rworld,<EOF>", 184))

    def test85_random(self):
        self.assertTrue(TestLexer.test("\"hello\\tworld\"", "hello\\tworld,<EOF>", 185))

    def test86_random(self):
        self.assertTrue(TestLexer.test("9.0", "9.0,<EOF>", 186))

    def test87_random(self):
        self.assertTrue(TestLexer.test("12e8", "12e8,<EOF>", 187))

    def test88_random(self):
        self.assertTrue(TestLexer.test("0.33E-3", "0.33E-3,<EOF>", 188))

    def test89_random(self):
        self.assertTrue(TestLexer.test("1.", "1.,<EOF>", 189))
    
    def test90_random(self):
        self.assertTrue(TestLexer.test("self", "self,<EOF>", 190))

    def test91_string(self):
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 191))

    def test92_float(self):
        self.assertTrue(TestLexer.test("1.2E-8", "1.2E-8,<EOF>", 192))
    
    def test93_string(self):
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \\\"Where is John?\\\",<EOF>", 193))

    def test94_string(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """, "This is a string containing tab \t,<EOF>", 194))

    def test95_id(self):
        self.assertTrue(TestLexer.test("@main", "@main,<EOF>", 195))

    def test96_cmt(self):
        self.assertTrue(TestLexer.test("// hello", "<EOF>", 196))

    def test97_cmt(self):
        self.assertTrue(TestLexer.test("/* hello */", "<EOF>", 197))
    
    def test98_2_cmt(self):
        self.assertTrue(TestLexer.test("/* This is a block comment so // has no meaning here */", "<EOF>", 198))

    def test99_2_cmt(self):
        self.assertTrue(TestLexer.test("//This is a line comment so /* has no meaning here", "<EOF>", 199))

    def test100_illegal_esc(self):
        self.assertTrue(TestLexer.test(""" "abc \k" """, "Illegal Escape In String: abc \k", 200))

    def test101_unclosed_str(self):
        self.assertTrue(TestLexer.test(""" "abc \t """, "Unclosed String: abc \t ", 201))

    def test102_illegal_esc(self):
        self.assertTrue(TestLexer.test(""" "a \ b" """, "Illegal Escape In String: a \ ", 202))

    def test103_illegal_esc(self):
        self.assertTrue(TestLexer.test(""" "a \\ b" """, "Illegal Escape In String: a \ ", 203))

    def test104_str_esc(self):
        self.assertTrue(TestLexer.test(""" "a \\\ b" """, "a \\\\ b,<EOF>", 204))

    def test105_str_esc(self):
        self.assertTrue(TestLexer.test(""" "a \\\\ b" """, "a \\\\ b,<EOF>", 205))

    def test106_cmt(self):
        self.assertTrue(TestLexer.test("""/*abcxyz*/ 1234""", "1234,<EOF>", 206))
    
    def test107_underscore_id(self):
        self.assertTrue(TestLexer.test("""_abcd""", "_abcd,<EOF>", 207))

    def test108_invalid_id(self):
        self.assertTrue(TestLexer.test("""1abcd""", "1,abcd,<EOF>", 208))

    def test109_invalid_float(self):
        self.assertTrue(TestLexer.test(""".12""", ".,12,<EOF>", 209))

    def test110_inv_float(self):
        self.assertTrue(TestLexer.test("""143e""", "143,e,<EOF>", 210))

    def test111_unclosed_str(self):
        self.assertTrue(TestLexer.test(""" "illegally escaped\\a """, "Unclosed String: illegally escaped\\a ", 211))

    def test112_illegal_esc(self):
        self.assertTrue(TestLexer.test(""" "illegally escaped\k " """, "Illegal Escape In String: illegally escaped\k", 212))
    
    def test_113_cmt(self):
        self.assertTrue(TestLexer.test("""143e+2 /*comment*/ 20""", "143e+2,20,<EOF>", 213))

    def test_114_class(self):
        self.assertTrue(TestLexer.test("""class A{}""", "class,A,{,},<EOF>", 214))

    def test115_class(self):
        self.assertTrue(TestLexer.test("""class A{var delta: int = 3;}""", "class,A,{,var,delta,:,int,=,3,;,},<EOF>", 215))

    def test116_class(self):
        self.assertTrue(TestLexer.test("""class A <- B{var delta: int = 3;}""", "class,A,<-,B,{,var,delta,:,int,=,3,;,},<EOF>", 216))

    def test117_class(self):
        self.assertTrue(TestLexer.test("""class Program{ const a, b: int = 3, 6;}""", "class,Program,{,const,a,,,b,:,int,=,3,,,6,;,},<EOF>", 217))
    
    def test118_class(self):
        self.assertTrue(TestLexer.test("""class A <- B{var @a: bool = false;}""", "class,A,<-,B,{,var,@a,:,bool,=,false,;,},<EOF>", 218))

    def test119_class(self):
        self.assertTrue(TestLexer.test("""1 + 2""", "1,+,2,<EOF>", 219))

    def test120_unc_str(self):
        self.assertTrue(TestLexer.test(""" "illegally escaped\m """, "Unclosed String: illegally escaped\m ", 220))

    def test121_ill_esc(self):
        self.assertTrue(TestLexer.test(""" "illegally escaped\mx" """, "Illegal Escape In String: illegally escaped\m", 221))

    def test122_op(self):
        self.assertTrue(TestLexer.test(""" ><=>=<>= """, ">,<=,>=,<,>=,<EOF>", 222))

    def test123_esc(self):
        self.assertTrue(TestLexer.test(""" "\nhello\t" """, "\n\nhello\t,<EOF>", 223))

    def test124_esc(self):
        self.assertTrue(TestLexer.test(""" "\\nhello\t" """, "\\nhello\t,<EOF>", 224))

    def test125_esc(self):
        self.assertTrue(TestLexer.test(""" "\\\nhello\t" """, "Illegal Escape In String: \\\n", 225))

    def test126_esc(self):
        self.assertTrue(TestLexer.test(""" "\\\\nhello\t" """, "\\\\nhello\t,<EOF>", 226))

    def test127_str(self):
        self.assertTrue(TestLexer.test(""" "This is a string\\b" """, "This is a string\\b,<EOF>", 227))

    def test128_str_esc(self):
        self.assertTrue(TestLexer.test(""" "\\\\" """, "Unclosed String: \\\\\" ", 228))