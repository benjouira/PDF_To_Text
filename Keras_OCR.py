# pip install keras-ocr

import matplotlib.pyplot as plt
import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()

images=[keras_ocr.tools.read(images) for images in ['bh.jpg']]

images

prediction = pipeline.recognize(images)

prediction
