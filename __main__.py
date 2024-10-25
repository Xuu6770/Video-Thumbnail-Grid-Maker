import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import VideoThumbnailGridMaker as vtgm


def main():

    def select_file():
        # 打开文件对话框，选择文件
        file_path = filedialog.askopenfilename(
            filetypes=[("All files", "*.*")]  # 允许选择所有类型的文件
        )
        # 如果用户选择了文件，则更新编辑框中的文本
        if file_path:
            file_path_entry.config(state="normal")  # 先让文本框可被编辑
            file_path_entry.delete(0, tk.END)  # 清除当前内容
            file_path_entry.insert(0, file_path)  # 插入文件路径
            file_path_entry.config(state="readonly")  # 恢复文本框的只读属性
            file_path_entry.xview(len(file_path))  # 定位到文本的末端

            # 设置图片的输出目录和文件名，默认输出在影片文件的目录下
            output_path_entry.delete(0, tk.END)  # 清除当前内容
            output_path = os.path.join(os.path.dirname(file_path), "预览.jpg")
            output_path_entry.insert(0, output_path)
            output_path_entry.xview(len(file_path))  # 定位到文本的末端

    def start_make_thumbnail():

        start_button["state"] = tk.DISABLED  # 程序开始工作，禁止多次点击按钮

        vtgm.create_thumbnail_grid(
            # 视频文件路径
            file_path_entry.get(),

            # 最终图片的名称及输出路径
            output_path_entry.get(),

            # 截图的数量，默认 4 行 4 列，总计 16 张图
            (int(pic_row_num_entry.get()),
             int(pic_col_num_entry.get())),

            # 截图的间距，位于边缘的截图同样需要与边缘保持这个距离
            int(padding_entry.get()),

            # 圆角半径，设置为 0 则不应用圆角效果
            int(corner_radius_entry.get()),

            # 最终图片的最终宽度，设置为 0 则不调整大小
            int(final_width_entry.get()))

        messagebox.showinfo("通知", "完成")
        start_button["state"] = tk.NORMAL  # 恢复按钮的点击

    # 创建主窗口
    root = tk.Tk()
    root.title("视频网格缩略图生成器")

    # 创建按钮
    button = tk.Button(root, text="选择影片文件", command=select_file)
    button.grid(row=0, column=0, padx=5, pady=4)  # 网格布局，需要设置控件所在的行和列

    # 创建编辑框
    file_path_entry = tk.Entry(root)
    file_path_entry.config(state="readonly")  # 编辑框只读
    file_path_entry.grid(row=0, column=1, padx=5, pady=4)

    # 创建标签
    label1 = tk.Label(root, text="截图行数：")
    label1.grid(row=1, column=0, padx=5, pady=4)

    pic_row_num_entry = tk.Entry(root)
    pic_row_num_entry.insert(0, "4")
    pic_row_num_entry.grid(row=1, column=1, padx=5, pady=4)

    label2 = tk.Label(root, text="截图列数：")
    label2.grid(row=2, column=0, padx=5, pady=4)

    pic_col_num_entry = tk.Entry(root)
    pic_col_num_entry.insert(0, "4")
    pic_col_num_entry.grid(row=2, column=1, padx=5, pady=4)

    label3 = tk.Label(root, text="最终图片宽度：")
    label3.grid(row=3, column=0, padx=5, pady=4)

    final_width_entry = tk.Entry(root)
    final_width_entry.insert(0, "1920")
    final_width_entry.grid(row=3, column=1, padx=5, pady=4)

    label4 = tk.Label(root, text="保存路径：")
    label4.grid(row=4, column=0, padx=5, pady=4)

    output_path_entry = tk.Entry(root)
    output_path_entry.grid(row=4, column=1, padx=5, pady=4)

    label5 = tk.Label(root, text="截图之间的距离：")
    label5.grid(row=5, column=0, padx=5, pady=5)

    padding_entry = tk.Entry(root)
    padding_entry.insert(0, "30")
    padding_entry.grid(row=5, column=1, padx=5, pady=4)

    label6 = tk.Label(root, text="截图的圆角：")
    label6.grid(row=6, column=0, padx=5, pady=5)

    corner_radius_entry = tk.Entry(root)
    corner_radius_entry.insert(0, "30")
    corner_radius_entry.grid(row=6, column=1, padx=5, pady=4)

    start_button = tk.Button(root, text="生成网格缩略图",
                             command=start_make_thumbnail)
    start_button.grid(row=7, column=0, columnspan=2, padx=5, pady=10)

    # 开始主事件循环
    root.mainloop()


if __name__ == "__main__":
    main()
