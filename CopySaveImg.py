import pyperclip
from PIL import ImageGrab
import tkinter as tk
from tkinter import filedialog
import os
from datetime import datetime

# Powered By GPT-3.5
# Designed By Jason_Stephen

def save_image(image, save_path):
    image.save(save_path)

def get_save_path():
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.askdirectory()
    return save_path

def get_return_path():
    root = tk.Tk()
    root.withdraw()
    return_path = filedialog.askdirectory()
    return return_path

def capture_and_save(save_path_entry, return_path_entry):
    # 从剪切板中获取图片数据
    img = ImageGrab.grabclipboard()

    # 获取保存图片的路径和返回路径的地址
    save_path = save_path_entry.get().strip('"')  # 去除额外的引号
    return_path = return_path_entry.get().strip('"')  # 去除额外的引号

    # 获取当前时间，并将其格式化为指定格式
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")

    # 构建图片文件名
    image_name = "Screenshot_{}.png".format(current_time)

    # 保存图片
    image_path = os.path.join(save_path, image_name)
    save_image(img, image_path)

    # 构建返回的路径
    relative_path = os.path.relpath(image_path, return_path)

    # 构建Markdown格式的链接
    markdown_link = "![]({})".format(os.path.join(return_path, image_name))

    # 复制Markdown格式的链接到剪切板
    pyperclip.copy(markdown_link)

    # 显示提示信息
    info_label.config(text="图片已保存到: {}\nMarkdown链接已复制到剪切板: {}".format(image_path, markdown_link))

# 创建主窗口
root = tk.Tk()
root.title("截图保存工具")

# 创建输入框和标签
save_path_label = tk.Label(root, text="保存图片的路径:")
save_path_label.pack(pady=(10, 0))
save_path_entry = tk.Entry(root, width=50)
save_path_entry.pack(pady=(0, 10))

return_path_label = tk.Label(root, text="返回路径的地址:")
return_path_label.pack()
return_path_entry = tk.Entry(root, width=50)
return_path_entry.pack(pady=(0, 10))

# 创建按钮
capture_button = tk.Button(root, text="保存图片并获取链接", command=lambda: capture_and_save(save_path_entry, return_path_entry))
capture_button.pack()

# 创建提示信息标签
info_label = tk.Label(root, text="")
info_label.pack()

# 运行主循环
root.mainloop()
