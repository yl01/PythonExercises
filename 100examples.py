#!/user/bin/python
# -*- coding:utf-8 -*-
'''01.题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？'''
# sum = 0
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and i!=k and j!=k:
#                 print(100*i+10*j+k)
#                 sum+=1
# print("共",sum)

'''02.题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？'''
# i = int(input('请输入净利润:'))
# # a = [100,60,40,20,10,0]
# # b = [0.01,0.015,0.03,0.05,0.075,0.1]
# # r = 0
# # for c in range(0,6):
# #     if i > a[c]:
# #         r+=((i-a[c])*b[c])
# #         print('区间提成:',(i-a[c])*b[c])
# #         i = a[c]
# # print("总提成为:",r)


'''03.题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
# import math
# for i in range(1,2000):
#     x = int(math.sqrt(i+100))
#     y = int(math.sqrt(i+100+168))
#     if (x*x == (i+100)) and (y*y == (i+100+168)):
#         print(i)


'''04.题目：输入某年某月某日，判断这一天是这一年的第几天？'''
# import time
# day =input("请输入日期:")
# f = time.strptime(day, '%Y/%m/%d')
# print(f.tm_yday)


'''05.题目：任意输入三个整数x,y,z，请把这三个数由小到大输出'''
# a = []
# for i in range(3):
#     x = int(input("请输入整数:"))
#     a.append(x)
# a.sort()
# print((a[0],a[1],a[2]))


'''06.题目：斐波那契数列,指的是从0，1开始，第三项为前两项之和。即：F0=0，F1=1，Fn=F[n-1]+F[n-2] (n>=2)'''
#方法一：
# def lib(n):
#     if n == 1 or n == 2:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return lib(n-1) + lib(n-2)
# print(lib(10))

#方法二：
# def lib(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return a
# print(lib(10))


'''07.题目：将一个列表的数据复制到另一个列表中'''
# a = [1,2,3]
# b = a[:]
# print(b)


'''08.题目：输出 9*9 乘法口诀表'''
# for i in range(1,10):
#     print()     #循环一次换行
#     for j in range(1,i+1):
#         print("{0}*{1}={2}\t".format(j,i,i*j),end='')


'''09.题目.计算三角形的面积'''
# a = float(input("请输入第一边长"))
# b = float(input("请输入第二边长"))
# c = float(input("请输入第三边长"))
# s = (a+b+c) / 2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('三角形的面积%0.2f' %area)


'''10.题目.生成随机数'''
# import random
# print(random.randint(0,9))


#获取10个数
#方法一：
# import random
# for i in range(10):
#     print(random.randint(1,100),end=',')

#方法二：
# import random
# a = [random.randint(1,100) for i in range(10)]
# print(a)


'''11.题目.输出1-100之间的素数'''
#方法一.for-else
# list1 = []
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     else:
#         list1.append(i)
# print(list1)

#方法二.while语句
# list1 = []
# i = 2
# while (i<100):
#     j = 2
#     while (j<=(i/j)):
#         if i%j == 0:break
#         j = j + 1
#     if (j>(i/j)):
#         list1.append(i)
#     i = i + 1
# print(list1)


'''12.题目.交换变量'''
# a = input("请输入变量a:")
# b = input(("请输入变量b:"))
# a,b=b,a
# print('交换后a的值为:{}'.format(a))
# print('交换后b的值为:{}'.format(b))


'''13.题目.if..elif..else语句判断正数、零、负数'''
#方法一：
# num = float(input("请输入一个数:"))
# if num>0:
#     print("正数")
# elif num==0:
#     print("零")
# else:
#     print("负数")

#方法二:
# num = float(input("请输入一个数:"))
# if num >= 0:
#     if num == 0:
#         print("零")
#     else:
#         print("正数")
# else:
#     print("负数")


'''14.题目.判断字符串是否为数字'''
# string = input("请输入一串字符:")
# #使用标志
# loop =1
# for i in range(len(string)):
#     if string[i] >= '0' and string[i] <= '9':
#         loop = 1
#     else:
#         loop = 0
# if loop == 1:
#     print("字符串是数字\n字符串为:",string)
# else:
#     print("字符串不是数字")


'''15.题目.判断奇偶数'''
# while True:
#     try:
#         num = int(input("输入一个整数：")) #判断输入是否为整数
#     except ValueError:#不是纯数字需要重新输入
#         print("输入的不是整数！")
#         continue
#     if num % 2 ==0:
#         print("{}是偶数".format(num))
#     else:
#         print("{}是奇数".format(num))
#     break

#方法二:
# num = eval(input("number:"))
# print('{} is '.format(num) + ('even number.'if num%2==0 else 'odd number.'))


'''16.题目.判断是否为闰年'''
#闰年：能被4整除但不能被100整除或者能被400整除
# year = int(input("请输入年份："))
# if ((year % 4 ==0 and year % 100 != 0 ) or year % 400 == 0):
#     print("{0}是闰年".format(year))
# else:
#     print("{0}不是闰年".format(year))


'''17.获取最大值函数'''
# print(max('a','b')) #获取字符串最大
# print(max([1,2]))  #获取列表最大
# print(max((1,2)))   #获取元组最大
# print(max(1,2))   #获取数字最大


'''18.题目.判断一个数是否为质数'''
# num = int(input("请输入一个整数:"))
# if num > 1 :
#     for i in range(2,num):
#         if num % i ==0:
#             print("{0}不是质数".format(num))
#             break
#     else:
#         print("{0}是质数".format(num))
# else:
#     print("请输入大于1的整数")


'''19.题目.输出指定范围的质数'''
# lower = int(input("输入最小区间:"))
# upper = int(input("输入最大区间:"))
# list1 = []
# for num in range(lower,upper+1):
#     if num > 1:
#         for i in range(2,num):
#             if num % i ==0:
#                 break
#         else:
#             list1.append(num)
# print(list1)


'''20.题目.输出1-100之间的素数'''
# list1 = []
# for num in range(2,101):
#     for i in range(2,num):
#         if num % i == 0:
#             break
#     else:
#         list1.append(num)
# print(list1)


'''21.题目.阶乘'''
# num = int(input("请输入一个数:"))
# # factorial = 1
# # if num < 0:
# #     print("负数没有阶乘")
# # elif num == 0:
# #     print("0的阶乘是1")
# # else:
# #     for i in range(1,num+1):
# #         factorial = factorial * i
# #     print("%d的阶乘是%d" %(num,factorial))


'''22.斐波那契数列指指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和'''
# nterms = int(input("你需要几项？"))
# n1,n2 = 0,1
# count = 2
# if nterms < 0:
#     print("请输入一个正数")
# elif nterms == 1:
#     print("斐波那契数列:")
#     print(n1)
# else:
#     print("斐波那契数列:")
#     print(n1,',',n2,end =',')
#     while count < nterms:
#         nth = n1 + n2
#         print(nth,end= ',')
#         n1,n2 = n2,nth
#         count = count+1


'''23.阿姆斯特朗数，如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153'''
# num = int(input("请输入一个整数:"))
# sum = 0
# n = len(str(num))  #获取指数
# term = num
# while term > 0:
#     digit = term % 10
#     sum += digit **n
#     term = term // 10   #/表示浮点除法，返回浮点结果，//表示整除法
# if sum == num:
#     print("%d是阿姆斯特朗数" %num)
# else:
#     print("%d不是阿姆斯特朗数" %num)


'''24.题目.最大公约数'''
# def hcf(x,y):
#     """该函数返回两个数的最大公约数"""
#     if x > y:
#         smaller = y
#     else:
#         smaller = x
#     for i in range(1,smaller+1):
#         if (x % i == 0) and (y % i == 0):
#             hcf = i
#     return hcf
# num1 = int(input("输入第一个数字"))
# num2 = int(input("输入第二个数字"))
# print(num1,'和',num2,'的最大公约数为',hcf(num1,num2))


'''25.题目.最小公倍数'''
#方法一.最小公倍数 = 两数之积/最大公约数
# def lcm(x,y):
#     for i in range(1,min(x,y)+1):
#         if (x % i == 0) and (y % i == 0):
#             lcm = (x*y) // i
#     print('最大公约数为',i)
#     return lcm
# num1 = int(input("输入第一个数"))
# num2 = int(input("输入第二个数"))
# print(num1,'和',num2,'的最小公倍数为',lcm(num1,num2))

#方法二.
# def lcm(x,y):
#     if x > y :
#         lager = x
#     else:
#         lager = y
#     while (True):
#         if ((lager % x == 0 ) and (lager % y == 0)):
#             lcm = lager
#             break
#         lager = lager + 1
#     return lcm
# num1 = int(input('输入第一个数:'))
# num2 = int(input('输入第二个数:'))
# print(num1,'和',num2,'的最小公倍数为',lcm(num1,num2))


'''26.题目.字符串大小写转换'''
# str = "hello world"
# print(str.upper()) #字符中所有小写转换成大写
# print(str.lower()) #字符中所有大写转化成小写
# print(str.capitalize())  #字符中第一个单词转换成大写，其余小写
# print(str.title())  #字符中每个单词的首字母大写，其余小写


'''27.题目.简单计算器实现'''
# def add(x,y):
#     return x + y
#
# def subtract(x,y):
#     return x - y
#
# def multiply(x,y):
#     x * y
#
# def divide(x,y):
#     x / y
#
# print("选择运算：")
# print("1、加法；2、减法；3、乘法；4、除法")
# choice = input("输入你的选择（1/2/3/4):")
# num1 = int(input("输入第一个数:"))
# num2 = int(input("输入第二个数:"))
# if choice == '1':
#     print(num1,"+",num2,"=",add(num1,num2))
# elif choice == '2':
#     print(num1,"-",num2,"=",subtract(num1,num2))
# elif choice == '3':
#     print(num1,"*",num2,"=",multiply(num1,num2))
# elif choice == '4':
#     print(num1,"/",num2,"=",divide(num1,num2))
# else:
#     print("输入有误，请重新输入！")


'''28.冒泡排序,时间O(n^2)'''
# def bubbleSort(num):
#     for i in range(0,len(num)-1):
#         for j in range(0,len(num)-i-1):
#             if num[j] > num[j+1]:
#                 num[j],num[j+1] = num[j+1],num[j]
#     return num
# # list1 = input("请输入一组数:")
# # list1 = (list1.split(',') ) #返回分割后的字符串列表
# # list1 = list(map(int,list1))  #列表字符串转数字
# list1 = list(map(int,input("请输入一组数:").split(',')))  #简洁写法
# print(list1)
# print(bubbleSort(list1))


'''29.二分查找（仅当列表有序时才管用），时间O(logn)'''
# def binary_search(list,item):
#     low = 0
#     high = len(list)-1
#     while low <= high:
#         mid = int((low + (high-low)/2))
#         if list[mid] == item:
#             return mid
#         elif list[mid] > item:
#             high = mid -1
#         else:
#             low = mid + 1
#     return None
# mylist = [2,3,5,7,9]
# print(mylist)
# print(binary_search(mylist,3))


'''30.选择排序'''
# def selection_Sort(list1):
#     for i in range(0,len(list1)-1):
#         min = i
#         for j in range(i+1,len(list1)):
#             if list1[j] < list1[min]:
#                 min = j
#         list1[i],list1[min] = list1[min],list1[i]
#         print(list1)
#     return list1
# mylist = [99,22,64,55,11]
# print(selection_Sort(mylist))


'''31.快速排序'''
'''32.插入排序'''
'''33.堆排序'''


'''34.生成10个随机数[0,100]且最终10个随机数之和为100，数字为整数，可重复'''
#思路：随机生成随机数，开区间（1,100），生成9个，然后按小到大排序，假设排序后这9个数字是a0,a1,...a8
#那么a0  a1-a0  a2-a1 ....  100-a8
# import random
# a = [random.randint(0,100) for i in range(9)]
# a.append(0)
# a.append(100)
# a.sort()
# print(a)
# b = [a[i+1] - a[i] for i in range(0,10)]
# print(b)


'''35.翻转转字符串和翻转列表'''
# str = 'python'
# print(str[::-1])
# list1 = [12,10,2,3,1]
# print(list1[::-1])
# list1.reverse()  #没有返回值，不能写list1=list1.reverse()
# print(list1)

'''36.对字符串切片机翻转'''
# def rotate(str,d):
#     lfirst = str[0:d]
#     lsecond = str[d:]
#     rfirst = str[0:len(str)-d]
#     rsecond = str[len(str)-d:]
#     print("头部切片翻转:",(lsecond+lfirst))
#     print("尾部切片翻转:",rsecond+rfirst)
#
# if __name__ == '__main__':
#     str = 'python'
#     d = 2
#     rotate(str,d)


'''37.将列表中头尾两个元素对调'''
# def swaplist(list1):
#     list1[0],list1[-1] = list1[-1],list1[0]
#     return list1
# newlist = [1,3,4,2]
# print(swaplist(newlist))

'''38.将列表中指定位置的元素对调'''
# def swaplist(list1,pos1,pos2):
#     list1[pos1],list1[pos2] = list1[pos2],list1[pos1]
#     return list1
# newlist = [2,3,1,4,6,7]
# print(swaplist(newlist,2,4))


'''39.计算字符串的长度'''
#方法一.利用内置函数
# str = 'python'
# print(len(str))
#
# #方法二.循环计算法
# def findlen(str):
#     count = 0
#     while str[count:]:
#         count += 1
#     return count
# str = 'python'
# print(findlen(str))


# '''40.计算元素在列表中出现的次数'''
# def countx(num,x):
#     count = 0
#     for i in num:
#         if i == x:
#             count = count +1
#     return count
# list1 = [1,2,2,3,2,4,2]
# num = countx(list1,2)
# print("出现次数:",num)


'''41.列表元素之和与积'''
# def multiply(list):
#     result = 1
#     for i in list:
#         result = result * i
#     return result
#
# def sum(list):
#     sum = 0
#     for i in list:
#         sum = sum + i
#     return sum
#
# mylist = [1,2,3,4]
# print("元素之积:",multiply(mylist))
# print("元素之和:",sum(mylist))


'''42.移除字符串中指定位置的字符'''
# str = 'python'
# print("原始字符串:" + str)
# newstr = ''
# for i in range(0,len(str)):
#     if i != 2 :
#         newstr = newstr + str[i]
# print("字符串移除后:" + newstr)


'''43.移除列表中指定位置的元素'''
# list1 = [1,2,3,4,5]
# print(list3)
# list2 = []
# for i in range(0,len(list1)):
#     if i != 2:
#         list2.append(list1[i])
# print(list2)


'''44.字符串判断'''
# str = 'python'
# print(str.isalpha())  #判断所有字符都是字母
# print(str.isalnum())  #判断所有字符都是数字或字母
# print(str.isdigit())  #判断所有字符都是数字


'''45.生成日历'''
# import calendar
# yy = int(input("输入年份:"))
# mm = int(input("输入月份:"))
# print(calendar.month(yy,mm))

'''46.计算每个月天数'''
# import calendar
# monthRange = calendar.monthrange(2016,9)
# print(monthRange)   #输出是一个元组，第一个元素表示所查月份的第一天是星期几（0-6），第二个元素表示这个月的天数


'''47.获取昨天的日期'''
# import datetime
# def getYesterday():
#     yesterday = datetime.date.today() - datetime.timedelta(days=1)
#     return yesterday
# print(getYesterday())


'''48.计算n个自然数的立方和'''
# def sumOfSeries(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i*i*i
#     return sum
# print(sumOfSeries(5))

'''49.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'''
#与波斐那锲数列类似
#方法1.
# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print('%12ld %12ld' %(f1,f2),end='' )
#     if (i % 3 == 0):
#         print(" ")
#     f1 = f1 + f2
#     f2 = f1 + f2


#方法二.
# def rabbit(n):
#     rabbit = [1,1]
#     for i in range(n-2):
#         rabbit.append((rabbit[-1] + rabbit[-2]))
#     return rabbit
# print(rabbit(4))

#方法三.递归效率低，当数字过大时，会很慢
# def lib(n):
#     if n ==1 or n == 2:
#         return 1
#     else:
#         return lib(n-1) + lib(n-2)
# print(lib(4))


'''50.打印出所有水仙花数，是指一个三位数，其各位数字立方和等于该数本身'''
# a = []
# for n in range(100,1000):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k **3:
#         a.append(n)
# print(a)

'''拓展50.判断输入的数是不是水仙花数'''
# num = int(input("请输入整数:"))
# n = len(str(num))  #int类型无法使用len函数
# temp = num
# sum = 0
# for i in range(n):
#     digit = temp % 10
#     temp = temp // 10
#     sum = sum + (digit ** n)
# if sum == num:
#     print('{0}是水仙花数'.format(num))
# else:
#     print("不是水仙花数")


'''51.将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5'''
# n = int(input("请输入要分解的正数:"))
# #创建一个列表用来存放遍历出来的因数
# lt = []
# #给n换个名字，便于打印时打印出用户输入的n
# m = n
#
# while n > 1:
#     for i in range(2,n+1):
#         if n % i == 0:
#             #记录下被最小因数分解后的n
#             n = n // i
#             #把i转换成str，存放在列表，便于后面用join拼接字符串列表
#             lt.append(str(i))
#             #找到一个最小的因数时，就跳出for循环，开始下一次循环
#             break
# if len(lt) == 1:
#     print(m,'=','1 x',m)
# else:
#     s = 'x'.join(lt)
#     print(m,'=',s)



'''52.输入成绩判断'''
# score = int(input("请输入分数:"))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
# print('%d属于%s' %(score,grade))


'''53.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数'''
# s = input("请输入一个字符串:")
# letters = 0
# space = 0
# digit = 0
# others = 0
# for c in s:
#     if c.isalpha():
#         letters += 1
#     elif c.isspace():
#         space += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         others += 1
# print("char=%d,space=%d,digit=%d,others=%d" %(letters,space,digit,others))


'''54.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制'''
# n = int(input("请输入个数:"))
# a = int(input('请输入数字:'))
# b = a
# lt = []
# s = 0
# for i in range(1,n+1):
#     lt.append(str(a))
#     a = a + b * (10 ** i)
# res = '+'.join(lt)
# for j in lt:
#     s += int(j)   #转换成int类型
# print(s,'=',res)



'''55.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数'''
#参考51题
#方法1.
# for i in range(2,1000):
# #     ls = []
# #     for j in range(1,i):
# #         if i % j == 0:
# #             ls.append(j)
# #     if i == sum(ls):
# #         print(i)
# #         print(ls)

#方法二.
# from functools import reduce
#
# def sum(x,y):
#     return x+y
#
# for i in range(2,1001):
#     ls = [1]
#     for j in range(2,int(i/2+1)):
#         if i % j == 0:
#             ls.append(j)
#     if i == reduce(sum,ls):
#         print(i)
#         print(ls)


'''56.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''
# height = 100
# tour = []
# h = []
# for i in range(1,11):
#     #从第二次开始，经过的距离是反弹高度的2倍
#     if i == 1:
#         tour.append(height)
#     else:
#         tour.append(height * 2)
#     height = height / 2
#     h.append(height)
# print("共经过%f米" %sum(tour))
# print("第10次反弹高度为:",h[-1])


