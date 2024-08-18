import cv2
from PIL import Image, ImageDraw, ImageOps, ImageFont


def create_rounded_rectangle(image, radius):
    # 创建一个与帧图像相同大小的黑色矩形，L 模式表示 8 位像素
    mask = Image.new("L", image.size, 0)

    # 创建一个与帧图像相同大小的白色圆角矩形，黑白两个图像形成掩码
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), image.size], radius=radius, fill=255)

    # 应用透明度并返回图像
    image.putalpha(mask)
    return image


def create_thumbnail_grid(video_path,
                          output_image_path,
                          grid_size,
                          padding,
                          corner_radius,
                          final_width,
                          font_size=100,
                          bg_color=(255, 255, 255),
                          info_bar_height=100):

    # 打开视频文件，如果无法打开则抛出异常。
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("无法打开视频文件")

    # 计算总帧数和帧间隔，用于均匀地从视频中提取帧
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = total_frames // (grid_size[0] * grid_size[1])

    # 从视频中提取指定数量的帧，并将它们存储在 frames 列表中
    frames = []
    for i in range(grid_size[0] * grid_size[1]):
        # 将视频的当前位置设置到特定帧
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * frame_interval)
        # 读取当前位置的视频帧，ret 表示是否成功读取帧，frame 是读取到的帧图像数据
        ret, frame = cap.read()
        # 如果读取失败（可能已到达视频末尾），则跳出循环
        if not ret:
            break
        # 将帧的颜色空间从 BGR（OpenCV 默认）转换为 RGB ，因为大多数图像处理库使用 RGB 格式
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # 将转换后的帧转换为 PIL 的 Image 对象，并添加到 frames 列表中
        frames.append(Image.fromarray(frame))

    if not frames:
        raise ValueError("未能从视频中提取到帧")

    # 记录单帧宽度和高度
    width, height = frames[0].size

    # 计算拼接完成后的图像的宽度和高度
    grid_width = width * grid_size[1] + padding * (grid_size[1] + 1)
    grid_height = height * grid_size[0] + \
        padding * (grid_size[0] + 1) + info_bar_height

    # 创建一张背景板
    grid_image = Image.new('RGBA', (grid_width, grid_height), bg_color)

    # 将每一帧放置到背景板中适当的位置
    for idx, frame in enumerate(frames):
        row = idx // grid_size[1]
        col = idx % grid_size[1]
        x = col * (width + padding) + padding
        y = row * (height + padding) + padding + info_bar_height

        # 如果用户设置了圆角的大小，则需要对图片进行圆角处理
        if corner_radius > 0:
            frame = create_rounded_rectangle(
                frame.convert("RGBA"), radius=corner_radius)

        grid_image.paste(frame, (x, y), frame)

    # 添加视频信息区域
    draw = ImageDraw.Draw(grid_image)
    font = ImageFont.load_default(size=100)

    # 获取视频的分辨率和帧率信息
    video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_resolution = f"{video_width}x{video_height}"
    video_fps = f"{cap.get(cv2.CAP_PROP_FPS):.2f} FPS"
    video_info = f"{video_resolution} | {video_fps}"

    # 设置分辨率和帧率信息文本的展示位置
    text_x = padding
    text_y = (info_bar_height - font_size) // 2  # 文本垂直居中

    draw.text((text_x, text_y), video_info, fill=(0, 0, 0), font=font)

    # 考虑到拼接完成后到图像可能过大，需要进行等比例缩放，所以这里将计算缩放的比例
    if final_width > 0:
        scale_factor = final_width / grid_width
        new_grid_width = final_width
        new_grid_height = int(grid_height * scale_factor)

        # 调整图像的最终大小
        grid_image = grid_image.resize((new_grid_width, new_grid_height))
        grid_image = grid_image.convert("RGB")
        grid_image.save(output_image_path)
    else:
        # 如果用户将最终的宽度设置为 0 ，则表示不需要对图像大小进行调整，直接保存即可
        grid_image.save(output_image_path)

    # 释放资源
    cap.release()


# 示例用法
video_path = 'xxx.mp4'  # 视频文件路径
output_image_path = '预览.jpg'  # 最终生成的图片的名称及保存路径
grid_size = (4, 4)  # 图片的数量，例如此处是 4 行 4 列，总计 16 张图
padding = 30  # 图片的间距，位于边缘的图片同样需要与边缘保持这个距离
corner_radius = 30  # 圆角半径，设置为 0 则不应用圆角效果
final_width = 1920  # 拼接完成后的图片的最终宽度，设置为 0 则不调整大小

# 调用函数并传入参数开始工作！
create_thumbnail_grid(video_path,
                      output_image_path,
                      grid_size,
                      padding,
                      corner_radius,
                      final_width)
