class PythonUtilities(object):
    _public_methods_ = [ 'SplitString' ] #提供的接口名
    
    _reg_progid_ = "Python.Utilities" #注册的ProgID
    
    _reg_clsid_ = "{71A4461C-6EDC-4cda-AF97-6744234C8D38}"#注册的CLSID
    
    def SplitString(self, val, sep=None):
        import string
        if sep!= None: sep = str(sep)
        return string.split(str(val), sep)

if __name__=='__main__':
    #注册COM服务组件
    print ("Registering COM server...")
    import win32com.server.register
    win32com.server.register.UseCommandLine(PythonUtilities)
