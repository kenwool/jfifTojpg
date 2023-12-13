from PIL import Image
import os

# 获取当前文件夹中所有的jfif格式图片
jfif_files = [f for f in os.listdir() if f.endswith('.jfif')]

# 遍历每个jfif文件并将其转换为jpg格式
for jfif_file in jfif_files:
    # 打开jfif图片
    with Image.open(jfif_file) as img:
        # 构造输出的jpg文件名，将jfif扩展名替换为jpg
        jpg_file = jfif_file.replace('.jfif', '.jpg')
        # 保存为jpg格式，quality=100表示无损保存
        img.save(jpg_file, 'JPEG', quality=100)

print("转换完成！")
