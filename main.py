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

class Bicep_curl:
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

    def calculate_angle2(a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle2 = np.abs(radians * 180.0 / np.pi)

        if angle2 > 180.0:
            angle2 = 360 - angle2

        return angle2


    file_name = "video.webm"
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

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

            # Calculating angle
            angle = calculate_angle(shoulder, elbow, wrist)


            # showing co-ordinates
            cv2.putText(frame, str(angle),
                        tuple(np.multiply(shoulder, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA
                        )


            # Curl counter logic
            if angle > 160:
                stage = "down"
            if angle < 30 and stage == 'down':
                stage = "up"
                count += 1
            # print(count)

            shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            angle2 = calculate_angle2(shoulder, elbow, hip)

            # showing feedback
            if angle2 < 140:
                time_string_good = 'bad Posture'
                cv2.putText(frame, time_string_good, (10, 300), font, 0.9, (50, 50, 255), 2)
            else:
                time_string_bad = 'good Posture'
                cv2.putText(frame, time_string_bad, (10, 300), font, 0.9, (127, 255, 0), 2)
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