###importing the required package
from PIL import Image
# path = "/home/chhabilal/Desktop/treeleaf/handwritten datasets/images/"
# counter = 1
# for fil
#open image in png format
img = Image.open('/home/chhabilal/Desktop/treeleaf/tesseract_comparision/data/13.png')
img_png = img.convert('RGB')
  
#The image object is used to save the image in jpg format
img_png.save('/home/chhabilal/Desktop/treeleaf/tesseract_comparision/data/13.jpg')
