# 数据类型之间在特定的场景可以互相转换
# 转换后的值需要进行接受操作，接收至原变量或赋值到一个新的变量
# str(x)  将x转化为字符串 所有的数据类型都可以转为字符串string类型
BianLiang1 = 1
print(type(BianLiang1),BianLiang1)
BianLiang2 = str (BianLiang1)
print(type(BianLiang2),BianLiang2)
BianLiang3 = 1.5
print(type(BianLiang3),BianLiang3)
BianLiang4 = str(BianLiang3)
print(type(BianLiang4),BianLiang4)
# 分割线-------------------------------------------
print("------------------------------------------")
# int(x) 将x转换为整数
BianLiang5 = "11"
print(type(BianLiang5),BianLiang5)
BianLiang6 = int(BianLiang5)
print(type(BianLiang6),BianLiang6)
# 分割线-------------------------------------------
print("------------------------------------------")
# float(x) 将x转化为浮点数
BianLiang7 = "1.5"
print(type(BianLiang7),BianLiang7)
BianLiang8 = float(BianLiang7)
print(type(BianLiang8),BianLiang8)
print("------------------------------------------")
#浮点数向整数转换后，值向下取整，只保留整数
BianLiang9 = 2.8
print(type(BianLiang9),BianLiang9)
BianLiang10 = int (BianLiang9)
print(type(BianLiang10),BianLiang10)
print("------------------------------------------")
# 整数转化位浮点类型
BianLiang11 = 5
print(type(BianLiang11),BianLiang11)
BianLiang12 = float(BianLiang11)
print(type(BianLiang12),BianLiang12)
# 分割线-------------------------------------------
print("------------------------------------------")
# 字符串向整数和浮点类型转换时，要保证字符串内的数据内容符合整数和浮点数的数据类型定义（纯数字）
BianLiang13 = "5"
print(type(BianLiang13),BianLiang13)
BianLiang14 = int(BianLiang13)
print(type(BianLiang14),BianLiang14)
BianLiang15 = float(BianLiang13)
print(type(BianLiang15),BianLiang15)
print("------------------------------------------")
BianLiang16 = "5.5"
print(type(BianLiang16),BianLiang16)
BianLiang17 = float(BianLiang16)
print(type(BianLiang17),BianLiang17)
# 字符串中包含小数的数字无法直接向整数类型转换，需要先转化为浮点数，再从浮点数转换位整数
BianLiang18 = int(BianLiang17)
print(type(BianLiang18),BianLiang18)
#