'''57.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。'''
#逆向思维，从后往前算
# p = 1
# for i in range(9,0,-1):
#     p = (p + 1) * 2
#     print("第%d天剩%d个桃子" %(i,p))
# print("第一天共摘了%d个桃子" %p)

#递归方法
# def pean(n):
#     if n == 1:
#         return 1
#     else:
#         return (pean(n-1)+1)*2
# print(pean(10))


'''58.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单'''
# for a in range(ord('x'),ord('z')+1):
#     for b in range(ord('x'),ord('z')+1):
#         if(a != b):  #避免参赛队员重复比赛
#             for c in range(ord('x'),ord('z')+1):
#                 if (a!=c and b!=c):  #避免参赛队员重复比赛
#                     if (a!=ord('x') and c!=ord('x') and c!=ord('z')):
#                         print("order is a--%s\t b--%s\t c--%s" %(chr(a),chr(b),chr(c)))


'''59.打印菱形和对顶三角'''
#https://blog.csdn.net/chenlinan_2017/article/details/81434967
#菱形
# for i in range(-4,5):
#     if i < 0:
#         j = -i
#     else:
#         j = i
#     print(' '* j + '*'*(9-2*j))

#对顶三角形
# for i in range(-4,5):
#     if i < 0:
#         j = -i
#     else:
#         j = i
#     print(' '*(9//2-j) + '*'*(2*j+1))


