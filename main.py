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
    if (image_path[-1] == 'g' and image_path[-2] == 'p' and image_path[-3] == 'j') or (image_path[-1] == 'g' and image_path[-2] == 'n' and image_path[-3] == 'p') or (image_path[-1] == 'g' and image_path[-2] == 'e' and image_path[-3] == 'p' and image_path[-4] == 'j'):
        clear_im = Image.open(image_path)
        clear_im.show()
        if suf_flag == 1:
            clear_im = clear_im.convert("RGB")
        blurred_im = clear_im.filter(ImageFilter.GaussianBlur(5))
        blurred_im.show()
        blurred_im.save('images/gauss_blur_jpg.jpg')
    else:
        print("You have uploaded the file having an invalid extension! Please add it and re-run the code.")

else:
    print("You haven't uploaded any kind of image file in the directory! Please add it and re-run the code.")
