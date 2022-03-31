import numpy as np
from Hexadecimal_conversion import *
from S_box import S_box,IP,Ls_Rs
from Pretreatment import *
#IP为一维列表，s盒子为二维列表。
def data_2_bits(file_name,mode=0):
    #加密字符串，返回2进制比特流。
    if mode!=0:#filename 是直接转换的文本
        return str_2_bit(file_name)
    message=read_file_txt(file_name)
    # print(message)
    bits=str_2_bit(message)#从下标0开始
    return bits
        # a=str(data[0]) + str(data[0 + 1]) + str(data[0 + 2]) + str(data[0 + 3])
        # print(a)
        # for i in range(0, len(data), 4):
        #     data_64bit_list.append(hex2bin(str(data[i]))+
        #                            hex2bin(str(data[i + 1]))
        #                            + hex2bin(str(data[i + 2])) +
        #                            hex2bin(str(data[i + 3])))
        # print(len(data_64bit_list), data_64bit_list[0], type(data_64bit_list[0]))
    # return data_64bit_list  #64为二进制为元素的数组，元素为字符串类型
def divide(bits):
    #bits : str
    bits64_list=[]
    last=0
    rest=0
    for i in range(0,len(bits),64):
        if len(bits)-i<64:
            rest=len(bits)-i
            last=int(len(bits)/64)
        bits64_list.append(bits[i:i+64])
    if rest!=0:
        last_bits=bits[64*last:]
        for j in range(64-rest):
            bits64_list[-1]="0"+bits64_list[-1]
    # bits64_list.append(last_bits)
    return bits64_list
def check_divide(bits64_list):
    for i in bits64_list:
        if len(i)==64:
            continue
        else:return False
    return True
#初始置换IP
def Initial_Permutation(data_64bits):
    # data_64bits 为str类型的
    # IP = [58, 50, 42, 34, 26, 18, 10, 2,
    #       60, 52, 44, 36, 28, 20, 12, 4,
    #       62, 54, 46, 38, 30, 22, 14, 6,
    #       64, 56, 48, 40, 32, 24, 16, 8,
    #       57, 49, 41, 33, 25, 17, 9, 1,
    #       59, 51, 43, 35, 27, 19, 11, 3,
    #       61, 53, 45, 37, 29, 21, 13, 5,
    #       63, 55, 47, 39, 31, 23, 15, 7]
    ip=IP()
    Ip=ip.ip
    return [data_64bits[Ip[i] - 1] for i in range(64)]
#初始逆置换IP_1
def Initial_Permutation_1(data_64bits):
    # data_64bits 为str类型的
    INVERSE_IP = [40, 8, 48, 16, 56, 24, 64, 32,
                  39, 7, 47, 15, 55, 23, 63, 31,
                  38, 6, 46, 14, 54, 22, 62, 30,
                  37, 5, 45, 13, 53, 21, 61, 29,
                  36, 4, 44, 12, 52, 20, 60, 28,
                  35, 3, 43, 11, 51, 19, 59, 27,
                  34, 2, 42, 10, 50, 18, 58, 26,
                  33, 1, 41, 9, 49, 17, 57, 25]
    ip=IP()
    # INVERSE_IP=ip.ip_1
    return [data_64bits[INVERSE_IP[i] - 1] for i in range(64)]
