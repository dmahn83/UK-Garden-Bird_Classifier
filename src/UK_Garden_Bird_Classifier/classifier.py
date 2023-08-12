import math
import os

import tensorflow as tf
from PIL import Image, ImageOps

from UK_Garden_Bird_Classifier import bird_classes

# Define the paths to the model and weights files
root_directory = os.path.dirname(os.path.abspath(__file__))
models_directory = os.path.join(root_directory, '/model')
model_path: str = os.path.join(models_directory, 'ft_ResNet50V2_20_UK_Garden_Birds.keras')
weights_path: str = os.path.join(models_directory, 'ft_ResNet50V2_20_UK_Garden_Birds_weights.h5')

# Load the model architecture
model = tf.keras.models.load_model(model_path)

# Load the model weights
model.load_weights(weights_path)


def classify_bird(image_path: str) -> tuple:
    """
    Classifies the bird in the given image and returns the predicted class and confidence score.
    :param image_path: Path to the image file.
    :return: A tuple containing the predicted class and confidence score.
    """
    # Load and preprocess the image
    img = Image.open(image_path).convert('RGB')

    # Pad the shortest dimension to ensure aspect ratio is retained after resize
    width, height = img.size
    if width != height:
        max_dim = max(width, height)
        pad_left = int((max_dim - width) / 2)
        pad_top = int((max_dim - height) / 2)
        pad_right = max_dim - width - pad_left
        pad_bottom = max_dim - height - pad_top
        img = ImageOps.pad(img, (pad_left, pad_top, pad_right, pad_bottom), color='white')

    # Resize the image to (224, 224)
    img = img.resize((224, 224))

    # Convert the image to an array and preprocess it
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = img_array.reshape((1, *img_array.shape))
    img_array /= 255.0

    # Perform the prediction
    prediction = model.predict(img_array)
    class_idx = prediction.argmax()

    predicted_class = bird_classes.class_names[class_idx]
    confidence_score = prediction[0][class_idx]  # Access the prediction score at the class_idx
    confidence_score = math.floor(confidence_score * 100) / 100  # Round the confidence score to 2 decimal places

    return predicted_class, confidence_score
