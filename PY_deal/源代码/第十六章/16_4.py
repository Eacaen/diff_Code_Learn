import unittest
import string

class StringStripTestCase(unittest.TestCase):
    def testBlank(self):
        expect = "HELLO"
        result = string.strip("HELLO     ")
        self.assertEqual(expect, result)

    def testStr(self):
       expect = "HELLO"
       result = string.strip("xxHELLOxx", "xx")
       self.assertEqual(expect, result)

class StringReplaceTestCase(unittest.TestCase):
#省略StringReplaceTestCase实现代码

def suite():    
    StringStripTestSuite = unittest.makeSuite(StringStripTestCase,'test')   
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
    
    alltests = unittest.TestSuite((StringStripTestSuite, StringReplaceTestSuite))
    return alltests
