import cv2

# Specify the camera port (0 for the default camera)
cam_port = 0

# Initialize the camera
cam = cv2.VideoCapture(cam_port)

# Check if the camera opened successfully
if not cam.isOpened():
    print("Error: Could not open the camera.")
else:
    # Read a frame from the camera
    ret, frame = cam.read()

    # Check if the frame was captured successfully
    if ret:
        # Display the frame (you can remove this line if you don't need to display it)
        cv2.imshow("Camera Frame", frame)
        
        # Provide a brief delay to display the frame (milliseconds)
        cv2.waitKey(2000)  # Adjust the delay time as needed
        
        # Save the captured frame as an image (you can change the filename and format)
        inp = input('Enter person name: ')
        filename = inp + ".png"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")

        # Release the camera
        cam.release()
        cv2.destroyAllWindows()
    else:
        print("Error: Could not capture a frame from the camera.")

# Release the camera (in case it's still open)
cam.release()
cv2.destroyAllWindows()
