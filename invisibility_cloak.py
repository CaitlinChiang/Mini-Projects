import cv2
import numpy as np
import sys

def apply_invisibility_cloak(background, lower_red1, upper_red1, lower_red2, upper_red2, frame_width=640, frame_height=480):
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        sys.exit(1)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Create a mask for the red color
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = cv2.bitwise_or(mask1, mask2)

        # Invert the mask
        mask_inv = cv2.bitwise_not(mask)

        # Segment out the red part
        red_part = cv2.bitwise_and(frame, frame, mask=mask)

        # Segment out the non-red part
        non_red_part = cv2.bitwise_and(frame, frame, mask=mask_inv)

        # Replace the red part with the background
        background_part = cv2.bitwise_and(background, background, mask=mask)
        combined_frame = cv2.add(non_red_part, background_part)

        cv2.imshow('Invisibility Cloak', combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    sys.exit(0)  # Clean exit

