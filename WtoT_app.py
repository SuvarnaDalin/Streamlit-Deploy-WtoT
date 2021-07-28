# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 10:43:55 2021

@author: suvarna
"""
# Import Libraries

import streamlit as st
from PIL import Image, ImageMath

import matplotlib.pyplot as plt
import numpy as np



# Function to covert White backgroung image to Transparent background image

def whiteToTransparent(white):
    img = Image.open(white)
    img = img.convert("RGBA")
    
    datas = img.getdata()

    newData = []

    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save('Transparent.png', 'PNG')
    return(img)

#Title of the App
st.title('WHITE TO TRANSPARENT BACKGROUD CONVERTER')

# create image uploader
img_data = st.file_uploader(label='Load Image For Conversion', type=['png', 'jpg'])

if img_data is not None:
    
    #display uploaded image
    uploaded_img = Image.open(img_data)
    st.title('Image with White Background')
    st.image(uploaded_img)
    
    #load image to do the coversion
    inp_image = img_data 
    #f'D:/WORK/3_July2021/IMAGE Conversion/Streamlit/{img_data.name}'
    
    #generate output
    out_image = whiteToTransparent(inp_image)

    #display it:
    st.title('Image with Transparent Background')
    st.image(out_image)
   
    
                
                
    
                
                