from skimage.io import imread, imsave

def read_image(path, is_gray=False):
    ima = imread(path, as_gray = is_gray)
    return ima

def save_image(ima, path):
    imsave(path, ima)