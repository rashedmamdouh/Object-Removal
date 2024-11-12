from PIL import Image
import sys

def resize_image(input_path, output_path, size=(1200, 1500)):
    image = Image.open(input_path)
    image = image.resize(size)
    image.save(output_path, 'PNG')
    print(f"Image resized and saved at {output_path}")

if __name__ == "__main__":
    resize_image(sys.argv[1], sys.argv[2])
