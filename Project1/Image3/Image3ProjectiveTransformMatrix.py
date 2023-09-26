import cv2
import numpy as np

image = cv2.imread('clock3_1.jpg')
print(image.shape)
print(image.size)
print(type(image))
num_rows, num_cols = image.shape[:2]

image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

src_points = np.float32([[98,1], [497,247], [497,464], [98,666]])
dst_points = np.float32([[0,0], [500,0], [500,500], [0,500]])
projective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
print(projective_matrix)

# [[ 3.50861308e-01 -2.30211437e-17 -3.43844082e+01]
#  [-3.97750607e-01  6.45132082e-01  3.83344274e+01]
#  [-1.44871766e-03 -0.00000000e+00  1.00000000e+00]]
#
#
