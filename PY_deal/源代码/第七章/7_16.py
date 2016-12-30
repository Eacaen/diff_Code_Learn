# 读配置文件
import configparser

config = configparser.ConfigParser()
config.read("ODBC.ini")
sections = config.sections()                    # 返回所有的配置块
print ("配置块：", sections)
o = config.options("ODBC 32 bit Data Sources")  # 返回所有的配置项
print ("配置项：", o)
v = config.items("ODBC 32 bit Data Sources")
print ("内容：", v)
# 根据配置块和配置项返回内容
access = config.get("ODBC 32 bit Data Sources", "MS Access Database")
print (access)
excel = config.get("ODBC 32 bit Data Sources", "Excel Files")
print (excel)
dBASE = config.get("ODBC 32 bit Data Sources", "dBASE Files")
print (dBASE)
