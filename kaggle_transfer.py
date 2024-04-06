# load_model.py

import numpy as np
import tensorflow as tf
import tensorflow_text as text
import tensorflow_hub as hub
import os


def load_model(model_path):
	"""
	Loads the model from the given path.
    :param model_path:
    :return:
    """
	load_model = tf.saved_model.LoadOptions(experimental_io_device='/job:localhost')
	model = tf.keras.models.load_model(model_path, custom_objects={'KerasLayer':hub.KerasLayer},
                                       options=load_model)
	print("Model loaded successfully")
	return model
