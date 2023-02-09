import numpy as np

# A = []

# A.append(np.array([1,2,3]))
# A.append(np.array([4,5,6]))
# B = np.concatenate(A, axis=0)
# print(A)
# print(B.shape)
# print(np.array(A).shape)

Optimization terminated successfully.           Current function value: 0.000107           Iterations: 8           Function evaluations: 894  
KeyboardInterrupt --------------------------------------------------------------------------- KeyboardInterrupt                         
Traceback (most recent call last) Cell In [15], line 27      
25 pts1 = np.hstack([templeCoords["x1"], templeCoords["y1"]])      
26 P_ref = compute3D_pts_ref(pts1, intrinsics, F, im1, im2) ---> 
27 P = compute3D_pts(pts1, intrinsics, F, im1, im2)      
29 threshold = 100      
30 try:  Cell In [13], line 25, in compute3D_pts(pts1, intrinsics, F, im1, im2)      
22 x2s_temple, y2s_temple = [], []      
23 for (x1,y1) in list(zip(x1s_temple, y1s_temple)): ---> 
25     x2, y2 = epipolarCorrespondence(im1, im2, F, x1, y1)      
26     x2s_temple.append(x2)      
27     y2s_temple.append(y2)  Cell In [9], line 90, in epipolarCorrespondence(im1, im2, F, x1, y1)      
88 patch_2 = np.asarray(patch_2)      
89 diff = patch_1-patch_2 ---> 
90 weighted_diff = np.dstack((scipy.ndimage.gaussian_filter(diff[:,:,0], sigma), scipy.ndimage.gaussian_filter(diff[:,:,1], sigma), scipy.ndimage.gaussian_filter(diff[:,:,2], sigma)))      
91 dist = np.linalg.norm(weighted_diff)      
93 if dist < dist_min:  File /usr/local/lib/python3.10/dist-packages/scipy/ndimage/_filters.py:342, in gaussian_filter(input, sigma, order, output, mode, cval, truncate)     
340 if len(axes) > 0:     
341     for axis, sigma, order, mode in axes: --> 
342         gaussian_filter1d(input, sigma, axis, order, output,     
343                           mode, cval, truncate)     
344         input = output     345 else:  File /usr/local/lib/python3.10/dist-packages/scipy/ndimage/_filters.py:260, in gaussian_filter1d(input, sigma, axis, order, output, mode, cval, truncate)     
258 lw = int(truncate * sd + 0.5)     
259 # Since we are calling correlate, not convolve, revert the kernel --> 260 weights = _gaussian_kernel1d(sigma, order, lw)[::-1]     261 return correlate1d(input, weights, axis, output, mode, cval, 0)  KeyboardInterrupt: 