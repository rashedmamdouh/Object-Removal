import sys
import subprocess

def run_inpainting(image_path, mask_path, output_path, checkpoint_path):
    command = [
        "python", "test.py",
        "--image", image_path,
        "--mask", mask_path,
        "--out", output_path,
        "--checkpoint", checkpoint_path
    ]
    subprocess.run(command)
    print(f"Model output saved at {output_path}")

if __name__ == "__main__":
    run_inpainting(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
