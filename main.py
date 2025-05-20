import cv2
cap = cv2.VideoCapture('wildlife_video.mp4') 
# Read the first frame for background comparison
ret, frame1 = cap.read()
ret, frame2 = cap.read()
while cap.isOpened():
  # Calculate difference between two frames
  	  diff = cv2.absdiff(frame1, frame2)
  	  gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
 # Blur to reduce noise
  	  blur = cv2.GaussianBlur(gray, (5, 5), 0)
# Threshold to get motion areas
   	  thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
 dilated = cv2.dilate(thresh, None, iterations=3)
     # Find contours (moving objects)
 contours, _ = cv2.findContours(dilated,
cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     # Draw bounding boxes around detected motion
   	 for contour in contours:
      		  if cv2.contourArea(contour) < 1000:  # Ignore small movements
           	 continue
        	x, y, w, h = cv2.boundingRect(contour)
        	cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.putText(frame1, 'Movement Detected', (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
    # Show the output
    	cv2.imshow("Wildlife Monitoring", frame1)
    # Update frames
    	frame1 = frame2
    	ret, frame2 = cap.read()	
    # Exit on 'q' key
    	if cv2.waitKey(10) == ord('q'):
        	break
cap.release()
cv2.destroyAllWindows()
