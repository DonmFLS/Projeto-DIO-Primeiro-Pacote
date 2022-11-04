import matplotlib.pyplot as plt


def plt_image(ima):
    plt.figure(figsize = (12, 4))
    plt.imshow(ima, cmap = 'gray')
    plt.axis('off')
    plt.show()

def plot_results(*args):
    ima_numbers = len(args)
    fig, axis = plt.subplots(nrows = 1, ncols = ima_numbers, figsize = (12, 4))
    names_lst = ['image {}'.format(i) for i in range(1, ima_numbers)]
    names_lst.append('Resultado')
    for ax, nome, ima in zip(axis, names_lst, args):
        ax.set_title(nome)
        ax.inshow(ima, cmap='gray')
        ax.axis('off')
    fig.tight_layout()
    plt.show()

def plot_histogram(ima):
    fig, axis = plt.subplots(nrows = 1, ncols = 3, figsize = (12, 4), sharex = True, sharey = True)
    color_lst = ['red', 'green', 'blue']
    for index, (ax, color) in enumerate(zip(axis, color_lst)):
        ax.set_title('{} Histogram'.format(color.title()))
        ax.hist(ima[:, :, index].ravel(), bins = 256, color = color, alpha = 0.8)
    fig.tight_layout()
    plt.show()