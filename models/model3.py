import numpy as np
from PIL import Image
from keras.models import load_model
from keras.models import Model
from keras.preprocessing import image as kimg
from keras.applications.imagenet_utils import preprocess_input
from keras.models import load_model
from io import StringIO
import keras.backend as K

def model3_predictor(iimage):
    model = load_model('static/happy.h5')
    try:
        img = kimg.load_img(iimage, target_size=(64, 64))
    except Exception as e:
        print(e)
    # try:
    #     ikm = Image.open(iimage.stream)
    #     print("ikm")
    #     img = ikm.resize((64,64))
    #     print("img")
    # except Exception as e:
    #     print(e)
    x = kimg.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    t = model.predict(x)
    del img
    del x
    K.clear_session()
    return t