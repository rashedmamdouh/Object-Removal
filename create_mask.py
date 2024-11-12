import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

def create_white_mask(image_path, output_path):
    # Load the original image
    image = cv2.imread(image_path)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of colors to mask
    lower_color1 = np.array([0, 120, 70])
    upper_color1 = np.array([10, 255, 255])
    lower_color2 = np.array([170, 120, 70])
    upper_color2 = np.array([180, 255, 255])

    # Create and merge masks
    mask1 = cv2.inRange(hsv_image, lower_color1, upper_color1)
    mask2 = cv2.inRange(hsv_image, lower_color2, upper_color2)
    mask = cv2.bitwise_or(mask1, mask2)
    white_mask = cv2.merge([mask, mask, mask])

    cv2.imwrite(output_path, white_mask)
    print(f"White mask saved at {output_path}")

if __name__ == "__main__":
    create_white_mask(sys.argv[1], sys.argv[2])
