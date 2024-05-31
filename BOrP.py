from PIL import Image

def check_jpeg_type(image_path):
    try:
        with Image.open(image_path) as img:
            # PIL库中，“info”字典包含了图像的元数据
            if "progressive" in img.info:
                return "Progressive JPEG" if img.info["progressive"] else "Baseline JPEG"
            else:
                return "Cannot determine JPEG type"
    except IOError:
        return "Error opening image. Please check the file path and try again."

# 在程序运行时获取用户输入的图片路径
image_path = input("请输入你想查询的图片路径: ")
print(check_jpeg_type(image_path))
