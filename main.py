'''牛排=200
猪排=500
套餐=100
点餐=input("请问你要点什么餐？（A）牛排（B）猪排").upper()
升级=input('请问你是否选择升级套餐（Y）是（N）否').upper()
if 点餐=="A":
    if 升级=='Y':
        print(f"你的点餐费用共是{牛排+套餐}元")
    else:
        print(f"你的点餐费用共是{牛排}元")
else:
    if 升级 == 'Y':
        print(f"你的点餐费用共是{猪排+套餐}元")
    else:
        print (f"你的点餐费用共是{猪排}元")
print('欢迎下次光临！')
if 点餐=="A" and 升级=='Y':
    print(f'你的餐费是{牛排+套餐}元')
elif 点餐=='A' and 升级=='N':
    print(f'你的餐费是{牛排}')
elif 点餐=='B' and 升级=='Y':
    print(f'你的餐费是{猪排+套餐}元')
else :
    print(f'你的餐费是{猪排}')'''
import random
from os import times_result

#from itertools import count

#student =['小虎',90,'小明',88,'小王',92,'小赵',100]
#日期='2002/02/02'
#student[1]='xiaoming'
#student.pop(1 )
#print(student.index('小王'))
'''操作 =input('请输入操作指令（A）查询(B)增加(C)删除（D）修改：').upper()
if  操作=='A':
    姓名=input('请输入要查询的姓名：')
    if 姓名 not in student:
        print('查无此人')
    else:
        顺位=student.index(姓名)
        print(f'{姓名}的成绩是：{student[顺位+1]}')
elif 操作=='B':
    学生资料=input('请输入你要增加的学生/成绩（中间以斜杠隔开）：')
    student.extend(学生资料.split('/'))
    print('学生成绩新增已完成。')
    print(f'目前已登记的学生人数为：{int(len(student)/2)}人')#int(len(student)/2)=len(student)//2
elif 操作=='C':
     姓名=input('请输入你要删除的姓名：')
     顺位=student.index(姓名)
     student.pop(顺位)
     student.pop(顺位)
     print(student)
elif 操作=='D':
     姓名 = input('请输入同学的姓名：')
     成绩 = input('请输入你要修改的成：”')
     姓名位置=student.index(姓名)
     student[姓名位置+1]=成绩
     print(student)'''
#早餐 = ['汉堡','三明治','热狗','饭团']
'''饮品 = ['豆浆','牛奶','绿豆杨']
数量 = 0
for 餐点 in 早餐:
    for 喝的 in 饮品:
        print(f"{餐点}配{喝的}")
        数量 += 1
print(f"一共有{数量}种搭配")'''
'''数据=[-1,2,-3,4,-5,6,-7]
正数=[]
负数=[]
for 数字 in 数据:
    if 数字 > 0:
        正数.append(数字)
    else:
        负数.append(数字)
print(f'正值的数字包括{正数}')
print(f'负值的数字包括{负数}')'''
'''正确密码=123456
for 次数 in range(5):
    密码=int(input('请输入正确密码：'))
    if 密码== (正确密码):
        print('密码正确。')
        break
    elif 密码 != 正确密码 and 次数 < 4:
        #print('密码错误，请重新输入')
        print(f'密码错误，请重新输入，您还剩下{4-次数}次机会')
    else :
        print('您输入太多次错误密码，账户已锁定')'''
'''商品金额=1000
玩家A=input('请输入玩家A的姓名')
玩家B=input('请输入玩家B的姓名')
回答次数=1
回答总数=3
while 回答次数<=回答总数:
    A作答=int(input(f'请{玩家A}输入金额'))
    B作答=int(input(f'请{玩家B}输入金额'))
    if A作答==1000:
        print(f'{玩家A}回答正确，获得胜利！')
        break
    elif B作答==1000:
        print(f'{玩家B}回答正确，获得胜利！')
        break
    elif abs(商品金额-A作答)<abs(商品金额-B作答):
        print(f'{玩家A}回答最为接近')
    else :
        print(f'{玩家B}回答最为接近')
    回答次数 +=1
if abs(商品金额-A作答)<abs(商品金额-B作答):
        print(f'游戏结束，{玩家A}的回答最为接近，{玩家A}获胜')
else :
        print(f'游戏结束，{玩家B}的回答最为接近，{玩家B}获胜') '''

