import flet as ft

from src import video_thumbnail_grid_maker as maker


def main(page: ft.Page):
    page.title = "视频网格缩略图生成器"
    page.window.width = 500
    page.window.height = 350
    page.window.resizable = False

    def start_make_thumbnail(e):
        maker.create_thumbnail_grid(video_path=video_path_tf.value,
                                    output_image_path=save_path_tf.value,
                                    grid_size=[int(ss_row_num_tf.value), int(ss_col_num_tf.value)],
                                    padding=int(ss_padding_tf.value),
                                    corner_radius=int(ss_radius_tf.value),
                                    final_width=int(final_pic_with_tf.value))
        page.open(ft.AlertDialog(title=ft.Text(value="完成")))

    start_fab = ft.FloatingActionButton(icon=ft.Icons.PHOTO, on_click=start_make_thumbnail, disabled=True)

    def on_dialog_result(e: ft.FilePickerResultEvent):
        # 处理「选择视频文件」的逻辑
        if e.files:
            file = e.files[0]
            video_path_tf.value = file.path
            # 使用 rfind 方法找到最后一个斜杠的索引位置
            last_slash_index = file.path.rfind('/')
            # 截取到最后一个斜杠的位置，即得到目录路径
            directory_path = file.path[:last_slash_index + 1]
            save_path_tf.value = directory_path + "预览.jpg"
            start_fab.disabled = False
            page.update()
        # 处理「选择保存位置」的逻辑
        if e.path:
            save_path_tf.value = e.path + "预览.jpg"
            start_fab.disabled = False
            page.update()

    video_path_tf = ft.TextField(label="视频文件路径", expand=True)
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    save_path_tf = ft.TextField(label="缩略图保存位置（默认保存至视频所在目录）", expand=True)

    ss_row_num_tf = ft.TextField(label="截图行数", value="4", expand=True)
    ss_col_num_tf = ft.TextField(label="截图列数", value="4", expand=True)

    final_pic_with_tf = ft.TextField(label="最终图片宽度", value="1920", expand=True)
    ss_padding_tf = ft.TextField(label="截图间距", value="30", expand=True)
    ss_radius_tf = ft.TextField(label="截图圆角", value="30", expand=True)

    view = ft.Column(controls=[
        ft.Row(controls=[video_path_tf,
                         ft.ElevatedButton(text="选择视频文件", on_click=lambda _: file_picker.pick_files())]),
        ft.Row(controls=[save_path_tf,
                         ft.ElevatedButton(text="选择保存位置", on_click=lambda _: file_picker.get_directory_path())]),
        ft.Row(controls=[ss_row_num_tf, ss_col_num_tf]),
        ft.Row(controls=[final_pic_with_tf, ss_padding_tf, ss_radius_tf])])

    page.overlay.append(file_picker)
    page.floating_action_button = start_fab
    page.add(view)


ft.app(main)
