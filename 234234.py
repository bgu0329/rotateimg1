import cv2
import numpy as np

img1 = cv2.imread('C:/Users/PC/Downloads/test.png')  # First image
img2 = cv2.imread('C:/Users/PC/Downloads/test.png')  # Second image
rows, cols = img1.shape[0:2]  # 사진 가로 세로 너비 가져오기

d45 = -9.5 * np.pi / 180  # 라디안으로 돌릴 각도 초기화

# 색 있는 이미지 회색으로 변환
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# 회색으로 만든 이미지 이진화 하기
threshold_value = 127  # 임계값 설정
ret, binary_img = cv2.threshold(gray_img2, threshold_value, 255, cv2.THRESH_BINARY)

shift_x = -1 * rows // 7
shift_y = cols // 10

m45 = np.float32([[np.cos(d45), -1 * np.sin(d45), shift_x],
                  [np.sin(d45), np.cos(d45), shift_y]])

r45 = cv2.warpAffine(img1, m45, (cols, rows))

cv2.imshow("45", cv2.resize(r45, None, fx=1, fy=1, interpolation=cv2.INTER_AREA))
cv2.imshow("gray", binary_img)  # 이진화 출력

cv2.waitKey(0)
cv2.destroyAllWindows()
