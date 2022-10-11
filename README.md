# Image Processing using Python. (Blurring an image.)

# Steps to use this:-
1) Any image to be blurred has to be placed in the images folder.

2) Further in the terminal we have to proceed to type in the command:- "images/image.jpg".

3) Lastly we obtain the blurred and the original image opened up in the window, and the files can be found in the images folder.


# Explanation:-
1) Firstly, we import the os and the pillow module.

2) We initialize the folder_dir with the name of the folder containing the images for blurring.

3) The checks namely, flag and suf_flag should be set to 0.

4) Next we run a loop in the folder_dir, to check whether any images with .jpg, .png, or .jpeg format is present in it.
If anything other than an image is present in the directory, than in that case we stop the code execution and handle the error by displaying 
an error message to the user.

5) Next, we take input as the image path, which is present in the same directory as that of the main.py file.

6) We use the Image.open method in order to open the image at the path specified, and then the .show() method will display the image 
onto the screen.

7) Next, we implement the Image.convert() method in order to convert the image from .png to .jpg format, before applying any kind of filter to it.

8) Further, we apply the Gaussian Blur filter onto the image, and then use the show command to display it. Lastly we also save the 
new blurred image in the same directory by the name of "gauss_blur_jpg.jpg".
