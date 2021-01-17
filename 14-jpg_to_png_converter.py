import sys  # for getting required inputs such as folders and python file
import os   # for arranging paths

from PIL import Image,ImageFilter  # we installed pillow to use PIL

# original_path = sys.argv[1]  # this python file have 3 argument, 0:py file, 1:original files folder, 2:converted files folder
# converted = sys.argv[2]
original_path = './script_pics/'
converted_path = './converted/'  # with . it will look at the current folder
print(converted_path,original_path)

print(os.path.exists(converted_path))  # check the folder exist
if not os.path.exists(converted_path):  # if the folder doesnt exist, make a new one
    os.makedirs(converted_path)

for files in os.listdir(original_path):
    img = Image.open(f'{original_path}{files}')  # with original path make a complete path for images
    clean_format = os.path.splitext(files)  # it gives a tuple that extract the name from extension
    print(clean_format)
    img.save(f'{converted_path}{os.path.splitext(clean_format[0])[0]}.png','png')  # I did this because it had two .jpg
    print('all converted')

