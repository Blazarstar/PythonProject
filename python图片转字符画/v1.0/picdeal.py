from PIL import Image
#先定义了字符集
table = ''' '#8XOHLTI)i=+;:`'.'''
count = len(table)

def transform(img):
    line = ''
    for i in range(0,b):
        for j in range(0,a):
            gray = img.getpixel((j,i))
            line = line + table[int(((count-1)*gray)/256)]
        line = line + '\n'       # line 就是转换后对应的字符，公式就是把灰度值平均分配到你给定的字符集
#把字符集写入文本文档
    return line

f = open('b.jpg','rb')
img = Image.open(f)
# 设置图像大小
img = img.resize((int(img.size[0]*0.75),int(img.size[1]*0.5)))
if img.mode != "L":
    img = img.convert("L")
a = img.size[0]
b = img.size[1]
print('Info:', a, ' ', b, ' ', count)
tmp = open('tmp.txt','w')
tmp.write(transform(img))
tmp.close()