'''60.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和'''
# a = 1.0
# b = 2.0
# s = 0
# for i in range(1,21):
#     s += b / a
#     a,b = b,a+b
# print("前20 项之和为:",s)


'''61.求1+2!+3!+...+20!的和'''
# s = 0
# t = 1
# for i in range(1,21):
#     t = t * i
#     s = s + t
# print("1+2!+3!+...+20!=%d" %s)


'''62.利用递归方法求5!'''
# def fact(i):
#     sum = 0
#     if i == 0:
#         sum = 1
#     else:
#         sum = i*fact(i-1)
#     return sum
# print(fact(5))


'''63.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来'''
# l = input("enter the string:")
# L = []
# for i in range(1,len(l)+1):
#     L.append(l[(-i)])
# print(L)


'''64.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？'''
#方法1.递归
# def age(n):
#     if n == 1:
#         c = 10
#     else:
#         c = age(n-1) + 2
#     return c
# print(age(5))

#方法2.
# age = 10
# for i in range(1,5):
#     age += 2
# print("第五个人的年龄:",age)


'''65.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字'''
#方法1.
# num = int(input("输入5位数以下的正整数:"))
# n = len(str(num))
# print("它是{0}位数".format(n))
# n = str(num)[::-1]
# print(n)
# for i in n:
#     print(i,end='')

