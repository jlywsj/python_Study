# 石头(1)、剪刀(2)、布(3)

# 用int把input的数字转换为整数
# 类型转换
player = int(input("请输入您要出的拳 石头(1)/剪刀(2)/布(3)：\n"))

# 假设电脑只会石头
computer = 1

# print("玩家选择的拳头是 %d - 电脑出的拳头是 %d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜利！")
elif player == computer:
    print("平局！")
else:
    print("电脑胜利~")
