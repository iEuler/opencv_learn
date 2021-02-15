import cv2

filepath = r"img/pic01.jpg"

# img = cv2.imread(filepath)
# cv2.namedWindow('Image')
# cv2.imshow('Image', img)
# cv2.waitKey(1000)
# cv2.destroyAllWindows()
#
img = cv2.imread(filepath)
# 转换灰色
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 显示图像
cv2.imshow("Image", gray)
cv2.waitKey(2000)
cv2.destroyAllWindows()