#f函数
def f_add_xor(r:str,subkeysi):#返回字符串
    r_extend = E_extend(r)  # 对右半部分进行E扩展运算，转换成48位对串
    xor1 = xor(r_extend, subkeysi)  # 对得到对48位串与48位对子密钥进行异或运算
    s_box_result = s_box_change(xor1)  # 异或得到对结果进行S盒转换
    p_box_result = P_Permutation(s_box_result)
    return p_box_result
    #改这里的异或？
    # Ri_num=[]
    # for i in Ri:
    #     Ri_num.append(int(i))
    # Ri = Ri_num
    # temp=np.array(Ri_num)
    # temp=temp.reshape((8,4))
    # L_temp=[Ri[31],Ri[4-1],Ri[8-1],Ri[12-1],
    #         Ri[16-1],Ri[20-1],Ri[24-1],Ri[28-1]]
    # R_temp = [Ri[4], Ri[8], Ri[12], Ri[16],
    #           Ri[20], Ri[24], Ri[28], Ri[0]]
    # L_temp=np.array(L_temp).reshape((8,1))
    # R_temp = np.array(R_temp).reshape((8, 1))
    # E_Ri=np.hstack((L_temp,temp,R_temp))#48 8x6,了
    #E扩展
    # E_Ri=E_extend(Ri)
    # print("E_ri",E_Ri)
    # s_in1=[0]*len(keys)
    # for i in range(len(keys)):
    #     s_in1[i]=int(keys[i])#把keyi的字符变数字
    # s_in2=np.array(s_in1).reshape(8,6)
    # E_Ri=E_Ri.astype('int32')
    # print(E_Ri)
    # s_in2 = s_in2.astype('int32')
    # s_in=np.zeros((8,6))
    # for i in range(8):
    #     for j in range(6):
    #         s_in[i,j]=E_Ri[i,j]^s_in2[i,j]
    # print(E_Ri[0,0],s_in2[0,0],s_in[0,0])
    # s_in = s_in.astype("int32")
    # print("keysss:","".join(keys))
    # print("sss",s_in)
    # for i in range(16):
    #     l, r = text[:32], text[32:]
    #     r_extend = E_extend(r)  # 对右半部分进行E扩展运算，转换成48位对串
    #     xor1 = xor(r_extend, keys[i])  # 对得到对48位串与48位对子密钥进行异或运算
    #     s_box_result = s_box_change(xor1)  # 异或得到对结果进行S盒转换
    #     p_box_result = P_Permutation(s_box_result)  # p置换，得到轮函数的输出
    #     xor2 = xor(l, p_box_result)  # 将左半部分与轮函数输出做异或，得到新串对右半部分
    #     text = r + xor2  # 左右部分结合，形成新串
    # text = text[32:] + text[:32]
    # print(InvereIpTable(text))
    # 将二进制密文串返回
    # return Initial_Permutation_1(text)
    # s_box=S_box()
    # s_out=[]
    # s=[s_box.s1,
    #    s_box.s2,
    #    s_box.s3,
    #    s_box.s4,
    #    s_box.s5,
    #    s_box.s6,
    #    s_box.s7,
    #    s_box.s8,
    #    ]
    # for i in range(8):
    #     xy=s_in[0,:]
    #     x = 2*xy[0]+xy[5]
    #     y=xy[1]*8 + xy[2]*4+xy[3]*2+xy[4]*1
    #     t=s[i][x][y]
    #     s_out.append(bin(t)[2:])#二进制，去掉ob
    # for i in range(len(s_out)):
    #     full4=s_out[i]
    #     for j in range(4-len(full4)):
    #         full4='0'+full4
    #     s_out[i]=full4
    # s_out="".join(s_out)#32bits
    # # print("s_out",s_out,'\t',len(s_out))
    # p_out=P_Permutation(s_out)
    # # print("p_out",p_out)
    # return p_out
# 异或，两个字符串的
def xor_str(Li,Fi):#返回字符串
    res=[0]*32
    for i in range(32):
        if (Li[i]==Fi[i]):
            res[i]="0"
        else:res[i]="1"
    return "".join(res)
#P_置换，S盒子
def P_Permutation(M):
    P = [16, 7, 20, 21, 29, 12, 28, 17,
         1, 15, 23, 26, 5, 18, 31, 10,
         2, 8, 24, 14, 32, 27, 3, 9,
         19, 13, 30, 6, 22, 11, 4, 25]
    return [M[P[i] - 1] for i in range(32)]
def gen_son_keys_decode(keys:str):
    ip = Ls_Rs()
    PC_1 = ip.pc_1
    PC_2 = ip.pc_2
    result = []
    key56 = [keys[PC_1[i] - 1] for i in range(56)]  # 对56个非校验位进行PC_1置换
    step = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  # 移动的步长
    for i in range(16):
        key_left = str_shift(key56[:28], step[i])
        key_right = str_shift(key56[28:], step[i])
        key56 = key_left + key_right
        key48 = [key56[PC_2[i] - 1] for i in range(48)]
        result.append(key48)
    return result[::-1]
    # son_keys = []
    # ls_rs = Ls_Rs()
    # rs = ls_rs.Rs  # 解密时用的。
    # pc1 = ls_rs.pc_1
    # pc2 = ls_rs.pc_2
    # keyis = []  # 和son_keys一样，只不过元素是字符串
    #     # 密钥置换pc1
    # res = [0] * 56
    # for j in range(56):
    #     res[j] = keys[pc1[j] - 1]
    # # 分成左右两部分
    # res = "".join(res)  # 转换为字符串,56
    # keyis.append(res)
    # for i in range(16):  # 16轮迭代
    #     res = keyis[-1]
    #     temp_l = res[:28]
    #     temp_r = res[28:]
    #     temp_r2 = str_shift(temp_r, rs[i], 1)
    #     temp_l2 = str_shift(temp_l, rs[i], 1)
    #     # print("Ci:")
    #     # print(temp_l)
    #     # print(temp_l2)
    #     # print("\n")
    #     temp = temp_l2 + temp_r2
    #     # print(temp)
    #     keyis.append(temp)
    #     res = [0] * 48
    #     for j in range(48):
    #         res[j] = temp[pc2[j] - 1]
    #     son_keys.append(res)
    # # print("decode's",son_keys[2])
    #     # k1,k2,...,k15。
    # return son_keys
