import json
import numpy as np
import os
from keras.models import load_model

# Paths to resources
# Find project root (assumes this file is in a subdirectory of the project)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
FIR_PATH = os.path.join(PROJECT_ROOT, 'dependencies', 'fir', 'foxhole', 'infantry-61')
CATALOG_PATH = os.path.join(FIR_PATH, 'catalog.json')
MODEL_PATH = os.path.join(FIR_PATH, 'classifier', 'model.json')  # TensorFlow.js format, needs conversion
CLASS_NAMES_PATH = os.path.join(FIR_PATH, 'classifer', 'class_names.json')

print(CATALOG_PATH)

# Load catalog
with open(CATALOG_PATH, 'r', encoding='utf-8') as f:
    catalog = json.load(f)

# Load class names
with open(CLASS_NAMES_PATH, 'r', encoding='utf-8') as f:
    class_names = json.load(f)

# NOTE: TensorFlow.js models must be converted to SavedModel or HDF5 for use in Python.
# You cannot load model.json directly in tf.keras. Use tensorflowjs_converter first.
# Example: tensorflowjs_converter --input_format=tfjs_graph_model model.json ./converted_model
MODEL_CONVERTED_PATH = './converted_model'

if os.path.exists(MODEL_CONVERTED_PATH):
    # Try loading as SavedModel directory
    try:
        model = load_model(MODEL_CONVERTED_PATH)
    except Exception as e:
        print(f'ERROR: Failed to load model from {MODEL_CONVERTED_PATH}: {e}')
        model = None
else:
    print('ERROR: Please convert the TensorFlow.js model to SavedModel format using tensorflowjs_converter.')
    model = None

# Example function to run inference on a 32x32 grayscale image
# image_array should be shape (32, 32, 1), dtype float32, normalized as needed

def predict_quantity(image_array):
    if model is None:
        raise RuntimeError('Model not loaded.')
    image_array = np.expand_dims(image_array, axis=0)  # Add batch dimension
    preds = model.predict(image_array)
    idx = np.argmax(preds[0])
    return class_names[idx]

# Example usage:
# image_array = ... # Load and preprocess your image here
# quantity = predict_quantity(image_array)
# print('Predicted quantity:', quantity)

# You can also use catalog for item lookups as needed.
