import skimage as ski
import matplotlib.pyplot as plt

image = ski.io.imread('img/Cat03.jpg')
""" gaussian_filters = ski.filters.gaussian(image,sigma=5,mode='nearest')

ski.io.imshow(gaussian_filters)
ski.io.show() """

#reflect: Extiende la imagen reflejando los pixeles de los  bordes
#nearest: Extiende la imagen copiando los pixeles del borde mas cercano
#constat: Extiende la imagen con un valor constante por defecto es 0
#Wrap:    Extiende la imagen envolviendo los pixeles del borde apuesto
modes = ['reflect','nearest','constant','wrap']

#Craer un linezo para mostrar las imagenes en una sola ventana
fig, axes = plt.subplots(nrows=2, ncols=2)
axes = axes.flatten()

for i, mode in enumerate(modes):
    gaussian_image = ski.filters.gaussian(image, sigma=5,mode=mode)
    axes[i].imshow(gaussian_image)
    axes[i].set_title(f'Modo:{mode}')
    axes[i].axis('off')

plt.tight_layout()
plt.show()