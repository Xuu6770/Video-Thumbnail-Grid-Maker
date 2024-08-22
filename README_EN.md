<h1 align = "center">Video Thumbnail Grid Maker</h1>

<p align = "center">
    <a href = "README.md" target = "_blank">CN</a> | <a href = "README_EN.md" target = "_blank">EN</a>
</p>

## Features

- [x] Customize the number of pictures, for example 3×3 or 4×4.
- [x] Customize the width of the final picture (the height will be scaled automatically), set to `0` to keep the original size;
- [x] Customize the distance between the pictures;
- [x] Customize the rounded corners of the pictures, set to `0` to not apply the rounded corner style;
- [x] Each screenshot in the grid is labeled with its corresponding time in the video;
- [x] Support `mp4`, `mkv` and other common video formats.

## Use

Install the dependencies first:

```shell
pip3 install opencv-python pillow
```

You also need to set the parameters before executing the code:

```python
video_path = 'xxx.mp4'  # Path to the video file
output_image_path = 'preview.jpg'  # The name of the final image and the output path
grid_size = (4, 4)  # number of images, e.g. here 4 rows and 4 columns, total 16 images
padding = 30  # the spacing of the images, images on the edges need to be spaced away from the edges as well
corner_radius = 30  # set to 0 to not apply the rounding effect
final_width = 1600  # The final width of the final image, set to 0 for no resizing
```

In fact, only `video_path` has to be changed.

## Demo

| ![](demo.jpg) |
|:----------------:|
| Screenshot from 《My Undead Yokai Girlfriend》 |  

## Todo

Sort by priority:

- [ ] Add GUI;
- [ ] Package as an executable for distribution to multiple platforms;
- [ ] Screenshots with subtitles;