#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans


# In[6]:


def change_color(path,k):
    img = cv2.imread(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    
    h = img.shape[0]
    w = img.shape[1]
    
    x = img.reshape((-1,3))
    km = KMeans(n_clusters=k)
    
    km.fit(x)
    
    centers = np.array(km.cluster_centers_, dtype="uint")
    new_img = np.zeros((x.shape[0],3), dtype = "uint")
    
    for i in range(x.shape[0]):
        new_img[i] = centers[km.labels_[i]]
    
    new_img = new_img.reshape((h,w,3))
    
    return new_img


# In[ ]:




