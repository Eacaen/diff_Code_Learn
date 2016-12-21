import re
# 限定符的使用
tel1 = "0791-1234567"
print (re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel1))
tel2 = "010-12345678"
print (re.findall(r"\d{3}-\d{8}|\d{4}-\d{7}", tel2))
tel3 = "(010)12345678"
print (re.findall(r"[\( ]?\d{3}[\]-]?\d{8}|[\( ]?\d{4}[\]-]?\d{7}", tel3))

# 分组
p = re.compile(r"(abc)\1")
m = p.match("abcabcabc")
print (m.group(0))
print(m.group(1))
print (m.group())
p = re.compile(r"(?P<one>abc)(?P=one)")
m = p.search("abcabcabc")
print (m.group("one"))
print (m.groupdict().keys())
print (m.groupdict().values())
print (m.re.pattern)
