import time
import numpy as np
import h5py
import scipy
from PIL import Image
from scipy import ndimage
from .dnn_app_utils_v3 import *
import pickle

def model1_predictor(fname, def_label):
    print ("kasdasd")
    try:
        parameters = pickle.load(open("model.pkl", "rb"))
    except Exception as e:
        print (e)
    print ("mod loaded")
    image = np.array(ndimage.imread(fname, flatten=False))
    print ("qqqqqqqq")
    num_px = 64
    try:
        my_image = scipy.misc.imresize(image, size=(num_px,num_px)).reshape((num_px*num_px*3,1))
    except Exception as e:
        print (e)
    print ("wwwwwwww")
    my_image = my_image/255.
    print ("eeeeeeeee")
    my_label_y = def_label
    try:
        my_predicted_image = predict(my_image, my_label_y, parameters)
    except Exception as e:
        print (e)
    return str(np.squeeze(my_predicted_image))