#方法2.
# num = int(input("输入5位数以下的正整数:"))
# a = num // 10000
# b = num % 10000 // 1000
# c = num % 1000 // 100
# e = num % 100 // 10
# f = num % 10
# if a != 0:
#     print("它是5位数:",10000*f+1000*e+100*c+10*b+a)
# elif a == 0 and b!= 0:
#     print("它是4位数:",1000*f+100*e+10*c+b)
# elif a == 0 and b == 0 and c != 0:
#     print("它是3位数:",100*f+10*e+c)
# elif a == 0 and b == 0 and c == 0 and e != 0:
#     print("它是2位数:",10*f+e)
# else:
#     print("它是1位数:",f)


'''66.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同'''
# num = int(input("输入一个5位正整数:"))
# a = str(num)
# flag = 1
# for i in range(len(a)//2):
#     if a[i] != a[-i-1]:
#         flag = 0
#         break
# if flag == 0:
#     print("%d不是回文数" %num)
# else:
#     print("%d是回文数" %num)


'''67.按逗号分隔列表'''
# a = [1,2,3,4]
# b = ','.join(str(n) for n in a)
# print(b)

#字符串转换为列表
# l = '1,2,3'
# m = l.split(',')
# print(m)


'''68.对10个数进行排序'''
#方法1.
# list = []
# for i in range(3):
#     a = input("请输入整数:")
#     list.append(a)
# print(list)
# list.sort()
# for i in list[:-1]:        #通过循环进行输出
#     print(i,end=',')
# print(list[-1])
# print(sorted(list))

