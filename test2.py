from main import *

test="1"*64
print(test)

iptest=Initial_Permutation(test)
print(iptest)
keys = process_key("qwerasdf")#获得64位密钥
son_keys=gen_son_keys(keys)
for i in son_keys:
    print(i)
# text=test
# for i in range(16):
#     l, r = text[:32], text[32:]
#     r_extend = E_extend(r)  # 对右半部分进行E扩展运算，转换成48位对串
#     xor1 = xor(r_extend, son_keys[i])  # 对得到对48位串与48位对子密钥进行异或运算
#     s_box_result = s_box_change(xor1)  # 异或得到对结果进行S盒转换
#     p_box_result = P_Permutation(s_box_result)  # p置换，得到轮函数的输出
#     xor2 = xor(l, p_box_result)  # 将左半部分与轮函数输出做异或，得到新串对右半部分
#     Xor=[]
#     for i in xor2:
#         Xor.append(str(i))
#     text = r + "".join(Xor)  # 左右部分结合，形成新串
# text = text[32:] + text[:32]
#     # print(InvereIpTable(text))
#     # 将二进制密文串返回
#
#     #4,初始逆置换
# result=Initial_Permutation_1(text)
# print("result",result)

# 001 1011000100110101011111101100000000011101101011001000000001100
# 100110100001
#密文：0010111001001001100101001110011100110110000001001000001111000011
