
# Image Loading with OpenCV

This project demonstrates how to load and display multiple images using the OpenCV (`cv2`) library in Python.

## Project Structure

```text
files/
│
├── images.py
│
├── images/
│   ├── sample1.jpg
│   └── sample2.jpg
│
└── README.md
````

## Description

The `images.py` program:

* Imports the OpenCV library.
* Loads images from the `images` folder.
* Checks whether each image was loaded successfully.
* Displays the images using OpenCV.
* Prints the image shape (height, width, and number of channels).
* Closes the image windows when a key is pressed.

## 🛠️ Requirements

Make sure Python is installed on your system.

Install OpenCV using:

```bash
pip install opencv-python
```

## How to Run

Open a terminal in the project folder and run:

```bash
python images.py
```

The program will load and display `sample1.jpg` and `sample2.jpg`.

Press any key while an image window is active to close the windows.

## Image Paths

The program uses relative paths to access the images:

```python
IMAGE_PATHS = [
    "images/sample1.jpg",
    "images/sample2.jpg",
]
```

Make sure the image names and folder name match exactly.

## Output

For each successfully loaded image, the program prints its path and shape, for example:

```text
Loaded 'images/sample1.jpg' successfully! Shape: (480, 640, 3)
Loaded 'images/sample2.jpg' successfully! Shape: (480, 640, 3)
```

The images are also displayed in separate OpenCV windows.

## Technologies Used

* Python
* OpenCV (cv2)

## Purpose

This project is a basic demonstration of image loading and visualization using OpenCV and can be used as a starting point for further image processing tasks.

````

**One important thing:** since your folder is named `images` and `images.py` is outside it, your paths should be:

```python
IMAGE_PATHS = [
    "images/sample1.jpg",
    "images/sample2.jpg",
]
````

—not `../Images/...`. Also note that Linux/GitHub is case-sensitive, so `images` and `Images` are treated as different folders.
