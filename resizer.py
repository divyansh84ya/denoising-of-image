import cv2

class resize:
	def __init__(selg,img,si1,si2):
		img=cv2.imread(img)
		img=cv2.resize(img,(si1,si2))
		cv2.imshow("Resize Image", img)
		cv2.waitKey(0)
		cv2.destroyAllWindows()
