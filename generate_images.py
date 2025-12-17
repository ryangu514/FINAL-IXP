#!/usr/bin/env python3
"""
生成20张记忆图片的脚本
"""
from PIL import Image, ImageDraw, ImageFont
import random
import colorsys

def generate_memory_image(index, filename):
    """生成一张记忆图片"""
    width, height = 1920, 1080

    # 生成渐变背景
    image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(image)

    # 随机选择颜色方案
    hue = (index * 17 + random.randint(0, 30)) % 360 / 360.0
    saturation = 0.3 + random.random() * 0.4

    # 创建渐变背景
    for y in range(height):
        progress = y / height
        lightness = 0.2 + progress * 0.6
        r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
        color = (int(r * 255), int(g * 255), int(b * 255))
        draw.line([(0, y), (width, y)], fill=color)

    # 添加一些抽象图形
    num_shapes = random.randint(5, 15)
    for _ in range(num_shapes):
        shape_type = random.choice(['circle', 'rectangle', 'line'])
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)

        # 半透明颜色
        shape_hue = random.random()
        r, g, b = colorsys.hls_to_rgb(shape_hue, 0.5, 0.5)
        alpha = random.randint(20, 80)

        if shape_type == 'circle':
            radius = random.randint(50, 300)
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.ellipse(
                [x1 - radius, y1 - radius, x1 + radius, y1 + radius],
                fill=(int(r * 255), int(g * 255), int(b * 255), alpha)
            )
            image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

        elif shape_type == 'rectangle':
            x2 = x1 + random.randint(100, 400)
            y2 = y1 + random.randint(100, 400)
            overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.rectangle(
                [x1, y1, x2, y2],
                fill=(int(r * 255), int(g * 255), int(b * 255), alpha)
            )
            image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

        elif shape_type == 'line':
            x2 = random.randint(0, width)
            y2 = random.randint(0, height)
            width_line = random.randint(5, 30)
            draw.line([x1, y1, x2, y2], fill=(int(r * 255), int(g * 255), int(b * 255)), width=width_line)

    # 添加记忆编号文字
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 120)
    except:
        font = ImageFont.load_default()

    text = f"Memory #{index:02d}"

    # 文字阴影
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # 半透明背景
    overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    padding = 40
    overlay_draw.rectangle(
        [text_x - padding, text_y - padding, text_x + text_width + padding, text_y + text_height + padding],
        fill=(0, 0, 0, 120)
    )
    image = Image.alpha_composite(image.convert('RGBA'), overlay).convert('RGB')

    # 绘制文字
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), text, fill=(255, 255, 255), font=font)

    # 添加一些噪点效果
    pixels = image.load()
    for _ in range(width * height // 100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        noise = random.randint(-30, 30)
        r, g, b = pixels[x, y]
        pixels[x, y] = (
            max(0, min(255, r + noise)),
            max(0, min(255, g + noise)),
            max(0, min(255, b + noise))
        )

    # 保存图片
    image.save(filename, 'JPEG', quality=85)
    print(f"Generated: {filename}")

def main():
    """生成所有记忆图片"""
    print("开始生成记忆图片...")

    for i in range(1, 21):
        filename = f"images/memory{i:02d}.jpg"
        generate_memory_image(i, filename)

    print("\n✓ 成功生成20张记忆图片！")

if __name__ == "__main__":
    main()
