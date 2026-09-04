import cv2

IMAGE_PATHS = [
    "../Images/sample1.jpg",
    "../Images/sample2.jpg",
]

for path in IMAGE_PATHS:
    # Load the image from disk
    image = cv2.imread(path)

    if image is None:
        print(f"Error: could not load image at '{path}'")
        continue

    print(f"Loaded '{path}' successfully! Shape: {image.shape}")

    cv2.imshow(path, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
