# Color Detection using OpenCV

This Python script captures video from the default camera, analyzes the color at the center of each frame in real-time, and displays the detected color on the frame.

## Prerequisites

- Python 3.x
- OpenCV (cv2) library

## Usage

1. Make sure you have Python installed on your system.

2. Install the required libraries using the following command:

   pip install opencv-python
Run the script using the following command:

Copy code
python ColorDetection.py
Press the 'ESC' key to exit the program.

Notes
The script uses the Hue value of the pixel at the center of the frame to determine the color.
The detected color is displayed as text on the video frame.
A circle is drawn at the center of the frame for reference.
