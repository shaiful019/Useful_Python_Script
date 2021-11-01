# Read the video from specified path
import cv2
cap = cv2.VideoCapture('20210929_20210929132851_20210929140029_132852.mp4')


#cap.set(1, 27000)
#cap.set(1, 16000)


fps = cap.get(cv2.CAP_PROP_FPS)
totalNoFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT);
durationInSeconds = float(totalNoFrames) / float(fps)

# currentframe = 0
print(totalNoFrames)

# frame_save_location = "frame"

