import numpy as np
import matplotlib.pyplot as plt
import pylab
import imageio
#import skimage.io
import cv2

if __name__=='__main__':
	cap = cv2.VideoCapture('/home/yman/demo.mp4');

	while(cap.isOpened()):
		ret, frame = cap.read()
		cv2.imshow('image',frame);
		k = cv2.waitKey(5)
	
		if(k & 0xff == ord('q')):
			break
	cap.release
	cv2.destroyAllWindows()
	
