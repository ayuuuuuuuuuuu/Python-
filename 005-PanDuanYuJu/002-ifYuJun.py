# if-else 语句
age =  input("输入你的年龄：\n")
age = int(age)
if age >= 18:
    print("你已经成年") # if语句下的语句以一个tab值的缩进表示属于上方if语句，若无缩进则不受if语句影响
else:
    print("你还未成年")
# -----------------------------------------------------------
print("------------------------------------------------------")
# if-elif-else多条件判断
# if - elif 自上而下逐个判断，在符合判断表达式时跳出，并执行属于该if或elif的下属语句，所有判断语句不符合执行else下的归属语句
gao = int(input("你有多高：(cm)\n"))
if gao >= 200:
    print("两米多高")
elif gao >= 190:
    print("一米九多")
elif gao >= 180:
    print("一米八多")
elif gao >= 170:
    print("一米七多")
elif gao >= 160:
    print("一米六多")
else:
    print("不到一米六")
# -----------------------------------------------------------
print("------------------------------------------------------")
# 判断语句中的变量可以直接替换为input获取的值
print("身高120cm以下、年龄小于12岁、或持有免票卡可免费乘车")
if int(input("请告知身高（cm）:\n")) < 120:
    print("身高120以下免票")
elif int(input("请告知年龄：\n")) < 12:
    print("十二岁以下免票")
elif (input("是否持有免票卡(请输入”是“或“否”)\n")) == "是":
    print("持卡可免费乘车")
else:
    print("请购买车票")
# -----------------------------------------------------------
print("------------------------------------------------------")
print("猜猜心里的数字！（0-9）")
if int(input("请输入一个数字\n（你有三次机会）：\n")) == 3:
    print("猜对咯")
elif int(input("请输入一个数字\n（你还有两次机会）\n")) == 3:
    print("猜对咯")
elif int(input("请输入一个数字\n（你还有一次机会）\n")) == 3:
    print("猜对咯")
else:
    print("这个数字是3")
# -----------------------------------------------------------
print("------------------------------------------------------")
# 判断语句的嵌套： 自由组合 if-elif-else 来进行多层次的判断语句
# 以缩进区分多个if语句
print("身高120cm以下、年龄小于12岁、或持有免票卡可免费乘车")
if int(input("请告知身高（cm）:\n")) >= 120:
    print("身高不低于120cm需要购票，如年龄低于12岁或持有乘车卡请说明")
    if int(input("请告知你的年龄\n")) >= 12:
        print("年龄超过12岁需要购票，若持有乘车卡请说明")
        if (input("是否持有乘车卡（输入“是”或“否”）\n")) != "是":
            print("请购买车票")
        else:
            print("请凭借乘车卡免费乘车")
    else:
        print("年龄未满12岁可免费乘车")
else:
    print("身高不足120cm可免费乘车")
# -----------------------------------------------------------
print("------------------------------------------------------")
# 判读出 年龄在18-30岁之间（包含18和30），且在职满两年或员工等级不低于三级的人
NianLing = int(input("请输入你的年龄：\n"))
if  NianLing >= 18:
    if NianLing <=30:
        if int(input("请输入你的在职时间（年）\n")) >= 2:
            print("恭喜你符合条件")
        elif int(input("抱歉，你的入职时间不足，请告知你的员工级别为多少\n")) >= 3:
                print("恭喜你符合条件")
        else:
                print("抱歉，你的员工基本也未达到要求")
    else:
        print("抱歉，你不符合最高年龄限制")
else:
    print("抱歉，你不符合最低年龄限制")























