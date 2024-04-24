import numpy as np
import cv2
import pyautogui

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

resolution = (1280, 720)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "Recording.avi"

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live", 960, 540)  

try:
    while True:
        
        
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert frame to grayscale for face detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Write frame to the output video
        out.write(frame)

        # Display the recording screen
        cv2.imshow('Live', frame)
        
        # Stop recording when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

except KeyboardInterrupt:
    pass

# Release the VideoWriter object
out.release()

# Destroy all windows
cv2.destroyAllWindows()
