import cv2
import numpy as np

img = cv2.imread('C:/Users/dlehd/Desktop/doc1.jpg')
rows,cols = img.shape[0:2]


d45 = 22.0 * np.pi / 180    # 45도



m45 = np.float32( [[ np.cos(d45), -1* np.sin(d45), rows//3],
                    [np.sin(d45), np.cos(d45), -1*cols//4]])



r45 = cv2.warpAffine(img,m45,(cols,rows))



cv2.imshow("45", cv2.resize(r45,None,fx = 0.2,fy = 0.2, interpolation=cv2.INTER_AREA))

cv2.waitKey(0)
cv2.destroyAllWindows()
