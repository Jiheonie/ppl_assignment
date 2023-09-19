import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test(self):
        self.assertTrue(TestLexer.test("abc\t", "abc,<EOF>", 101))
        self.assertTrue(TestLexer.test("1234567", "1234567,<EOF>", 102))
        self.assertTrue(TestLexer.test("0000001", "1,<EOF>", 103))
        self.assertTrue(TestLexer.test("1.2E-8", "1.2E-8,<EOF>", 104))
        self.assertTrue(TestLexer.test(""" "He asked me: \\"Where is John?\\"" """, "He asked me: \\\"Where is John?\\\",<EOF>", 105))
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \t" """, "This is a string containing tab \t,<EOF>", 106))
        self.assertTrue(TestLexer.test("@main", "@main,<EOF>", 107))
