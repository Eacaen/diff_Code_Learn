import unittest
import string

class StringStripTestCase(unittest.TestCase):
#省略StringStripTestCase实现代码

class StringReplaceTestCase(unittest.TestCase):
#省略StringReplaceTestCase实现代码

def suite():    
    StringStripTestSuite = unittest.makeSuite(StringStripTestCase,'test')   
    StringReplaceTestSuite = unittest.makeSuite(StringReplaceTestCase,'test')
    
    alltests = unittest.TestSuite((StringStripTestSuite, StringReplaceTestSuite))
    return alltests

if __name__ == "__main__":
    runner = unittest.TextTestRunner()

    runner.run(suite())