def gen_son_keys(keys:str):#mode==0为加密
    # son_keys=[]
    # ls_rs=Ls_Rs()
    # ls=ls_rs.LS#加密时用的
    # pc1=ls_rs.pc_1
    # pc2=ls_rs.pc_2
    # keyis=[]#和son_keys一样，只不过元素是字符串
    # #密钥置换pc1
    # res = [0] * 56
    # for j in range(56):
    #     res[j] = keys[pc1[j] - 1]
    # #分成左右两部分
    # res="".join(res)#转换为字符串,56
    # keyis.append(res)
    # for i in range(16):  # 16轮迭代
    #     res=keyis[-1]
    #     temp_l=res[:28]
    #     temp_r=res[28:]
    #     #两部分分别向左移位
    #     temp_r2=str_shift(temp_r,ls[i])
    #     temp_l2=str_shift(temp_l,ls[i])
    #     # print("Ci:")
    #     # print(temp_l)
    #     # print(temp_l2)
    #     # print("\n")
    #     #拼接一起
    #     temp=temp_l2+temp_r2
    #     keyis.append(temp)
    #     #pc2
    #     res = [0] * 48
    #     for j in range(48):
    #         res[j] = temp[pc2[j] - 1]
    #         #res是列表类型
    #     son_keys.append(res)#共生成16个子密钥
    # # print("encode's", son_keys[-3])
    # return son_keys
    ip=Ls_Rs()
    PC_1=ip.pc_1
    PC_2=ip.pc_2
    result = []
    key56 = [keys[PC_1[i] - 1] for i in range(56)]  # 对56个非校验位进行PC_1置换
    step = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]  # 移动的步长
    for i in range(16):
        key_left = str_shift(key56[:28], step[i])
        key_right = str_shift(key56[28:], step[i])
        key56 = key_left + key_right
        key48 = [key56[PC_2[i] - 1] for i in range(48)]
        result.append(key48)
    return result
def Decode(bits64:list,key="qwerasdf"):
    for i in range(64-len(bits64)):#不足64也处理一下。
        bits64="0"+bits64
    keys = process_key(key)  # 获得64位密钥
    son_keys = gen_son_keys_decode(keys)
    text = []
    for i in bits64:
        text.append(int(i))
    text = Initial_Permutation(text)
    for i in range(16):
        l, r = text[:32], text[32:]
        p_box_result = f_add_xor(r, son_keys[i])
        xor2 = xor(l, p_box_result)  # 将左半部分与轮函数输出做异或，得到新串对右半部分
        text = r + xor2  # 左右部分结合，形成新串
    text = text[32:] + text[:32]
    res = Initial_Permutation_1(text)
    return res
