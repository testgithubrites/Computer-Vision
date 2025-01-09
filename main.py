'''import cv2

for i in range(5):  # Try checking up to 5 camera indices
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i} is available")
        cap.release()
    else:
        print(f"Camera {i} is not available")'''

import cv2

cap = cv2.VideoCapture(0);
while True: #This is an infinite loop to keep capturing video frame by frame until the user stops it.
    ret , frame = cap.read()
    cv2.imshow('frame',frame)
    #cap.read() captures a single frame from the webcam.
    #ret (boolean) → True if the frame was captured successfully, otherwise False.
    #frame → Stores the actual image (frame) captured from the video.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() #Releases the webcam resource (stops video capture).
cv2.destroyAllWindows() #Closes all OpenCV windows.

#Hue - Represents color itself.