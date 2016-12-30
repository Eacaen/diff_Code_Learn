# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import itchat
def print_content(msg):
    print(msg['Text'])

itchat.auto_login()
itchat.run()
itchat.auto_login(hotReload=True)
itchat.send(u'测试消息发送', 'filehelper')