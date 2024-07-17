import cv2
import numpy as np

def capture_background(duration=3, frame_width=640, frame_height=480):
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return None

    # Calculate the number of frames to capture over the given duration
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    total_frames = duration * fps
    frames = []

    print("Capturing background, please wait...")

    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            return None
        frames.append(frame)

    # Release the camera
    cap.release()

    # Calculate the average frame to get the background
    background = np.mean(frames, axis=0).astype(np.uint8)

    return background
