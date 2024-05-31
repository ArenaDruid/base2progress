from PIL import Image
import os

# 设定原始和目标文件夹路径
origin_dir_path = './origin_dir'
progressive_dir_path = './progressive_dir'

# 如果目标文件夹不存在，创建它
if not os.path.exists(progressive_dir_path):
    os.makedirs(progressive_dir_path)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(origin_dir_path):
    if filename.endswith(('.jpeg', '.jpg', '.png')):  # 检查文件是否为JPEG或PNG
        # 构建完整的文件路径
        origin_file_path = os.path.join(origin_dir_path, filename)
        # 修改文件扩展名为.jpg
        progressive_file_path = os.path.join(progressive_dir_path, os.path.splitext(filename)[0] + '.jpg')

        # 打开并处理图片
        original_image = Image.open(origin_file_path)
        original_image = original_image.convert('RGB')
        
        # 获取原始DPI信息（如果存在）
        dpi = original_image.info.get('dpi', (96, 96))
        
        # 保存为优化的渐进式JPEG
        original_image.save(progressive_file_path, 'JPEG', optimize=True, quality=100, progressive=True, dpi=dpi)

print("所有图片已转换为渐进式JPEG格式。")
