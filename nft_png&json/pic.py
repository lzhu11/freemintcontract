
from PIL import Image, ImageDraw
import random
for i in range(0,100):
    # 创建一个新的图像，宽度为 200 像素，高度为 200 像素，背景颜色为白色
    img = Image.new('RGB', (200, 200), color=random.choice(['#ffccb3', '#d2b48c', '#c68642', '#704214', '#3b240b']))

    # 获取一个图像绘制对象
    draw = ImageDraw.Draw(img)

    # 随机选择猫或狗
    animal = random.choice(['cat', 'dog'])

    # 随机选择颜色
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 绘制不同形状的动物
    if animal == 'cat':
        # 绘制猫的头部
        draw.ellipse((50, 50, 150, 150), fill=color)
        # 绘制猫的耳朵
        draw.polygon([(60, 70), (70, 40), (90, 60)], fill=color)
        draw.polygon([(130, 70), (120, 40), (100, 60)], fill=color)
        # 绘制猫的眼睛
        draw.ellipse((80, 80, 95, 95), fill='black')
        draw.ellipse((105, 80, 120, 95), fill='black')
        # 绘制猫的嘴巴
        draw.line((85, 115, 115, 115), fill='black', width=3)
    elif animal == 'dog':
        # 绘制狗的头部
        draw.ellipse((50, 50, 150, 150), fill=color)
        # 绘制狗的耳朵
        draw.polygon([(60, 70), (70, 40), (90, 60)], fill=color)
        draw.polygon([(130, 70), (120, 40), (100, 60)], fill=color)
        # 绘制狗的眼睛
        draw.ellipse((80, 80, 95, 95), fill='black')
        draw.ellipse((105, 80, 120, 95), fill='black')
        # 绘制狗的鼻子
        draw.ellipse((90, 110, 110, 130), fill='black')
        # 绘制狗的舌头
        draw.polygon([(95, 135), (100, 130), (105, 135)], fill='red')

    accessory = random.choice(['hat', 'glasses'])

    # 绘制附件
    if accessory == 'hat':
        hat_color = random.choice(['black', 'blue', 'brown', 'green', 'red'])
        vertices = [(90, 50), (100, 30), (110, 50)]
        draw.polygon(vertices, fill=hat_color, outline=hat_color)
        
    elif accessory == 'glasses':
        glasses_color = random.choice(['white', 'brown','blue'])
        draw.rectangle((75, 80, 96, 100), fill=glasses_color, outline='black')
        draw.rectangle((104, 80, 125, 100), fill=glasses_color, outline='black')
        draw.line((96, 90, 104, 90), fill='black', width=2)
        
    # 保存图像到文件
    img.save('/Users/zhu/Desktop/pic/'+str(i)+'.png')
