class myURLOpener(urllib.request.FancyURLopener):

    def setAuth(self, user, passwd):
        self.user = user
        self.passwd = passwd

    def prompt_user_passwd(self, host, realm):
        return self.user, self.passwd

myurlopener = myURLOpener()
myurlopener.setAuth("user", "passwd")

op = myurlopener.open("http://www.secret.com")
