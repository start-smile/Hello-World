import random
import sys

print("lifalong")
var = 42
print(var)

#字符串分片
string = "wo shi li fa long"
print(string[0])
print(string[1:])
print(string[:1])
print(string[3:6])
print(string[-1])

Name = "li\
falong"
print(Name)

OtherName = Name.replace(Name[:1], 'Y'*2)
print(OtherName)

#CityName = input("Please enter City Name:")
#url = "CityName:{0}".format(CityName)
#print(url)
#缩进的语句块表示语句的逻辑cunshu关系
def funcion():
    return "lifalong"
print(funcion())
len(funcion())

print(type(var))
print(type(str(var)))


#关键字和函数 关键字都为斜体函数为竖直体

#函数参数传递的方式有两种：位置传参、关键此传参

def calc(L, B, H):
    return (L+B)*H

print(calc(1, 2, 3))#位置传参
L = 3
B = 2
H = 1
print(calc(H, B, L))#位置传参
print(calc(H=3, L=1, B=2))#关键词传参

#sDir = __file__
#sDir = sDir[-len(__name__):]
#file = open(sDir+"/1.txt", 'w')
#file.write("wo shi lifalong")

#成员运算符 in   归属运算符  is
List = ["lifalong", "Gansu", 1986]

bResult = "lifalong" in List
print(bResult)

print(List[0])
print(List[-1])

def test():
    print("test")

print(test())

#布尔运算符 not and or
bTest1 = True or False
bTest2 = True and False
print(bTest1)
print(bTest2)
print(not bTest1)

#条件语句
#后面为语句块的必须在前面使用：进行标示
def conditionFunc(bCon):
    if bCon:
        print("bCon:", bCon)
    else:
        print("lifalong")

conditionFunc(True)
conditionFunc(False)

#循环语句
def print1_10():
    for i in range(1, 10):
        print(i)

print1_10()

pt1 = random.randrange(1, 7)
pt2 = random.randrange(1, 7)
pt3 = random.randrange(1, 7)

print(pt1, pt2, pt3)

#python 拥有四大数据结构 列表 字典 元组 集合
#列表支持增删改查
ListTest = ["haha", 123, True]
print(ListTest)

#字典Key不能重复，不可修改,可以进行增删改
DirTest = {123:"haha", 123:"heihei", 456:90}
print(DirTest)

#元组成员不可修改，固定版本的列表
ArrTest = (":", 123)
print(ArrTest)

#集合,没有顺序不能通过索引访问，也不能修改，只能增删
ColTest = {1, 2, 3, 4}
ColTest.discard(2)
print(ColTest)
ColTest.add(5)
print(4 in ColTest)


letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3]
r1 = zip(letters, numbers)
r2 = enumerate(letters)
print(type(r1))
print(type(r2))


#python 类属性 对象属性
class OneClass:
    trib = ["kaka", "haha", 123]
    def func1(self):
        print("First Function")
    def func2(self):
        print("Second Function")

OneClassObject = OneClass()
print(OneClassObject.trib)
OneClassObject.func1()
OneClassObject.func2()

class CocaCola:
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))
    def drink(self):
        print('Energy!')
coke = CocaCola()

class Class1:
    a = 1
object = Class1()
Class1.a = 32
print(object.a)
print(Class1.__dict__)
print(object.__dict__)

class Class3(Class1):
    a = 1
    def __init__(self):
        self.a=42
object3 = Class3()
print(object3.a)
print(Class3.__dict__)
print(object3.__dict__)

print(sys.path)