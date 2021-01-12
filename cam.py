#For importing cv2 use command: pip install opencv-python
import cv2 

'''This function helps to read the webcam feed and display it.
   Webcam_index identifies which webcam is in use, 
   incase of just one webcamindex is equal to 0 '''
def webcam_read(webcam_index=0):

	video = cv2.VideoCapture(webcam_index)	  #video is an object of VideoCapture  

	while(video.isOpened()):

		ret, frame = video.read()             #ret holds boolean value while frame stores the frame of the video
		
		cv2.imshow('frame', frame)            #Displays the frame

		if cv2.waitKey(1) & 0xFF == ord('q'): #q key can be pressed to exit and waitKey(1) shows a frame for 1 ms only 
			break
	video.release()
	cv2.destroyAllWindows()

