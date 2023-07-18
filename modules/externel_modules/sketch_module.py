from sketchpy import library as lib

# obj=lib.rdj()
# obj.draw()
#
# obj=lib.tom_holland()
# obj.draw()
#
# obj=lib.vijay()
# obj.draw()




















import cv2
image = cv2.imread(r'C:\Users\ANAGHA\PycharmProjects\pythoncourse\modules\externel_modules\PIC2.jpg') # loads an image from the specified file
# convert an image from one color space to another
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img) # helps in masking of the image
# sharp edges in images are smoothed while minimizing too much blurring
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=158.0)
cv2.imwrite("sketch.png", sketch) # converted image is saved as mentioned name
