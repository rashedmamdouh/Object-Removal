import matplotlib.pyplot as plt
from PIL import Image
import sys

def display_output_image(output_path, original_image_path):
    img_out = Image.open(output_path)
    original_image = Image.open(original_image_path)
    original_size = original_image.size
    img_out_resized = img_out.resize(original_size)

    plt.imshow(img_out_resized)
    plt.axis('off')
    plt.show()
    print("Displayed the final output image.")

if __name__ == "__main__":
    display_output_image(sys.argv[1], sys.argv[2])
