import cv2

# Create a VideoCapture object to read from the webcam
video_capture = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not video_capture.isOpened():
    print("Failed to open camera")
    exit()

# Get the camera properties and print their current values
properties = [
    (cv2.CAP_PROP_EXPOSURE, "Exposure"),
    (cv2.CAP_PROP_GAIN, "Gain"),
    (cv2.CAP_PROP_SHARPNESS, "Sharpness"),
    (cv2.CAP_PROP_BACKLIGHT, "Backlight"),
    # Add more camera properties if needed
]

for prop_id, prop_name in properties:
    prop_value = video_capture.get(prop_id)
    print(f"{prop_name}: {prop_value}")

# Release the VideoCapture
video_capture.release()
