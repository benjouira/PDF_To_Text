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

# *************************

output = reader.readtext('bh.jpg')
output
