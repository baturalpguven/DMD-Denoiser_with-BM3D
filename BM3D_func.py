from skimage import io
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from bm3d import bm3d, BM3DProfile
from experiment_funcs import get_experiment_noise, get_psnr, get_cropped_psnr
from math import *





def BM3D(my_image,noisy_signal,noise_var):

    
    

    y_est = bm3d(noisy_signal, sqrt(noise_var));


    # Ignore values outside range for display (or plt gives an error for multichannel input)
    denoied_image = np.minimum(np.maximum(y_est, 0), 1)
    z_rang = np.minimum(np.maximum(noisy_signal, 0), 1)
    
    return denoied_image


my_image = io.imread(r"C:\Users\User\Desktop\Masa Üstü Çöpleri ))\test_image.jpg",True) 

#noice added
noise = np.random.normal(0, .1, my_image.shape)
noisy_signal = my_image + noise
if __name__ == '__main__':
    plt.figure()
    a=BM3D(my_image,noisy_signal,0.01)
    plt.imshow(a,cmap='gray')
