<h1 align = "center">
Video Thumbnail Grid Maker
</h1>

<p align = "center"><a href = "README.md" target = "_blank">CN</a> | <a href = "README_EN.md" target = "_blank">EN</a></p>

## Features

- [x] Customize the number of images, e.g. 3×3 or 4×4.
- [x] Customize the width of the final image (height is scaled), set width to `0` and no adjustment will be made;
- [x] Customize the distance between the pictures;
- [x] Customize the rounded corners of the images, set `0` to disable rounding;

## Use

Install the dependencies first:

```shell
pip3 install opencv-python pillow
```

You also need to set the parameters before executing the code:

```python
video_path = 'xxx.mp4'  # Path to the video file
output_image_path = 'preview.jpg'  # Name and save path of the final image generated
grid_size = (4, 4)  # number of images, e.g. here 4 rows and 4 columns, total 16 images
padding = 30  # the spacing of the images, images on the edges need to be spaced away from the edges as well
corner_radius = 30  # The radius of the rounded corners, set to 0 to not apply the rounding effect
final_width = 1600  # The final width of the stitched image, set to 0 for no resizing
```

In fact, only `video_path` has to be changed.

## Demo

| ![](preview.jpg) |
|:----------------:|
| Screenshot from 《斗破苍穹》 |  

## Todo

Sort by priority:

- [ ] Add GUI;
- [ ] Package as an executable for distribution to multiple platforms;
- [ ] Label each image with its time;