!pip install easyocr
!pip3 install opencv-python

# ************************

import matplotlib.pyplot as plt
import cv2
import easyocr
from pylab import rcParams
from IPython.display import Image
rcParams['figure.figsize'] = 8, 16

# /**********************

reader = easyocr.Reader(['fr'])
Image("bh.jpg")

# **********************

%pylab inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from PIL import Image
im = Image.open("bh.jpg")

# img = mpimg.imread('bh.jpg')

crop_rectangle = (70, 90, 130, 110)
cropped_img = im.crop(crop_rectangle)

imgplot = plt.imshow(cropped_img)
plt.show()
# ************
cropped_img.save('cropped_img.jpg')
# output = reader.readtext('bh.jpg')
output = reader.readtext('cropped_img.jpg')
output

# *************************

output = reader.readtext('bh.jpg')
output


cord = output[-1][0]
x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
x_max, y_max = [int(max(idx)) for idx in zip(*cord)]