'''def 加法(x,y):
    return x+y
def 减法(x,y):
   return x-y
def 乘法(x,y):
    return x*y
def 除法(x,y):
    商数=x//y
    余数=x%y
    return 商数,余数
while True:
    计算类型=input('请选择计算类型（1）加法（2）减法（3）乘法（4）除法，或者输入其它任何字符退出。')
    if 计算类型 in('1','2','3','4'):
        数字1=int(input('请输入第一个数字'))
        数字2=int(input('请输入第一个数字'))
        if 计算类型=='1':
            print(f'{数字1}+{数字2}={加法(数字1,数字2)}')
        elif 计算类型=='2':
            print(f'{数字1}-{数字2}={减法(数字1,数字2)}')
        elif 计算类型=='3':
            print(f'{数字1}*{数字2}={乘法(数字1, 数字2)}')
        elif 计算类型=='4':
            if 数字1 % 数字2==0:
                print(f'{数字1}%{数字2}={除法(数字1,数字2)[0]}')
            else :
                print(f'{数字1}%{数字2}={除法(数字1,数字2)[0]}余数{除法(数字1,数字2)[1]}')
    else:
        print('拜拜')
        break'''
'''手机1={'厂牌':'苹果',
     '型号':'iphon 14',
      '颜色':['黑色','银色'],
      '容量':'512 GB'
      }
手机2={'厂牌':'小米',
     '型号':'小米14',
      '颜色':['黑色','白色'],
      '容量':'512 GB'
      }
手机3={'厂牌':'vivo',
     '型号':'vivo x200pro',
      '颜色':['黑色','红色','白色'],
      '容量':'512 GB'
      }
库存=[手机1,手机2,手机3]
查询=input('请输入要查询的手机厂牌')
if 查询 in str(库存):
    for 手机 in 库存:
        if 手机['厂牌']==查询:
            print(f'{查询}手机有库存，型号为{手机['型号']}，颜色有{手机['颜色']}，容量为{手机['容量']}')

else:
    print('暂无库存')'''

'''import random
import string
数字=string.digits
字母=string.ascii_letters
字母表=list(数字+字母)
random.shuffle(字母表)
长度=int(input(f'请输入你想要的密码长度：'))
密码=''.join(字母表[:长度])
print(f'密码为{密码}')'''

'''import requests
城市=input(f'请输入要查询的城市：')
api='ca8a02be8f7a939c0112435824242573'
网址=f'https://api.openweathermap.org/data/2.5/weather?q={城市}&appid={api}'
天气资料=requests.get(网址)
气温=int(天气资料.json()['main']['temp']-273.15)
print(f'{城市}今天的气温是{气温}度')'''

import random
class 游戏角色:
    生命值 = 500
    攻击力 = 200
    def __init__(self,姓名):
        self.姓名=姓名
    def 防御(self,指令):
        if 指令==1:
            print(f'{self.姓名}使用了格挡')
            return 0.5
        elif 指令==2:
         print(f'{self.姓名}尝试使用闪避')
        return random.choice([0,1])
class 战士(游戏角色):
    def 攻击(self,指令):
        if 指令==1:
            print(f'{self.姓名}使用了突刺攻击')
            return 200
        elif 指令==2:
            print(f'{self.姓名}尝试使用特殊攻击')
            return random.choice([100,300])
class 怪兽(游戏角色):
    def 攻击(self,指令):
        if 指令==1:
            print(f'{self.姓名}使用了利爪攻击')
            return 200
        elif 指令==2:
            print(f'{self.姓名}尝试使用毒液攻击')
            return random.choice([150,350])
玩家姓名 = input('请玩家创建角色姓名')
玩家 = 战士(玩家姓名)
敌方 = 怪兽('哥布林')
随机 =random.choice([1,2])
while True:
    攻击指令=int(input('请输入您的攻击指令（1）普通攻击（2）特殊攻击：'))
    玩家攻击力=玩家.攻击(攻击指令)
    损血量=int(敌方.防御(随机)*玩家攻击力)
    敌方.生命值 -= 损血量
    if 敌方.生命值 <=0:
        print(f'{敌方.姓名}倒下了，{玩家.姓名}胜利！！')
        break
    else:
        print(f'{敌方.姓名}受到{损血量}点攻击，剩余血量为{敌方.生命值}。')
        print('')

    防御指令 = int(input('请输入您的防御指令（1）格挡（2）闪避：'))
    敌方攻击力 = 敌方.攻击(随机)
    损血量 = int(玩家.防御(防御指令)*敌方攻击力)
    玩家.生命值 -= 损血量
    if 玩家.生命值 <= 0:
        print(f'{玩家.姓名}倒下了，{敌方.姓名}胜利！！')
        break
    else:
        print(f'{玩家.姓名}受到{损血量}点攻击，剩余血量为{玩家.生命值}。')
        print('')





