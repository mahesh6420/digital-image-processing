# %%
# !pip install cvlib

# %%
import cv2
import cvlib
import numpy as np
import matplotlib.pyplot as plt

# %%
img = cv2.imread("before.jpg")
plt.imshow(img)
plt.show()

# %%
img_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rbg)
plt.show()

# %%
box, label, conf = cvlib.detect_common_objects(img_rbg, confidence=0.5)

# %%
output = cvlib.object_detection.draw_bbox(img_rbg, box, label, conf)
plt.imshow(output)
plt.show()
