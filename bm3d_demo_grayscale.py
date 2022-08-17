"""
Grayscale BM3D denoising demo file, based on
Y. Mäkinen, L. Azzari, A. Foi, 2020,
"Collaborative Filtering of Correlated Noise: Exact Transform-Domain Variance for Improved Shrinkage and Patch Matching",
in IEEE Transactions on Image Processing, vol. 29, pp. 8339-8354.
"""
from skimage import io
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from bm3d import bm3d, BM3DProfile
from experiment_funcs import get_experiment_noise, get_psnr, get_cropped_psnr
from math import *

def main():

    my_image = io.imread(r"C:\Users\User\Desktop\Masa Üstü Çöpleri ))\test_image.jpg",True) 

    #noice added
    noise = np.random.normal(0, .1, my_image.shape)
    noisy_signal = my_image + noise
    
    noise_var = 0.01  # Noise variance

    y_est = bm3d(noisy_signal, sqrt(noise_var));


    # Ignore values outside range for display (or plt gives an error for multichannel input)
    y_est = np.minimum(np.maximum(y_est, 0), 1)
    z_rang = np.minimum(np.maximum(noisy_signal, 0), 1)
    plt.title("y, z, y_est")
    plt.imshow(np.concatenate((my_image, np.squeeze(z_rang), y_est), axis=1), cmap='gray')
    plt.show()


if __name__ == '__main__':
    main()

