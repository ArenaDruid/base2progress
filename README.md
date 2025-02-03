# 图片转渐进式JPEG工具

此脚本用于将指定文件夹中的图片（JPEG/PNG）转换为渐进式JPEG格式，保留原始DPI信息并优化存储。

## 功能特性
- 🖼️ 支持格式：`JPEG`、`JPG`、`PNG` → 输出为`JPEG`
- 🚀 自动创建目标文件夹
- 🔍 保留原始DPI元数据
- ⚡ 优化压缩与渐进式加载支持
- 📁 批量处理整个文件夹

## 依赖安装
```bash
pip install Pillow
```

## 使用方法
1. 创建文件夹结构：
   ```
   ├── main.py
   ├── origin_dir/     # 存放原始图片
   └── progressive_dir/ # 输出目录（自动创建）
   ```

2. 将要转换的图片放入`origin_dir`

3. 运行脚本：
```bash
python main.py
```

## 参数配置
- **质量设置**：修改`quality=100`（范围1-100，值越大质量越高）
- **DPI保留**：自动读取原始DPI，若无则默认96x96
- **优化压缩**：`optimize=True`启用额外压缩优化

## 注意事项
1. 输出文件名将与原始文件同名（扩展名强制为`.jpg`）
2. 100%质量可能生成较大文件，建议根据需求调整
3. 转换后透明度通道（Alpha Channel）将被移除
4. 支持中/英/数字文件名，特殊符号建议提前测试

## 示例
```bash
# 原始文件：origin_dir/photo.png
# 输出文件：progressive_dir/photo.jpg
```

> 建议配合cron或CI/CD工具实现自动化图片优化流程
