# 获取信息输入 如键盘输入
# input 语句 #
# 1.使用 ” input（） “来获取信息输入
# 2.使用变量接受（存储）获取到的数据
# ---------------------------------------------
# 字符串类型
print("随便输入点啥")
A = input("输点啥吧求你了\n")             # 将input获取的值赋予变量A（可在input语句的括号中属于提示语句，以替代第五行的print语句）
print("刚刚输入了：",A)  # 打印输出
print("输入的类型是：",type(A))
# ----------------------------------------------
# 数字类型（整数（int）浮点（float））
B = input("来俩数字\n")
print("刚刚输入的是：",B,"类型为：",type(B))
# ↑input 默认会将获取到的内容存为字符串（string)
# 进行数据类型转换
C = input("来俩数字\n这次给你转换数据类型\n")
C = int(C)
print(f"刚刚输入的是：{C}","类型为：",type(C))