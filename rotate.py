import cv2
import imutils
class rotate:
 	
	def __init__(self,img,ang):
		image = cv2.imread(img)
		 
		rot = imutils.rotate(image, angle=ang)
		cv2.imshow("Rotated", rot)
		cv2.waitKey(0)
