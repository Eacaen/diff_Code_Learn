#filename: tdd_2.py

import unittest
import string

class SimpleStringReplaceTestCase(unittest.TestCase):
     “””  准备测试的源字符串 ”””
    def setUp(self):
        self.source = "HELLO"

class StringReplaceTestCase1(SimpleStringReplaceTestCase):
    """测试空字符替换"""
    def runTest(self):
        expect = "HELLO"
        result = string.replace(self.source, "", "")
        self.assertEqual(expect, result)

class StringReplaceTestCase2(SimpleStringReplaceTestCase):
    """测试空字符替换成常规字符"""
    def runTest(self):
        expect = "*H*E*L*L*O*"
        result = string.replace(self.source, "", "*")
        self.assertEqual(expect, result)        

class StringReplaceTestCase3(SimpleStringReplaceTestCase):
    """测试常规字符替换为空字符"""
    def runTest(self):
        expect = "HEO"
        result = string.replace(self.source, "LL", "")
        self.assertEqual(expect, result)

class StringReplaceTestCase4(SimpleStringReplaceTestCase):
    """测试常规字符换"""
    def runTest(self):
        expect = "HEMMO"
        result = string.replace(self.source, "LL", "MM")
        self.assertEqual(expect, result)
