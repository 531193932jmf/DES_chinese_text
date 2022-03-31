import os
import matplotlib.pyplot as plt
import cv2
from io import BytesIO
import base64
from main import *

def str_2_bit8( message ):#bit流:str
    bits = ""
    for i in message:
        asc2i = bin(ord(i))[2:] #bin将十进制数转二进制返回带有0b的01字符串
        '''为了统一每一个字符的01bit串位数相同，将每一个均补齐8位'''
        for j in range(8-len(asc2i)):
            # if len(asc2i)==8:
            #     break
            asc2i = '0' + asc2i
        bits += asc2i
    return bits
def bits8_2_strs_decode(bits:str):
    bits8_list = []
    if len(bits) % 8!=0:
        print("比特流转字节流失败！（不是8的倍数）")
        return
    for i in range(0, len(bits), 8):
        bits8_list.append(bits[i:i + 8])
    dec_list = []
    for i in bits8_list:
        dec = int(bin2dec(i))
        if dec==0:#不要0，即这基本属于填充的，这里去掉
            continue
        dec_list.append(chr(dec))
    return "".join(dec_list)

# 二进制读取图片,再将图片转为 base64 类型的字符串
def main_image(filename,count=5,mode=0):#mode>=10返回明文比特流，==0不返回，其余返回密文比特流
    with open(filename, 'rb') as fin:  # 第一个参数为图片全路径或相对路径
        # print('二进制类型')
        image_data = fin.read()
        # 图片:二进制类型
        # print(image_data)
    # print('二进制类型--转--bytes类型')
    base64_data_bytes = base64.b64encode(image_data)
    # 图片:bytes类型
    # print(base64_data_bytes)
    # print('bytes类型--转--str类型')
    base64_data_str = base64_data_bytes.decode()
    # 图片:str类型
    # print(base64_data_str)
    # print(type(base64_data_str))
    bits_stream_str = str_2_bit8(base64_data_str)#明文的比特流
    bits_stream_miwen=""
    if mode>=10:
        return bits_stream_str#明文比特流
    if mode!=0:
        per_groups=divide(bits_stream_str)
        print(len(bits_stream_str))
        i=1
        for per_group in per_groups:#per_group为二进制字符串
            print("第",i,"轮")
            i+=1
            bits_stream_miwen=bits_stream_str+list_2_str(Encrypt(per_group))
        return bits_stream_miwen
    print("二进制比特流大小",len(bits_stream_str),"共",int(len(bits_stream_str)/64)+1,"组")
    for i in range(1,count+1):
        c = Encrypt(bits_stream_str[(i-1)*64:64*i])
        m = Decode(c)
        print("第",i,"组    64bits"
          "\n二进制明文为:", bits_stream_str[(i-1)*64:64*i],"\n对应原内容字符串",bits8_2_strs_decode(bits_stream_str[(i-1)*64:64*i]))
        print("二进制密文为:", list_2_str(c),"\n对应密文字符串：",bits8_2_strs_decode(list_2_str(c)))
        print("二进制解密为:", list_2_str(m),"\n对应解密字符串",bits8_2_strs_decode(list_2_str(m)))
# main_image("123.jpg",3)
    return

def show_image_c_or_m(bits_stream:str):
    base64_data_str=bits8_2_strs_decode(bits_stream)
    str_2_image(base64_data_str)
def str_2_image(base64_data_str):
    base64_data_bytes = base64_data_str.encode('utf-8')
    # print(base64_data_bytes)
    # print('bytes类型--转--二进制类型')
    image_data = base64.b64decode(base64_data_bytes)
    # print(image_data)
    # print('二进制类型--转--数组')
    # 使用 matplotlib,io 库将二进制类型转为数组
    img_data = plt.imread(BytesIO(image_data), "JPG")
    # 第一个参数目前还不清楚
    # 第二个参数可以为 PNG、JPG
    # print(type(img_data))
    # print(img_data.shape)
    # 使用cv2库显示图片
    img_cv2 = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
    cv2.imshow('a', img_cv2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    filename="123.jpg"
    bits_miwen_stream=main_image(filename)
    # with open(filename, 'rb') as fin:  # 第一个参数为图片全路径或相对路径
    #     # print('二进制类型')
    #     image_data = fin.read()
    #     # 图片:二进制类型
    #     # print(image_data)
    # # print('二进制类型--转--bytes类型')
    # base64_data_bytes = base64.b64encode(image_data)
    # # 图片:bytes类型
    # # print(base64_data_bytes)
    # # print('bytes类型--转--str类型')
    # base64_data_str = base64_data_bytes.decode()
    # # 图片:str类型
    # # print(base64_data_str)
    # # print(type(base64_data_str))
    # bits_stream_str = str_2_bit8(base64_data_str)
    # # print(bits_stream_str[:10])
    # # print(base64_data_str[:10])
    # # print(type(bits_stream_str))
    # # print(ord("a"))
    # #
    #
    # # s="01100001"*3
    # # print(s)
    # # print(len(s))
    # # a=bits_2_strs_decode(s)
    # # print(a)