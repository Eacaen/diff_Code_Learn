# 三引号制作doc文档
class Hello:
    '''hello class'''
    def printHello():
        '''print hello world'''
        print ("hello world!")
print( Hello.__doc__)
print (Hello.printHello.__doc__)
