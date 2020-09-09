"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
from random import randint
#定义战斗函数
def fight():
    #初始化我的血量
    my_hp = 1000
    #随机产生我的攻击力在199-201之间
    my_power = randint(199, 201)
    #初始化敌人的血量
    enemy_hp = 1000
    # 随机产生敌人的攻击力在199-201之间
    enemy_power = randint(199, 201)
    #打印查看我的攻击力
    print(my_power)
    # 打印查看敌人的攻击力
    print(enemy_power)

    while True:
        #我的最终血量
        my_hp = my_hp - enemy_power
        #敌人的最终血量
        enemy_hp = enemy_hp - my_power
        if my_hp>0:
           print(f"我还剩{my_hp}血量。")
        if my_hp<=0:
           print("我还剩0血量。")
           print("敌人赢了")
           break
        if enemy_hp > 0:
            print(f"敌人还剩{enemy_hp}血量。")
        if enemy_hp <= 0:
            print("敌人还剩0血量。")
            print("我赢了")
            break
#调用函数
fight()