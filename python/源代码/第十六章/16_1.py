#filename: tdd_1.py
import unittest
import string

class StringReplaceTestCase1(unittest.TestCase):
    """测试空字符替换"""
    def runTest(self):
        source = “HELLO”
        expect = "HELLO"
        result = string.replace(source, "", "")
        self.assertEqual(expect, result)

class StringReplaceTestCase2(unittest.TestCase):
    """测试空字符替换成常规字符"""
    def runTest(self):
        source = “HELLO”
        expect = "*H*E*L*L*O*"
        result = string.replace(source, "", "*")
        self.assertEqual(expect, result)        

class StringReplaceTestCase3(unittest.TestCase):
    """测试常规字符替换为空字符"""
    def runTest(self):
        source = “HELLO”
        expect = "HEO"
        result = string.replace(source, "LL", "")
        self.assertEqual(expect, result)

class StringReplaceTestCase4(unittest.TestCase):
    """测试常规字符换"""
    def runTest(self):
        source = “HELLO”
        expect = "HEMMO"
        result = string.replace(source, "LL", "MM")
        self.assertEqual(expect, result)        
