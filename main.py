import cv2
import mediapipe as mp
import numpy

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
    print(result.pose_landmarks)
    if result.pose_landmarks:
        mp_draw.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_draw.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                              mp_draw.DrawingSpec(color=(42, 42, 165), thickness=2, circle_radius=2))

    # to display fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow('Video capture', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()