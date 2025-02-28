import skimage as ski
import matplotlib.pyplot as plt

image = ski.io.imread('img/fruta2.jpg')
gray_image = ski.color.rgb2gray(image)
canny_filter = ski.feature.canny(gray_image,sigma=2)

ski.io.imshow(canny_filter)
ski.io.show()

