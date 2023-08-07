import cv2

source = "ef3dfac7-6b2c-463b-b02e-13d2fadaad63.jpg"
destination = 'newImage.png'
scale_percent = 50

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)

new_width = int(src.shape[1] * scale_percent/100)
new_height = int(src.shape[0] * scale_percent/100)

output = cv2.resize(src, (new_width,new_height))

cv2.imwrite('newImage.png',output)
cv2.waitKey(0)

# cv2.imshow("title",src)
# cv2.waitKey(0)