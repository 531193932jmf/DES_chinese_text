base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
except_dec_num=[]#放的是10进制数字
def add_except(num:int):
    except_dec_num.append(int(num))
# 二进制 to 十进制:
def bin2dec(string_num):
    return str(int(string_num, 2))
# 十六进制 to 十进制
def hex2dec(string_num):
    return str(int(string_num.upper(), 16))
# 十进制 to 二进制: bin()
def dec2bin(string_num):
    num = int(string_num)
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])
#数字列表转字符串
def list_2_str(lis):
    list_str=[]
    for i in lis:
        list_str.append(str(i))
    return "".join(list_str)
# a=list_2_str([1,2,3])
# print(a)
# print(type(a))
# 十进制 to 十六进制:
#10进制 to 16进制
def dec2hex(string_num):
    num = int(string_num)
    if num == 0:
        return '0'
    mid = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 16)
        mid.append(base[rem])
    return ''.join([str(x) for x in mid[::-1]])
# 十六进制 to 二进制
def hex2bin(string_num):
    return dec2bin(hex2dec(string_num.upper()))
# 二进制 to 十六进制
def bin2hex(string_num):
    return dec2hex(bin2dec(string_num))
#bits--> str
def bits_2_str_chinese(bits_stream:list):
    bits16_list=[]
    for i in range(0,len(bits_stream),16):
        bits16_list.append(bits_stream[i:i+16])
    dec_list=[]
    punctoin="，。：；‘”、？】【}{！~·《》|、"
    for i in bits16_list:
        dec=int(bin2dec(i))
        if dec in except_dec_num:
            continue
        if (dec <0 or dec >50000):
            for j in punctoin:
                if(dec==ord(j)):
                    dec_list.append(chr(dec))
            continue
        dec_list.append(chr(dec))
    return "".join(dec_list)
# print(bin(ord("我")))
# print(bin(ord("是")))
# bits="0110001000010001" \
#      "0110011000101111"
# print(len(bits))
# chinese=bits_2_str_chinese(bits)
# print(chinese)

