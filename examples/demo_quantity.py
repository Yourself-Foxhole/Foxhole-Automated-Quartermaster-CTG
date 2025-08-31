import numpy as np
from PIL import Image
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))
from screenshot_parse.parse_screenshot import predict_quantity

# Example image path (replace with your own test image)
EXAMPLE_IMAGE_PATH = '../examples/test_quantity.png'

# Load and preprocess image
if not os.path.exists(EXAMPLE_IMAGE_PATH):
    print(f'Please add a test image at {EXAMPLE_IMAGE_PATH} (32x32 grayscale).')
else:
    img = Image.open(EXAMPLE_IMAGE_PATH).convert('L').resize((32, 32))
    img_array = np.array(img, dtype=np.float32)
    img_array = img_array / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=-1)  # Shape (32, 32, 1)

    # Run prediction
    quantity = predict_quantity(img_array)
    print('Predicted quantity:', quantity)
