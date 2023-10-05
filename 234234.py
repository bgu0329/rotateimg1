import cv2
import numpy as np

img1 = cv2.imread('C:/Users/PC/Downloads/test.png')
img2 = cv2.imread('C:/Users/PC/Downloads/test.png')
rows, cols = img1.shape[0:2]

d45 = -9.5 * np.pi / 180  
gray_img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


shift_x = -1* rows //7
shift_y = cols // 10 

m45 = np.float32([[np.cos(d45), -1 * np.sin(d45), shift_x],
                  [np.sin(d45), np.cos(d45), shift_y]])

r45 = cv2.warpAffine(img1, m45, (cols, rows))

cv2.imshow("45", cv2.resize(r45, None, fx=1, fy=1, interpolation=cv2.INTER_AREA))
cv2.imshow("gray",cv2.resize(gray_img, None, fx=2, fy=2, interpolation=cv2.INTER_AREA))

cv2.waitKey(0)
cv2.destroyAllWindows()
