import tkinter as tk  # 引入tkinter库，用于GUI界面设计
from PIL import Image, ImageTk  # 引入PIL库中的Image和ImageTk模块，用于图像处理和Tkinter兼容
import numpy as np  # 引入numpy库，用于处理数组操作
import cv2  # 引入OpenCV库，用于图像处理

# 读取图像，并将BGR转换为RGB格式
#TODO

# 将RGB图像分解为R、G、B三个通道
red_image = #TODO
green_image = #TODO
blue_image = #TODO

# 获取图像的高度和宽度
height, width = #TODO

# 创建一个空(全0)的RGB图像，用于显示调色后的RGB图像【注意是RGB，不是灰度图】
# 高度为图像的高度，宽度为三张图像并列显示的宽度，数据类型为 np.uint8
rgb_image = #TODO

# 初始化Tkinter窗口
root = tk.Tk()
root.title("RGB Image Mixer")

# 定义显示图像的最大宽度和高度
display_width = 1000
display_height = 800

# 创建一个标签用于显示图像
label_image = tk.Label(root)
label_image.pack()

# 创建一个变量用于存储显示模式（灰度或彩色）
display_mode = tk.IntVar()

def update_image(*args):
    """
    更新图像函数，用于根据R、G、B通道的偏移量以及显示模式更新显示图像。
    """
    # 获取R、G、B通道的偏移量
    red_offset = scale_red.get()
    green_offset = scale_green.get()
    blue_offset = scale_blue.get()

    # 创建一个空的显示图像
    display_image = np.zeros_like(rgb_image)

    # 根据偏移量将R、G、B通道的图像添加到显示图像中
    display_image[:, red_offset:red_offset+width, 0] = red_image
    display_image[:, green_offset:green_offset+width, 1] = green_image
    display_image[:, blue_offset:blue_offset+width, 2] = blue_image

    # 如果显示模式为灰度，将图像display_image转换为灰度图
    if display_mode.get() == 0:
        display_image = #TODO 

    # 将图像转换为PIL格式
    pil_image = Image.fromarray(np.uint8(display_image))

    # 计算图像宽高与显示宽高的比例
    width_ratio = display_width / pil_image.width
    height_ratio = display_height / pil_image.height

    # 选择较小比例进行等比例缩放
    ratio = min(width_ratio, height_ratio)
    new_width = int(pil_image.width * ratio)
    new_height = int(pil_image.height * ratio)

    # 根据比例缩放图像
    pil_image = pil_image.resize((new_width, new_height), Image.LANCZOS)

    # 将缩放后的图像转换为Tkinter兼容的格式
    tk_image = ImageTk.PhotoImage(pil_image)

    # 更新标签中的图像
    label_image.configure(image=tk_image)
    label_image.image = tk_image

# 创建R、G、B通道偏移量的滑动条
max_offset = 2 * width
scale_red = tk.Scale(root, from_=0, to=max_offset, orient=tk.HORIZONTAL, command=update_image)
scale_red.pack(fill=tk.X)
scale_green = tk.Scale(root, from_=0, to=max_offset, orient=tk.HORIZONTAL, command=update_image)
scale_green.set(width)
scale_green.pack(fill=tk.X)
scale_blue = tk.Scale(root, from_=0, to=max_offset, orient=tk.HORIZONTAL, command=update_image)
scale_blue.set(2 * width)
scale_blue.pack(fill=tk.X)

# 创建显示模式的单选按钮（灰度和彩色）
rb_gray = tk.Radiobutton(root, text="Grayscale", variable=display_mode, value=0, command=update_image)
rb_gray.pack()
rb_color = tk.Radiobutton(root, text="Color", variable=display_mode, value=1, command=update_image)
rb_color.pack()

# 调用更新图像函数以显示初始图像
update_image()

# 启动Tkinter主循环
root.mainloop()