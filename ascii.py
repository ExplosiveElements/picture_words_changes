# -*- coding=utf-8 -*-

from PIL import Image
import argparse

# 字符画所用的字符集（一共有70个）
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 首先，构建命令行参数处理 ArgumentParaser实例
parser = argparse.ArgumentParser()

# 定义输入文件、输出文件、输出字符画的宽和高
parser.add_argument("file") # 输入文件
parser.add_argument("-o", "--output", type = str) # 输出文件
parser.add_argument("--width", type = int, default=80) # 输出字符画宽
parser.add_argument("--height", type = int, default=80) # 输出字符串高

# 解析并获取参数
args = parser.parse_args()
# 输入的图片的文件路径
IMG = args.file
# 输出字符画的宽度
WIDTH = args.width
# 输出字符画的高度
HEIGHT = args.height
# 输出字符画的路径
OUTPUT = args.output

# 实现RGB转字符的函数
def get_char(r, g, b, alpha = 256):

    # 判断alpha 值
    if alpha == 0:
        return " "
    # 获取字符集的长度（这个是79个）
    length = len(ascii_char)

    # 将 RGB 值转换为灰度值 gary，灰度值范围为 0-255
    gray = int(0.2126 * r + 0.7152 * g + 0.0772 * b)

    # 灰度值范围会0-255 ，而字符集只有 70
    # 需要进行如下处理才能将灰度值映射到指定的字符上
    unit = (256.0 + 1) / length

    # 返回灰度值对应的字符
    return ascii_char[int(gray/unit)]

# 处理图片
if __name__ == '__main__':

    # 打开并调整图片的宽和高
    im = Image.open(IMG)
    #                                表示输出低质量的图片
    im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    # 初始化字符串
    txt = ""

    # 遍历图片中的每一行
    for line in range(HEIGHT):
        # 遍历该行的每一列
        for column in range(WIDTH):
            # 将（colmun, line）坐标的RGB像素转换为字符后添加到txt 字符串
            txt += get_char(*im.getpixel((column, line)))
        # 遍历完一行后需要加换行符
        txt += "\n"
    # 输出到屏幕
    print(txt)

    # 字符画输出到文件
    if OUTPUT:
        with open(OUTPUT, "W") as f:
            f.write(txt)
    else:
        with open("output.txt", "w") as f:
            f.write(txt)