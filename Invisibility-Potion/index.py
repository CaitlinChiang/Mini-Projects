from capture_background import capture_background
from invisibility_cloak import apply_invisibility_cloak
import numpy as np

# Capture the background image
background_image = capture_background()

# Define the range for red color in HSV
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# Apply the invisibility cloak effect
if background_image is not None:
    apply_invisibility_cloak(background_image, lower_red1, upper_red1, lower_red2, upper_red2)
else:
    print("Failed to capture background.")
