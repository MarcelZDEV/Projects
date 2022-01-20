import cv2

img = cv2.imread('../background_os.jpg', 0)
img = cv2.resize(img, (400, 400))
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite('newbackground.jpg', img)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
