# %%
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt

# %%
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# %%
X_train.shape

# %%
plt.imshow(X_train[0], cmap='gray')

# %% [markdown]
# creating model

# %%
X_train[0][27]

# %%
X_train[0][24]

# %%
plt.hist(X_train[0], density=True)

import cv2

# %%
img = cv2.imread('./dog.jpeg')

# %%
plt.imshow(img)
# bc cv read BRG

# %%
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# %%
plt.imshow(rgb_img)

# %%

plt.imshow(lab_img)

# %%



