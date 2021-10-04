#!/usr/bin/env python
# coding: utf-8

# In[1]:


from osgeo import gdal
import matplotlib.pyplot as plt

file_path = 'validation/0157baf3866b2cf9v/VH_dB.tif'
gdal_dataset = gdal.Open(file_path)

arr = gdal_dataset.ReadAsArray()

#plt.imshow(arr)


# In[2]:


plt.hist(arr)
plt.show()


# In[3]:


file_path1 = 'validation/0157baf3866b2cf9v/owiWindSpeed.tif'
gdal_dataset = gdal.Open(file_path1)

arr2 = gdal_dataset.ReadAsArray()
plt.hist(arr2)
plt.show()


# In[5]:


file_path2 = 'validation/0157baf3866b2cf9v/owiWindQuality.tif'
gdal_dataset = gdal.Open(file_path2)

arr3 = gdal_dataset.ReadAsArray()
plt.hist(arr3)
plt.show()

