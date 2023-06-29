# DMD-Denoiser_with-BM3D
In this project, the BM3D model has been used as a powerful tool for the purpose of image reconstruction. The primary objective of this project was to reconstruct an image through the simulation of a Single-Pixel-Imagin with randomly generated Digital Micromirror Device (DMD) patterns using Python. In order to achieve this goal, various conventional methods were employed for the image reconstruction process. The resultant reconstructed images obtained from each method were compared visually with one another to assess their performance and effectiveness.

## What is BM3D

BM3D (Block-Matching 3D) is a state-of-the-art image-denoising algorithm that effectively reduces noise in images while preserving their details and structures. It operates on the principle of collaborative filtering, where similar patches in the image are grouped together and jointly processed to enhance denoising performance. The main steps involved in the BM3D algorithm include block-matching, collaborative filtering, and aggregation.

## Alternating Direction Method of Multipliers (ADMM)

The Alternating Direction Method of Multipliers (ADMM) is an optimization algorithm commonly used to solve optimization problems with multiple variables and constraints. It is particularly useful for problems that can be decomposed into smaller subproblems, allowing for efficient parallelization. ADMM iteratively updates the variables while enforcing consistency between them through the use of dual variables. The general update steps in ADMM involve minimizing individual subproblems and updating the dual variables.

## Total Variation (TV) Norm Minimization

Total Variation (TV) regularization is a technique used for image denoising and image reconstruction tasks. It exploits the property that natural images tend to have regions with smooth intensity variations separated by sharp edges. The TV method aims to preserve the sharp edges while reducing the noise by minimizing the total variation of the image, which represents the sum of the absolute differences between adjacent pixel intensities. By minimizing the total variation, the TV method effectively suppresses noise while preserving important image features.

## $\ell_1$ Norm Minimization

$\ell_1$ norm minimization is a commonly used technique in signal processing and optimization problems. It involves minimizing the sum of the absolute values of the elements of a vector. The $\ell_1$ norm promotes sparsity and is often employed in situations where the underlying signal or solution is expected to have a sparse representation. By minimizing the $\ell_1$ norm, one can encourage solutions with fewer non-zero coefficients, leading to simpler and more interpretable models. In the context of denoising or image reconstruction, $\ell_1$ norm minimization can be used to promote sparsity in the transformed domain, helping to reduce noise and enhance important signal features.


## Results

<div align='center'>

![image](https://github.com/baturalpguven/DMD-Denoiser_with-BM3D/assets/77858949/f7909cc5-1d28-41fe-ad68-c65dec4e9714)

![image](https://github.com/baturalpguven/DMD-Denoiser_with-BM3D/assets/77858949/d6b82941-0f4d-443d-8c74-a169a020e6d5)
</div>

## Running the Code

The files that were previously stored on Google Drive have now been migrated to the GitHub repository. You can access and view these files directly in the repository. The primary code that encompasses the entirety of the work done is the `BM3D_ADMM_Code.ipynb` notebook. This notebook serves as the central hub where all the necessary tasks and operations have been implemented.
