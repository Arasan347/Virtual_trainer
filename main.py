import cv2
import mediapipe as mp
import time
import numpy as np
pTime = 0

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Calculating angles for bicep curls
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle


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

        # Calculating angle
        angle = calculate_angle(shoulder, elbow, wrist)

        # showing co-ordinates
        cv2.putText(frame, str(angle),
                    tuple(np.multiply(elbow, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    )
        print(landmarks)
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