#方法2.冒泡法
# ls = list(map(int,input("请输入10个数，以逗号分隔:").split(',')))
# print(ls)
#
# for i in range(0,9):
#     for j in range(0,9-i):
#         if ls[j] > ls[j+1]:
#             ls[j],ls[j+1] = ls[j+1],ls[j]
# print(ls)


'''69.求一个3*3矩阵主对角线元素之和'''
# a = []
# sum = 0
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(input("请输入整数:"))
# for i in range(3):
#     for j in range(3):
#         print(a[i][j],end=' ')
#     print()
#     sum += int(a[i][i])
# print("对角线之和:",sum)


'''70.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。'''
# def sort1(ls):
#     ls.sort()
#     return ls
#
# def sort2(ls):
#     for i in range(len(ls)):
#         for j in range(i):
#             if ls[i] < ls[j]:
#                 ls[i],ls[j] = ls[j],ls[i]
#     return ls
#
# if __name__ == '__main__':
#     a = [1,2,4,5,6,8]
#     n = int(input("请输入插入的数:"))
#     a.append(n)
#     print(a)
#     l1 = sort1(a)
#     l2 = sort2(a)
#     print(l1)
#     print(l2)


'''71.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵'''
# x = [[12,7,3],
#      [4,5,6],
#      [7,8,9]]
# y = [[5,8,1],
#      [6,7,3],
#      [4,5,9]]
# result = [[0,0,0],
#           [0,0,0],
#           [0,0,0]]
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j] = x[i][j] + y[i][j]
# for r in result:
#     print(r)

