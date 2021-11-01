# Read the video from specified path
import cv2
cap = cv2.VideoCapture('20210929_20210929125746_20210929131749_125747.mp4')


#cap.set(1, 27000)
#cap.set(1, 16000)


fps = cap.get(cv2.CAP_PROP_FPS)
totalNoFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT);
durationInSeconds = float(totalNoFrames) / float(fps)

currentframe = 0
# print(totalNoFrames)

frame_save_location = "frame2"



while(True): 
      
    # reading from frame 
    ret, frame = cap.read() 
    

    if ret: 

        #print()
        #print(cap.get(cv2.CAP_PROP_POS_FRAMES))
        cur_frame_num = int(cap.get(cv2.CAP_PROP_POS_FRAMES))


        ## Use object detection to get frames with only humans 
        #if currentframe > 13000:
        #  break

        ## Generate frame based on fps
        #if currentframe % round_fps == 0:
        if currentframe:

          ## skip frames
          #print(currentframe)


          ## crop part of image to avoid logo or undesired part
          #fsx, fsy = frame.shape
          #frame = frame[0:fsy - 100, 0:fsx]


          ## if video is still left continue creating images     
          name = frame_save_location + str(cur_frame_num) + '.jpg'
          #name = frame_save_location + str(currentframe) + '.jpg'
          print ('Creating...' + name) 


          # writing the extracted images 
          cv2.imwrite(name, frame) 


          ## skip every N frames
          cap.set(1, cur_frame_num + 30)


        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break

  
# Release all space and windows once done 
cap.release() 
cv2.destroyAllWindows() 
