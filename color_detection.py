import cv2

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Set the frame width and height
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # Read a frame from the camera
    _, frame = cap.read()

    # Convert the frame to HSV (Hue, Saturation, Value) color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the height, width, and channels of the frame
    height, width, _ = frame.shape

    # Calculate the center coordinates of the frame
    cx = int(width / 2)
    cy = int(height / 2)

    # Get the HSV value of the pixel at the center of the frame
    pixel_center = frame[cy, cx]
    hue_value = pixel_center[0]

    # Determine the color based on the hue value
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"

    # Get the BGR value of the pixel at the center of the frame
    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    # Display the color text on the frame
    cv2.putText(frame, color, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (b, g, r), 2)

    # Draw a circle at the center of the frame
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    # Display the frame
    cv2.imshow("Frame", frame)

    # Check for the ESC key to exit the loop
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the camera
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
