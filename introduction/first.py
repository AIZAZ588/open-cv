import cv2

# load image
## 
# @ params
# cv2.IMREAD_COLOR : read image as color image
# 
img = cv2.imread('./deadpool.jpg',cv2.IMREAD_COLOR)
#img = cv2.imread('./deadpool.jpg',cv2.IMREAD_GRAYSCALE)

# resize image
img = cv2.resize(img,(400,400))

# Show image
##
#  @ params
#  Image : Name of the window
#  img   : Actual variable
# 
cv2.imshow('Image',img)

# Wait for keypress to exit or close the window
## 0: wait for infinite amount of time, i.e 5 means wait for 5 seconds

cv2.waitKey(0)

# when key pressed!
cv2.destroyAllWindows()