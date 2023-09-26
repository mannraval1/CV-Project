import cv2
import numpy as np

image = cv2.imread('clock2_1.jpg')
print(image.shape)
print(image.size)
print(type(image))
num_rows, num_cols = image.shape[:2]

image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

src_points = np.float32([[100,1], [497,247], [495,614], [46,660]])
dst_points = np.float32([[0,0], [500,0], [500,500], [0,500]])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
print(projective_matrix)

# [[ 6.02633166e-01  4.93811699e-02 -6.03126978e+01]
#  [-4.51494595e-01  7.28631522e-01  4.44208280e+01]
#  [-1.04342290e-03  8.65079026e-05  1.00000000e+00]]
#
#
