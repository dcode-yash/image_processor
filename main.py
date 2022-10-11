import os
from PIL import Image, ImageFilter
from os import listdir

folder_dir = "images"
flag = 0
suf_flag = 0

for images in os.listdir(folder_dir):
    if images.endswith(".jpg") or images.endswith(".jpeg") or images.endswith("png"):
        if images.endswith(".jpg") or images.endswith(".jpeg"):
            flag = 1
        else:
            suf_flag = 1

if flag == 1:
    image_path = input('Enter the path of the image you want to be blurred.')
    clear_im = Image.open(image_path)
    clear_im.show()
    if suf_flag == 1:
        clear_im = clear_im.convert("RGB")
    blurred_im = clear_im.filter(ImageFilter.GaussianBlur(5))
    blurred_im.show()
    blurred_im.save('images/gauss_blur_jpg.jpg')

else:
    print("You haven't uploaded any kind of image file in the directory! Please add it and re-run the code.")
