import tflite_runtime.interpreter as tflite
import numpy as np

from io import BytesIO
from urllib import request
from PIL import Image

# define methods

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def preprocess_input(x):
    return x / 255

# initialize and loading model :

interpreter = tflite.Interpreter(model_path='bees-wasps-v2.tflite') # edited with the new model pulled with the docker
interpreter.allocate_tensors()  
input_index = interpreter.get_input_details()[0]['index']  # get INPUT index 
output_index = interpreter.get_output_details()[0]['index'] # get OUTPUT index 

def predict(url):

	img = prepare_image(download_image(url),(150,150))
	
	x = np.array(img, dtype='float32')
	X = np.array([x])
	X = preprocess_input(X)
	
	interpreter.set_tensor(input_index, X) 
	interpreter.invoke() 
	preds = interpreter.get_tensor(output_index)

	wasp_probability = ['Wasp_probability']
	
	return dict(zip(wasp_probability, preds[0].tolist()))


def lambda_handler(event, context):
	url = event['url']
	result = predict(url)
	return result