'''72.求输入数字的平方，如果平方运算后小于 50 则退出。'''
# def sq(x):
#     return x*x
# print("如果结果小于50，程序停止运行")
# again = True
# while again:
#     num = int(input("请输入一个数:"))
#     print("运算结果为:",sq(num))
#     if sq(num) > 50:
#         again = True
#     else:
#         again = False


'''73.取一个整数a从右端开始的4〜7位'''
# num = input("请输入不少于7位数的整数:")
# print(num[-7:-3])


'''74.打印杨辉三角（前10行)'''
#方法一
# num = input("请输入行数:")
# num = int(num)

# list1 = []  #保存杨辉三角
# for n in range(num):
#     row = [1]   #保存行
#     list1.append(row)

#     if n==0:
#         print(row)
#         continue
#     for m in range(1,n):
#         row.append(list1[n - 1][m - 1] + list1[n - 1][m])
#     row.append(1)
#     print(row)


#方法二
# a = []
# for i in range(10):
# 	a.append([])
# 	for j in range(10):
# 		a[i].append(0)
# for i in range(10):
# 	a[i][0] = 1
# 	a[i][i] = 1
# for i in range(2,10):
# 	for j in range(1,i):
# 		a[i][j] = a[i-1][j-1] + a[i-1][j]
# for i in range(10):
# 	for j in range(i+1):
# 		print(a[i][j],end = ' ')
# 	print()



