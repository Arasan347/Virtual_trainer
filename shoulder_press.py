import math

import cv2
import mediapipe as mp
import time
import numpy as np
pTime = 0

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


# font type
font = cv2.FONT_HERSHEY_SIMPLEX


# Calculating angles for bicep curls
def calculate_angle(a, b, c, d, e, f):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    e = np.array(e)
    f = np.array(f)

    left_Angle = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle1 = np.abs(left_Angle * 180.0 / np.pi)

    if angle1 > 180.0:
        angle1 = 360 - angle1

    right_Angle = np.arctan2(f[1] - e[1], f[0] - e[0]) - np.arctan2(d[1] - e[1], d[0] - e[0])
    angle2 = np.abs(right_Angle * 180.0 / np.pi)

    if angle2 > 180.0:
        angle2 = 360 - angle2



    return angle1



file_name = "shoulder_press.mp4"
# with opencv capturing video
cap = cv2.VideoCapture(file_name)

# curl count
count = 0
stage = None

while True:
    ret, frame = cap.read()

    # get height and width
    # h, w = frame.shape[:2]

    # convert BGR to RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = pose.process(imgRGB)

    # convert image from RGB to BGR
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Extract landmarks in body
    try:
        landmarks = result.pose_landmarks.landmark

        left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
        left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
        left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                         landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                      landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        # Calculating angle
        angle = calculate_angle(left_shoulder, left_elbow, left_wrist, right_shoulder, right_elbow, right_wrist)


        # showing co-ordinates
        cv2.putText(frame, str(angle),
                    tuple(np.multiply(left_shoulder, [640, 480]).astype(int)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                    )


        # Curl counter logic
        if angle > 160:
            stage = "down"
        if angle < 50 and stage == 'down':
            stage = "up"
            count += 1
        # print(count)

    except:
        pass

    # display counts in display
    # Rep data
    cv2.putText(frame, 'REPS', (15, 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, str(count),(10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2, cv2.LINE_AA)




    if result.pose_landmarks:
        mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_draw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_draw.DrawingSpec(color=(42, 42, 165), thickness=2, circle_radius=2))

    # to display fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(frame, str(int(fps)), (100, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow('Video capture', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()