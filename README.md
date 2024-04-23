# Python Image Processing - CamScanner Clone

## Overview
This project demonstrates the basics of image processing in Python, simulating functionalities similar to those of a mobile CamScanner application. It includes transforming images to correct perspective, applying grayscale and custom filters, and scaling images. The program utilizes Python libraries such as NumPy, PIL, and Matplotlib to process and visualize the transformations.

## Features
- **Perspective Transformation**: Corrects the perspective of images to simulate a flat scanner effect.
- **Filter Application**: Implements grayscale and custom filters to manipulate images.
- **Image Scaling**: Adjusts the size of the image without altering its content.
- **Custom Filter Effects**: Provides functionalities to apply unique filters that can invert colors or apply complex transformations.

## Prerequisites
To run this project, you must have Python installed along with the following libraries:
- NumPy
- PIL (Pillow)
- Matplotlib

## Usage
To use the image processing functionalities, run the `main.py` file. The script will apply a series of transformations to an input image specified by the path in the script. Ensure to place an image file named `pic.jpg` in the project directory or modify the path in the script to match your image's location.

### Example Usage
1. **Perspective Warp**: Correct the perspective of an image to make it appear as if taken directly from above.
2. **Grayscale Filter**: Convert the image to grayscale using a uniform color weight.
3. **Crazy Filter**: Apply a predefined custom filter and its inversion to the image.
4. **Image Scaling**: Scale the image to different dimensions based on specified scale factors.
