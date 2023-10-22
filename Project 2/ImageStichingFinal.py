#!/usr/bin/env python
# coding: utf-8

# In[6]:


# importing necessary libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# taking two images for stiching
#importing images from folder
#reference image

#one and two
img1_a = cv.imread('b1.jpg')
img2_a = cv.imread('b2.jpg')
img1 = cv.resize(img1_a,(500,500))
img2 = cv.resize(img2_a,(500,500))

#stiching image

def keyPointMatcher(im1,im2):

  # Initiate SIFT object with default values
  sift = cv.SIFT_create()

  # detect and compute the keypoints and descriptors with SIFT
  kp1, des1 = sift.detectAndCompute(im1,None)
  kp2, des2 = sift.detectAndCompute(im2,None)

  # draw keypoints in image
  im1 = cv.drawKeypoints(im1, kp1, None, flags=0)
  im2 = cv.drawKeypoints(im2, kp2, None, flags=0)

  # display the image with keypoints drawn on it
  cv.imshow('im1',im1)
  # display the image with keypoints drawn on it
  cv.imshow('im2',im2)
  # create BFMatcher object
  bf = cv.BFMatcher()
  # Perform Feature Matching
  matches_12 = bf.knnMatch(des1,des2,k=2)

  # Apply ratio test to filter good matches
  good_matches_12 = []
  for m,n in matches_12:
   if m.distance < 0.6 * n.distance:
        good_matches_12.append(m)

  # Extract keypoints from good matches
  src_pts12 = np.float32([kp1[m.queryIdx].pt for m in good_matches_12]).reshape(-1, 1, 2)
  dst_pts12 = np.float32([kp2[m.trainIdx].pt for m in good_matches_12]).reshape(-1, 1, 2)

  # Use RANSAC to estimate the transformation matrix (homography)
  M12, mask12 = cv.findHomography(src_pts12, dst_pts12, cv.RANSAC, 5.0)
  # Detect outliers
  outliers12 = []
  for i in range(len(mask12)):
     if not mask12[i]:
         outliers12.append(good_matches_12[i])
         # Visualize outliers (draw them in red)
  outlier_image12 = cv.drawMatches(im1, kp1, im2, kp2, good_matches_12, None, matchColor=(0, 0, 255), singlePointColor=(255, 0, 0))
  cv.imshow('Image',outlier_image12)


#detecting key points and finding correspondence
def keypoints(img1,img2):
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # FLANN parameters
    # FINDING INDEX PARAMETERS FOR FLANN OPERATORS
    des1 = np.float32(des1)
    des2 = np.float32(des2)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    pts1 = []
    pts2 = []
    # ratio test as per Lowe's paper for best matches
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            pts2.append(kp2[m.trainIdx].pt)
            pts1.append(kp1[m.queryIdx].pt)
    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)
    return pts1,pts2,matches

#find correspondence
pts1, pts2, matches = keypoints(img1, img2)
#threshold num of correspondence obtain
if len(matches) <= 15:
    print("image pair is not suaitable for stiching")
    #M = np.identity(3) # no homography generated
else:
    # find homography matrix between images :
    M1 , mask = cv.findHomography(pts2, pts1, cv.RANSAC, ransacReprojThreshold = 3)
    #final width, height of stiched image
    width = img1.shape[1] + img2.shape[1]
    height = img1.shape[0] + img2.shape[0]
    results = cv.warpPerspective(img2, M1, (width,height))
    #print(results.shape)
    #appending images 2 to first
    results[0:img1.shape[0],0:img1.shape[1]] = img1
    
one_two = results

keyPointMatcher(img1,img2)

cv.imshow('img1_2',one_two)
print("Homography Matrix Image 1, Image 2: ",M1)
cv.imwrite('1_2.jpg',results)     #for saving image
cv.waitKey(0)

# importing necessary libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# taking two images for stiching
#importing images from folder
#reference image

#one and two
#img1_a = cv.imread('1_2.jpg')
img1_a = cv.imread('1_2.jpg')
img2_a = cv.imread('b3.jpg')

#img1 = cv.resize(img1_a,(500,500))
img2 = cv.resize(img2_a,(500,500))

#stiching image


#detecting key points and finding correspondence
def keypoints(img1,img2):
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # FLANN parameters
    # FINDING INDEX PARAMETERS FOR FLANN OPERATORS
    des1 = np.float32(des1)
    des2 = np.float32(des2)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    pts1 = []
    pts2 = []
    # ratio test as per Lowe's paper for best matches
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            pts2.append(kp2[m.trainIdx].pt)
            pts1.append(kp1[m.queryIdx].pt)
    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)
    return pts1,pts2,matches

#find correspondence
pts1, pts2, matches = keypoints(img1, img2)
#threshold num of correspondence obtain
if len(matches) <= 15:
    print("image pair is not suaitable for stiching")
    #M = np.identity(3) # no homography generated
else:
    # find homography matrix between images :
    M2 , mask = cv.findHomography(pts2, pts1, cv.RANSAC, ransacReprojThreshold = 3)
    #final width, height of stiched image
    width = img1.shape[1] + img2.shape[1]
    height = img1.shape[0] + img2.shape[0]
    results = cv.warpPerspective(img2, M2, (width,height))
    #print(results.shape)
    #appending images 2 to first
    results[0:img1.shape[0],0:img1.shape[1]] = img1
    
one_two = results
keyPointMatcher(img1_a,img2_a)
print("Homography Matrix Image 1, Image 2, Image 3: ",M2)

cv.imshow('img1_2_3',one_two)
cv.imwrite('1_2_3.jpg',results)     #for saving image
cv.waitKey(0)
# importing necessary libraries
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# taking two images for stiching
#importing images from folder
#reference image
#one and two
img1_a = cv.imread('1_2_3.jpg')
img2_a = cv.imread('b4.jpg')

#img1 = cv.resize(img1_a,(500,500))
img2 = cv.resize(img2_a,(500,500))

#stiching image

#detecting key points and finding correspondence
def keypoints(img1,img2):
    sift = cv.SIFT_create()
    # find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    # FLANN parameters
    # FINDING INDEX PARAMETERS FOR FLANN OPERATORS
    des1 = np.float32(des1)
    des2 = np.float32(des2)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(des1,des2,k=2)
    pts1 = []
    pts2 = []
    # ratio test as per Lowe's paper for best matches
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            pts2.append(kp2[m.trainIdx].pt)
            pts1.append(kp1[m.queryIdx].pt)
    pts1 = np.float32(pts1)
    pts2 = np.float32(pts2)
    return pts1,pts2,matches

#find correspondence
pts1, pts2, matches = keypoints(img1, img2)
#threshold num of correspondence obtain
if len(matches) <= 15:
    print("image pair is not suaitable for stiching")
    #M = np.identity(3) # no homography generated
else:
    # find homography matrix between images :
    M3 , mask = cv.findHomography(pts2, pts1, cv.RANSAC, ransacReprojThreshold = 3)
    #final width, height of stiched image
    width = img1.shape[1] + img2.shape[1]
    height = img1.shape[0] + img2.shape[0]
    results = cv.warpPerspective(img2, M3, (width,height))
    #print(results.shape)
    #appending images 2 to first
    results[0:img1.shape[0],0:img1.shape[1]] = img1
    
one_two = results
keyPointMatcher(img1_a,img2_a)
print("Homography Matrix Image 1, Image 2, Image 3, Image 4: ",M3)

cv.imshow('img1_2_3_4',one_two)
cv.imwrite('1_2_3_4.jpg',results)     #for saving image
cv.waitKey(0)


# In[ ]:





# In[ ]:




