"""
随机生成一个数字，拥有三次猜中的机会，通过三层嵌套if语句来判断是否猜中
通过如下代码生成一个1-10的随机数
import random
num = random.randint(1,10)
若没有猜中，提示猜打了或者猜小了
"""
# 分割--------------------------------------------
# 嵌套1
import random
num_1 = int(random.randint(1,10))
num_2 = int(input("猜一猜这个数是多少（1-10）\n你有三次机会\n"))
if  num_2 != num_1:
    if num_2 > num_1:
        print("猜大了，往小点猜")
        num_3 = int(input("猜一猜这个数是多少（1-10）\n你还有两次机会\n"))
        if num_3 != num_1:
            if num_3 > num_1:
                print("猜大了，往小点猜")
                num_4 = int(input("猜一猜这个数是多少（1-10）\n你还有一次机会\n"))
                if num_4 != num_1:
                    if num_4 > num_1:
                        print("猜大了，正确数字是：", num_1)
                else:
                    print("恭喜你猜对了！")
            elif num_3 < num_1:
                print("猜小了，往大了猜")
                num_4 = int(input("猜一猜这个数是多少（1-10）\n你还有一次机会\n"))
                if num_4 != num_1:
                    if num_4 < num_1:
                        print("猜小了，正确数字是：", num_1)
                else:
                    print("恭喜你猜对了！")
        else:
            print("恭喜你猜对了！")
    elif num_2 < num_1:
        print("猜小了，往大了猜")
        num_3 = int(input("猜一猜这个数是多少（1-10）\n你还有两次机会\n"))
        if num_3 != num_1:
            if num_3 > num_1:
                print("猜大了，往小点猜")
                num_4 = int(input("猜一猜这个数是多少（1-10）\n你还有一次机会\n"))
                if num_4 != num_1:
                    if num_4 > num_1:
                        print("猜大了，正确数字是：", num_1)
                else:
                    print("恭喜你猜对了！")
            elif num_3 < num_1:
                print("猜小了，往大了猜")
                num_4 = int(input("猜一猜这个数是多少（1-10）\n你还有一次机会\n"))
                if num_4 != num_1:
                    if num_4 < num_1:
                        print("猜小了，正确数字是：", num_1)
                else:
                    print("恭喜你猜对了！")
        else:
            print("恭喜你猜对了！")
else:
    print("恭喜你猜对了！")
# 分割 ----------------------------------------------------------
# 嵌套 2
print("----------------------------------------------------------")
num_a = int(random.randint(1,10))
num_b = int(input("猜一猜这个数是多少（1-10）\n你有三次机会\n"))
if  num_b == num_a:
    print("恭喜你猜对了！")
elif num_b  > num_a:
    print("猜大了，往小点猜")
    num_c = int(input("猜一猜这个数是多少（1-10）\n你有两次机会\n"))
    if num_c == num_a:
        print("恭喜你猜对了！")
    elif num_c > num_a:
        print("猜大了，往小点猜")
        num_d = int(input("猜一猜这个数是多少（1-10）\n你有一次机会\n"))
        if num_d == num_a:
            print("恭喜你猜对了！")
        elif num_d > num_a:
            print("猜大了，正确数字是",num_a)
        elif num_d < num_a:
            print("猜小了，正确数字是", num_a)
    elif num_c < num_a:
        print("猜小了，往大点猜")
        num_d = int(input("猜一猜这个数是多少（1-10）\n你有一次机会\n"))
        if num_d == num_a:
            print("恭喜你猜对了！")
        elif num_d > num_a:
            print("猜大了，正确数字是", num_a)
        elif num_d < num_a:
            print("猜小了，正确数字是", num_a)
elif num_b  < num_a:
    print("猜小了，往大点猜")
    num_c = int(input("猜一猜这个数是多少（1-10）\n你有两次机会\n"))
    if num_c == num_a:
        print("恭喜你猜对了！")
    elif num_c > num_a:
        print("猜大了，往小点猜")
        num_d = int(input("猜一猜这个数是多少（1-10）\n你有一次机会\n"))
        if num_d == num_a:
            print("恭喜你猜对了！")
        elif num_d > num_a:
            print("猜大了，正确数字是",num_a)
        elif num_d < num_a:
            print("猜小了，正确数字是", num_a)
    elif num_c < num_a:
        print("猜小了，往大点猜")
        num_d = int(input("猜一猜这个数是多少（1-10）\n你有一次机会\n"))
        if num_d == num_a:
            print("恭喜你猜对了！")
        elif num_d > num_a:
            print("猜大了，正确数字是",num_a)
        elif num_d < num_a:
            print("猜小了，正确数字是", num_a)
# 分割-----------------------------------------------
# 不完全嵌套
num_A = int(random.randint(1,10))
num_B = int(input("猜一猜这个数是多少（1-10）\n你有三次机会\n"))
if num_B == num_A:
    print("猜对了")
elif num_B > num_A:
    print("猜大了，往小点猜")
elif num_B < num_A:
    print("猜小了，往大点猜")
num_B = int(input("猜一猜这个数是多少（1-10）\n你有两次机会\n"))
if num_B == num_A:
    print("猜对了")
elif num_B > num_A:
    print("猜大了，往小点猜")
elif num_B < num_A:
    print("猜小了，往大点猜")
num_B = int(input("猜一猜这个数是多少（1-10）\n你有一次机会\n"))
if num_B == num_A:
    print("猜对了")
elif num_B > num_A:
    print("猜大了，正确数字是",num_A)
elif num_B < num_A:
    print("猜小了，正确数字是",num_A)




