'''75.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组'''
#方法一
# a = list(map(int,input("请输入6个整数，以逗号分隔:").split(',')))
# print(a)
# max = 0
# min = 0
# for i in range(0,len(a)-1):
# 	if a[max] < a[i]:
# 		max = i
# 	if a[min] > a[i]:
# 		min = i
# a[0],a[max] = a[max],a[0]
# a[5],a[min] = a[min],a[5]
# print(a)

#方法二、函数法
# def inp(a):
# 	for i in range(6):
# 		a.append(int(input("请输入整数:")))

# def arry_min(arry):
# 	min = 0
# 	for i in range(0,len(arry)-1):
# 		if arry[min] > arry[i]:
# 			min = i
# 	arry[5],arry[min] = arry[min],arry[5]

# def arry_max(arry):
# 	max = 0
# 	for i in range(0,len(arry)-1):
# 		if arry[max] < arry[i]:
# 			max = i
# 	arry[0],arry[max] = arry[max],arry[0]

# def outp(a):
# 	for i in range(len(a)):
# 		print(a[i],end = ' ')

# if __name__ =='__main__':
# 	arry = []
# 	inp(arry)
# 	arry_max(arry)
# 	arry_min(arry)
# 	outp(arry)



'''76.有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数'''
m = int(input("请输入后移的位数:"))
numbers = list(map(int,input("请输入整数并以逗号分隔:").split(',')))
a = numbers[-m:] + numbers[0:len(numbers)-m]
print(a)

