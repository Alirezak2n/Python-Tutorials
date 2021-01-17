
from PIL import Image,ImageFilter  # we installed pillow to use PIL


img = Image.open('script_pics/4.1 pikachu.jpg.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)  # color mode
filtered_image = img.filter(ImageFilter.BLUR)  # we say we want to filter image with ImageFilter's filters
print(dir(img))  # it gives all the options
filtered_image.save('blur.png','png')  # we should mention the name with the extension and also the extension type
# if we dont mention .png, we should change the file to a png by ourself
filtered_image = img.filter(ImageFilter.SMOOTH_MORE)  # jpg doesnt support some of filters
filtered_image.save('Smooth.png','png')
filtered_image = img.convert('L')  # it will grey the image
filtered_image.save('grey.png','png')
rotated = filtered_image.rotate(90)
resized = rotated.resize((300,300))  # for resize we should give the size in a tuple
cropped = resized.crop((100,100,400,400))  # it is for (left,up,right,down) a square
cropped.show()  # it will open the file

img = Image.open('script_pics/6.1 astro.jpg.jpg')
print(img.size)
img2 = img.resize((400,400))  # by doing this we change the default aspect ratio
img2.save('astro_small.jpg')
img.thumbnail((400,400))  # with thumbnail it keep the ratio in place and not in a new image
img.save('astro_ratio.jpg')
print(img.size)
