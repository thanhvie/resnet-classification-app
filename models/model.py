import numpy as np

from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

# Load the model
model = load_model('models/model_resnet.h5')


def model_predict(img_path):
    """
    Function to process image and get prediction result from model
    :param img_path: image path in uploads folder
    :return result: prediction result from resnet model
    """
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x, mode='caffe')

    preds = model.predict(x)

    # Process result for human
    pred_class = decode_predictions(preds, top=1)
    result = str(pred_class[0][0][1])
    return result
