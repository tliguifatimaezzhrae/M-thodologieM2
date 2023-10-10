import numpy as np

def pre_process(images, labels):
    train = np.empty((len(images), 128, 128))
    for i, image in enumerate(images):
        l = [value / 255.0 for value in image.convert('L').getdata()]
        for j in range (128):
            for k in range (128):
                train[i][j][k] = l[j*128+k]

    return train, np.array(labels)

def pre_process(images):
    train = np.empty((len(images), 128, 128))
    for i, image in enumerate(images):
        l = [value / 255.0 for value in image.convert('L').getdata()]
        for j in range (128):
            for k in range (128):
                train[i][j][k] = l[j*128+k]
    return train