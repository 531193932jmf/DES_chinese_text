from S_box import *
def read_file_txt(filename):
    try:
        fp = open(filename,"r",encoding='utf-8')
        message = fp.read()
        fp.close()
        return message
    except:
        print("Open file error!")
def char2bin(char):
    # 返回一个（ASCII）字符的8位二进制表示
    b = bin(ord(char)).replace('0b', '')
    space = 8 - len(b)
    return '0' * space + b
#生成密钥，用户输入，最好为字母。
def process_key(text="qwerasdf"):
    key_bits = ""
    key=text
    for i in key:
        count = 0
        asc2i = bin(ord(i))[2:]
        '''将每一个ascii均补齐7位,第8位作为奇偶效验位'''
        for j in asc2i:
            count += int(j)
        if count % 2 == 0:
            asc2i += '0'
        else:
            asc2i += '1'
        for j in range(7-len(asc2i)):
            asc2i = '0' + asc2i
        key_bits += asc2i
    if len(key_bits) > 64:
        return [int(number) for number in key_bits[0:64]]
    else:
        for i in range(64-len(key_bits)):
            key_bits += '0'
        return [int(number) for number in key_bits]
    # if len(text) != 8:
    #     return False
    # temp = [char2bin(char) for char in text]
    # return [int(number) for number in ''.join(temp)]
#字符串to二进制，中文字符串。
def str_2_bit( message ):
    bits = ""
    for i in message:
        asc2i = bin(ord(i))[2:] #bin将十进制数转二进制返回带有0b的01字符串
        '''为了统一每一个字符的01bit串位数相同，将每一个均补齐8位'''
        for j in range(16-len(asc2i)):
            # if len(asc2i)==8:
            #     break
            asc2i = '0' + asc2i
        bits += asc2i
    return bits
# a=str_2_bit("物")
# print(a)
# print(len(a))
def dec2bin4(dec):
    return '{:04b}'.format(dec)
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 15, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
S_box = [S1, S2, S3, S4, S5, S6, S7, S8]
def s_box_change(text):
    result = []
    for i in range(0, 8):
        temp = text[i*6:(i+1)*6]
        xx = int(str(temp[0])+str(temp[-1]), 2)
        yy = int(str(temp[1])+str(temp[2])+str(temp[3])+str(temp[4]), 2)
        message = S_box[i][xx][yy]
        result.append(dec2bin4(message))
    return [int(x) for x in ''.join(result)]
def xor(m, n):
    # M=[]
    # N=[]
    # for i in m:
    #     M.append(int(i))
    # for i in n:
    #     N.append(int(i))
    return [a ^ b for a, b in zip(m, n)]
def E_extend(text):
    E = [32, 1, 2, 3, 4, 5,
         4, 5, 6, 7, 8, 9,
         8, 9, 10, 11, 12, 13,
         12, 13, 14, 15, 16, 17,
         16, 17, 18, 19, 20, 21,
         20, 21, 22, 23, 24, 25,
         24, 25, 26, 27, 28, 29,
         28, 29, 30, 31, 32, 1]
    return [text[E[i] - 1] for i in range(48)]
def str_shift(stri,shift,direction=0):
    res=[0]*len(stri)
    if direction==0:#默认左移
        index=list(range(len(stri)))
        for i in range(len(stri)):
            index[i]=(i+len(stri)-shift) % len(stri)
        for i in range(len(stri)):
            # print(index[i])
            res[index[i]]=stri[i]
    else:
        index = list(range(len(stri)))
        for i in range(len(stri)):
            index[i] = (i + len(stri) + shift) % len(stri)
        for i in range(len(stri)):
            res[index[i]] = stri[i]
    # print("".join(res))
    return res
# a=str_shift("1101",1)
# print(a)
# a='1234'
# b=[0]*4
# for i in range(4):
#     b[i]=int(a[i])
# print(int("1")^2)
# print(b)
# import numpy as np
# E_Ri=np.array([1,0,1,1,0,1,0,0]).reshape(8,1)
# s_in2=np.array([1,1,1,1,1,0,0,0]).reshape(8,1)
# E_Ri=E_Ri.astype('int32')
# s_in2 = s_in2.astype('int32')
# s_in=np.zeros((8,1))
# for i in range(8):
#     for j in range(1):
#         s_in[i,j]=E_Ri[i,j]^s_in2[i,j]
# s_in=s_in.astype("int32")
# print(type(s_in[0,0]),type(s_in))
#
# text="1"*64
# s_box_change(text)