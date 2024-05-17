#this is a secirty camera made on python using opencv and playsound library


import cv2  # Import the OpenCV library for image processing
from playsound import playsound  # Import the playsound library for sound playback

webcam = cv2.VideoCapture(0)  # Initialize the webcam for capturing video (0 indicates the default webcam)

# Initialize the flag for motion detection
motion_detected = False  # This flag will be set to True when motion is detected

while True:  # Loop continuously until explicitly terminated
    _, im1 = webcam.read()  # Capture a frame from the webcam and store it in im1
    _, im2 = webcam.read()  # Capture another frame from the webcam and store it in im2
    diff = cv2.absdiff(im1, im2)  # Compute the absolute difference between the two frames to detect motion
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # Convert the difference image to grayscale
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)  # Apply a binary threshold to the grayscale image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # Find contours in the thresholded image
    
    for c in contours:  # Iterate over each contour found in the image
        if cv2.contourArea(c) < 5000:  # Check if the contour area is smaller than a threshold (to filter out noise)
            continue  # Skip this contour if it's too small
        # Set the flag to True if motion is detected
        motion_detected = True  # Set the motion_detected flag to True if a contour with sufficient area is found
    
    # If motion is detected, play the sound
    if motion_detected:
        playsound("/Users/ameshajid/Documents/VisualStudioCode/Sign Language Letters Detection/beep-01a.mp3")
        # Reset the flag to False to prepare for the next motion detection
        motion_detected = False  # Reset the motion_detected flag after playing the sound
        
    cv2.imshow("Security camera", thresh)  # Display the thresholded image in a window titled "Security camera"
    
    # Check for key press to exit the loop (27 is the ASCII code for the Esc key)
    if cv2.waitKey(1) & 0xFF == 27:
        break  # Exit the loop if the Esc key is pressed

webcam.release()  # Release the webcam
cv2.destroyAllWindows()  # Close all OpenCV windows

