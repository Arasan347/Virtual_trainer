import cv2
import mediapipe as mp
import numpy

# with opencv capturing video
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    # to display fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow('Video capture', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()