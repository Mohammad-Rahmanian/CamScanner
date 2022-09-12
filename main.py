import utils
from utils import *
import numpy as np


def warpPerspective(img, transform_matrix, output_width, output_height):
    warped_image = np.zeros((output_width, output_height, 3), dtype='int')
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            vector = np.full((3, 1), 1)
            vector[0][0] = i
            vector[1][0] = j
            vector = np.dot(transform_matrix, vector)
            new_x = int(vector[0][0] / vector[2][0])
            new_y = int(vector[1][0] / vector[2][0])
            if 0 <= new_x < output_width and 0 <= new_y < output_height:
                warped_image[new_x][new_y] = img[i][j]
    return warped_image


def grayScaledFilter(img):
    transformation_matrix = np.array([[1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3],
                                      [1 / 3, 1 / 3, 1 / 3]])
    gray_scaled_image = utils.Filter(img, transformation_matrix)
    return gray_scaled_image


def crazyFilter(img):
    transformation_matrix = np.array([[0, 0, 1],
                                      [0, 0.5, 0],
                                      [0.5, 0.5, 0]])
    crazy_filter_image = utils.Filter(img, transformation_matrix)
    inverted_crazy_filter_image = utils.Filter(crazy_filter_image, np.linalg.inv(transformation_matrix))
    return crazy_filter_image, inverted_crazy_filter_image


def scaleImg(img, scale_width, scale_height):
    scaled_image = np.zeros((scale_width * img.shape[0], scale_height * img.shape[1], 3), dtype='int')
    for i in range(img.shape[0] * scale_width):
        for j in range(img.shape[1] * scale_height):
            scaled_image[i][j] = img[int(i / scale_width)][int(j / scale_height)]
    return scaled_image


def permuteFilter(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            temp = img[i][j][2]
            img[i][j][2] = img[i][j][0]
            img[i][j][0] = temp
    return img


if __name__ == "__main__":
    image_matrix = get_input('pic.jpg')
    # You can change width and height if you want
    width, height = 300, 400
    showImage(image_matrix, title="Input Image")

    pts1 = np.float32([[260, 20], [590, 180], [250, 975], [620, 900]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    m = getPerspectiveTransform(pts1, pts2)
    warpedImage = warpPerspective(image_matrix, m, width, height)
    showWarpPerspective(warpedImage)

    grayScalePic = grayScaledFilter(warpedImage)
    showImage(grayScalePic, title="Gray Scaled")
    #
    crazyImage, invertedCrazyImage = crazyFilter(warpedImage)
    showImage(crazyImage, title="Crazy Filter")
    showImage(invertedCrazyImage, title="Inverted Crazy Filter")

    #
    scaledImage = scaleImg(warpedImage, 3, 4)
    showImage(scaledImage, title="Scaled Image")

    permuteImage = permuteFilter(warpedImage)
    showImage(permuteImage, title="Permuted Image")
