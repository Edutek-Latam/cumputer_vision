import skimage as ski
import matplotlib.pyplot as plt

image = ski.io.imread('img/fruta2.jpg')
gray = ski.color.rgb2gray(image)

sobel_filter = ski.filters.sobel(gray,)

ski.io.imshow(sobel_filter)
ski.io.show()