def Encrypt(bits64:str,key="qwerasdf"):
    for i in range(64-len(bits64)):
        bits64="0"+bits64
    # 1获得子密钥
    keys = process_key(key)#获得64位密钥
    son_keys=gen_son_keys(keys)
    text=[]
    for i in bits64:
        text.append(int(i))
    text=Initial_Permutation(text)
    # print(son_keys[-1])
    #2, 初始置换
    # IP_out = Initial_Permutation(bits64)
    # print("en ", bits64)
    # print("en ", IP_out)
    #3，16轮迭代加密
    # R_i=[0]*17
    # R_i[0]=IP_out[32:]
    # L_i=[0]*17
    # L_i[0]=IP_out[:32]
    # for i in range(1,17):
        #第i轮的替换与迭代
        # L_i[i]=R_i[i-1]
        #f(R:str,keys:list1)
        # f_data = f(R_i[i - 1], son_keys[i - 1])
        # print("f_data",f_data)
        # print("L_i[i-1]",L_i[i-1])
        # # f(R:str,keys:list1)
        # R_i[i] = xor_str(L_i[i - 1], f_data)
        # print("R_i[i]",R_i[i])
        # print("key:","".join(son_keys[i-1]))
        # print("R[i]:",R_i[i])
        # print("L[i]:",L_i[i])
    # res=L_i[16]+R_i[16]
    #4,初始逆置换
    # print("res:",res)
    # result=Initial_Permutation_1(res)
    # print("result",result)
    for i in range(16):
        l, r = text[:32], text[32:]
        f_result=f_add_xor(r,son_keys[i])
        xor2 = xor(l, f_result)  # 将左半部分与轮函数输出做异或，得到新串对右半部分
        text = r + xor2  # 左右部分结合，形成新串
    text = text[32:] + text[:32]
    res=Initial_Permutation_1(text)
    return res
def text_single_group(bits64_stream:str,key="qwerasdf"):
    c = Encrypt(bits64_stream,key)
    # chinese_c=bits_2_str_chinese(list_2_str(c))
    # print(type(c), c)
    print("明文:", bits64_stream)
    print("密文:", list_2_str(c), bits_2_str_chinese(list_2_str(c)).replace(" ",""))
    m = Decode(c,key)
    # chinese_m=bits_2_str_chinese(list_2_str(m))
    print("解密:", list_2_str(m), bits_2_str_chinese(list_2_str(m)).replace(" ",""))
    bit_stream_tuple=(bits64_stream,list_2_str(c),list_2_str(m))
    chinese_tuple=(bits_2_str_chinese(list_2_str(c)).replace(" ",""),bits_2_str_chinese(list_2_str(m)).replace(" ",""))
    res=[]
    res.append(bit_stream_tuple)
    res.append(chinese_tuple)
    return res
def main_text(data,mode=0,key="qwerasdf"):
    with open(data,"r",encoding="utf8") as file:
        data_text=file.read()
    print("原文本内容:\n",data_text)
    if mode!=0:
        data_bits=data_2_bits(data,1)
    else:
        data_bits = data_2_bits(data)
    print("比特流信息:", data_bits, '\n', type(data_bits))
    print("比特流长度：", len(data_bits))
    bits_64_list = divide(data_bits)
    # print(type(bits_64_list[0])) #:str
    boolen=check_divide(bits_64_list)
    if boolen==False:
        print("对不起，分组失败")
        return
    total_bits_c=""
    total_bits_m = ""
    total_chines_c = ""
    total_chines_m = ""
    res=[]
    i=1
    for group in bits_64_list:
        print("第",i,"组:")
        i+=1
        temp=text_single_group(group,key)
        res.append(temp)
    result_miwen=""
    result_jiemi=""
    for temp in res:
        result_miwen += temp[1][0]
        result_jiemi += temp[1][1]
    return (result_miwen,result_jiemi)
    # print("\n\n")
    # for i in bits_64_list:
        # print(len(i))
    # print(check_divide(bits_64_list))
    # print(type(bits_64_list[0]))
if __name__=="__main__":
    key="asdfghjk"#密钥文本
    miwen,jiemi=main_text("test",key=key)#有其他参数使用关键字传参
    print("密文为：\n",miwen)
    print("解密为：\n",jiemi)
    # with open("ciphertext.txt","w",encoding="utf8") as file:
    #     file.write(miwen)
    # 1,读取数据
    # 2,分组
    # a=['1']*64
    # a=''.join(a)
    # print(a)
    # b=Encrypt(a)
    # print(list_2_str(b))
    # print(list_2_str(Decode(b)))
    # 3,初始置换
    # first=Initial_Permutation(bits_64_list[-1])
    # print(first)
    # print(bits_64_list[1][42],first[2])
    #获得密钥
    # keys=process_key()
    # print(type(keys))
    # a=np.array([1,2,3,4]).reshape((4,1))
    # b = np.array([1, 0, 0, 1]).reshape((4, 1))
    # c = np.array([1, 1,0, 1,1,0,0,1]).reshape((4, 2))
    # d=np.hstack((a,c,b))
    # print(d)
    # xy = d[0, :]
    # x =bin (xy[1]*2+xy[2])[2:]
    # y=bin (xy[1]*2+xy[0])[2:]
    # print(x,y)
    # print("".join([x,y]))
    # print(type(x))














