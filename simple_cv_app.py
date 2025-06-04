import cv2
import sys


def main(image_path: str, output_path: str = "edges.png"):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image {image_path}")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Save the result
    cv2.imwrite(output_path, edges)
    print(f"Edge detection complete. Output saved to {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simple_cv_app.py <image_path> [output_path]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else "edges.png"
    main(image_path, output_path)
