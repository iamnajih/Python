import cv2
import mediapipe as mp
import pyautogui
cam=cv2.VideoCapture(0)
face=mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h=pyautogui.size()
while True:
    _, frame=cam.read()
    frame=cv2.flip(frame, 1)
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out=face.process(frame)
    land=out.multi_face_landmarks
    frame_h, frame_w, _ =frame.shape
    if land:
        landm=land[0].landmark
        for id, landmark in enumerate(landm[474:478]):
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,0))
            if id==1:
                screenx=screen_w * landmark.x
                screeny=screen_h * landmark.y
                pyautogui.moveTo(screenx, screeny)
        left=[landm[145], landm[159]]
        for landmark in left:
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0,255,255))
        if (left[0].y-left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(1)==13:
        break











                
