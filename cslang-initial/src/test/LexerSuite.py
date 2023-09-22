import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test(self):
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("1234567", "1234567,<EOF>", 102))
        # self.assertTrue(TestLexer.test("0000001", "1,<EOF>", 103))
        self.assertTrue(TestLexer.test("1.2E-8", "1.2E-8,<EOF>", 104))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \\\"Where is John?\\\",<EOF>", 105))
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """, "This is a string containing tab \t,<EOF>", 106))
        self.assertTrue(TestLexer.test("@main", "@main,<EOF>", 107))
        self.assertTrue(TestLexer.test("// hello", "<EOF>", 108))
        self.assertTrue(TestLexer.test("/* hello */", "<EOF>", 109))
        self.assertTrue(TestLexer.test("/* This is a block comment so // has no meaning here */", "<EOF>", 110))
        self.assertTrue(TestLexer.test("//This is a line comment so /* has no meaning here", "<EOF>", 111))
        self.assertTrue(TestLexer.test(""" "abc \k" """, "Illegal Escape In String: abc \k", 112))
        self.assertTrue(TestLexer.test(""" "abc \t """, "Unclosed String: abc \t ", 113))
        self.assertTrue(TestLexer.test(""" "a \\ b" """, "Illegal Escape In String: a \ b", 114))
