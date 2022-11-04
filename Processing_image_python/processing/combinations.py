import numpy as np
from skimage.color import rgb2gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity

def find_diference (ima1, ima2):
    assert ima1.shape == ima2.shape, "2 imagens com a mesma forma."
    ima_gray1 = rgb2gray(ima1)
    ima_gray2 = rgb2gray(ima2)
    (score, image_difference) = structural_similarity(ima_gray1, ima_gray2, full=True)
    print("Similariedade de: ", score)
    image_difference_normal = (image_difference-np.min(image_difference))/(np.max(image_difference)-np.min(image_difference))
    return image_difference_normal

def transferir_histograma(ima1, ima2):
    corresponding_ima = match_histograms(ima1, ima2, multichannel=True)
    return corresponding_ima