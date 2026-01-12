import cv2

#Read images (basic)

img = cv2.imread('lena.jpg' , 1) # 0(grayscale) , 1(colored) , -1(alpha channel)
print(img)
cv2.imshow('image' , img)
k = cv2.waitKey()
if k == 27:
   cv2.destroyAllWindows()
elif k == ord('s'):  #Save the image with tha name copied_image
    cv2.imwrite('copied_image.png' , img)
    cv2.destroyAllWindows()
