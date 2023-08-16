# 字面量
# 被写下来的固定的值
"""
----数字----
整数（int）
浮点数（float）
复数（complex）4+3j 以j结尾表示复数
----字符串----string
 即文本，由任意数量的字符（中文，英文，各类符号，数字等组成）
 （“string”）
"""
# 使用type()查看数据类型
# int
a = 1
print(type(a),a)
# float
b = 1.5
print(type(b),b)
# complex
c = 4+3j
print(type(c),c)
# string
# 三种定义方式
d = "abc123"
print(type(d),d)
e = 'abc123'
print(type(e),e)
# 三双引号中的值未被操作和接受是即作为注释存在
f = """abc123"""
print(type(f),f)
# --------------------------------------------------------
# 定义字符串时字符串内容若需要包含 “ ” 以及 ' '时(最外层定义生效)
A = "'sadsadasd'"
print(type(A),A)
B = '"sdasdasdasdas"'
print(type(B),B)
C = '"""wqeweqeqwe"""'
print(type(C),C)
# 以及可以使用 " \ " 解除字符串定义符号(接触\后的首个符号的定义作用)
D = "\""
print(type(D),D)
E = '\''
print(type(E),E)