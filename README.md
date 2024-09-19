<h1 align = "center">Video Thumbnail Grid Maker</h1>

<p align = "center">
    <a href = "README.md" target = "_blank">EN</a> | <a href = "README_CN.md" target = "_blank">CN</a>
</p>

## Features

- [x] Customize the number of screenshots, for example 3×3 or 4×4;
- [x] Customize the width of the final picture (the height will be scaled automatically), set to `0` to keep the original size;
- [x] Customize the distance between the screenshots;
- [x] Customize the rounded corners of the screenshot, set to `0` to not apply the rounded corner style;
- [x] Each screenshot in the grid is labeled with its corresponding time in the video;
- [x] Support `mp4`, `mkv` and other common video formats;
- [x] A simple but sufficiently usable GUI;

## Use

Install the dependencies first:

``shell
pip3 install opencv-python pillow
``

Open the project, run `__main__.py`, and adjust the parameters on the interface according to your needs (bold text is mandatory setting items):

1. **Click the button to select the video file to read its file path;**
2. the number of screenshot rows, default is 4;
3. the number of screenshot columns, default is 4;
4. final picture width, default is 1920 pixels, if you adjust the width manually, the height will be adjusted automatically according to the proportion.
5. save path, default to `__main__.py` directory. You can modify the path by yourself. Note that the path needs to include the file name;
6. distance between screenshots, default is 30;
7. the rounded corners of the screenshots, default is 30;

## Demo

| Program Interface |
|:----------------:|
| ![](GUI.png) |  

| Output Image Effect |
|:----------------:|
| ![](demo.jpg) |
|:----------------:|
| Screenshot from 《My Undead Yokai Girlfriend》 | 

## Todo

- [ ] Compile to executable so it can run directly on Windows and macOS;
- [ ] Add multi-language support to the GUI;
- [ ] If the video has embedded subtitles, screenshots can be taken with or without subtitles;
