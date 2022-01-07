import cv2
import numpy as np

def play_video(path):
    
    cap = cv2.VideoCapture(path)
    
    if cap.isOpened() == False:
        print("Fail to open the video")
        
    
    while(cap.isOpened()):
        
        ret,frame = cap.read()
        
        if ret == True:
            
            cv2.imshow("frame", frame)
            
            if cv2.waitKey(25) & 0XFF == ord('q'):
                break
        else:
            break
    
    cap.release()
    cv2.destroyAllWindows()


play_video("/home/sfm/Downloads/t1.mp4")
