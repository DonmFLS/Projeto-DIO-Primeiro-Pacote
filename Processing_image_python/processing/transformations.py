from skimage.transform import resize

def resize_image(ima, proportion):
    assert 0 <= proportion <= 1, "Especifique entre 0 e 1."
    height = round(ima.shape[0] * proportion)
    width = round(ima.shape[1] * proportion)
    ima_rezised = resize(ima, (height, width), anti_aliasing=True)
    return ima_rezised