
import skimage as ski
import matplotlib.pyplot as plt

image = ski.io.imread('img/fruta2.jpg')

gray_image = ski.color.rgb2gray(image)

thresh = ski.filters.threshold_otsu(gray_image)

binary = gray_image> thresh

#Limpiar la imagen binaria para eliminar el ruido
cleared = ski.morphology.remove_small_objects(binary,min_size=200)

""" ski.io.imshow(cleared)
ski.io.show() """

""" plt.imshow(cleared,cmap='gray')
plt.title('Segmentacion por threshold')
plt.show() """

lab_image = ski.color.rgb2lab(image)
segments = ski.segmentation.slic(lab_image,n_segments=100,compactness=10)
segmentacion= ski.color.label2rgb(segments,image,kind='avg')
ski.io.imshow(segmentacion)
ski.io.show()


