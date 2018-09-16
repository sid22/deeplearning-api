import numpy as np
import scipy
from PIL import Image
from scipy import ndimage
from .dnn_app_utils_v3 import *
import pickle

def model1_predictor(fname, def_label):
    parameters = pickle.load(open("model1.pkl", "rb"))
    image = np.array(ndimage.imread(fname, flatten=False))
    num_px = 64
    my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((num_px*num_px*3,1))
    my_image = my_image/255.
    my_label_y = def_label
    my_predicted_image = predict(my_image, my_label_y, parameters)
    return str(np.squeeze(my_predicted_image))