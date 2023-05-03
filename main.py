import cv2
import mediapipe as mp
import time
import numpy
pTime = 0

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# with opencv capturing video
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    # convert BGR to RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = pose.process(imgRGB)

    # convert image from RGB to BGR
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Extract landmarks in body
    try:
        landmarks = result.pose_landmarks.landmark
        shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
    except:
        pass


    if result.pose_landmarks:
        mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_draw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_draw.DrawingSpec(color=(42, 42, 165), thickness=2, circle_radius=2))

    # to display fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow('Video capture', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()