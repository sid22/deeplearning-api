import pickle

import numpy as np
import scipy
from PIL import Image
from scipy import ndimage

from .tf_utils import predict


def model2_predictor(fname):
    parameters = pickle.load(open("model2.pkl", "rb"))
    image = np.array(ndimage.imread(fname, flatten=False))
    my_image = scipy.misc.imresize(image, size=(64,64)).reshape((1, 64*64*3)).T
    my_image_prediction = predict(my_image, parameters)
    return str(np.squeeze(my_image_prediction))
