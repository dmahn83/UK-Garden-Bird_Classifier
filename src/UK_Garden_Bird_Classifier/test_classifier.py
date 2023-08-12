# Import necessary libraries
import os
import random
import matplotlib.pyplot as plt

# Import class_names from bird_classes and classify_bird function from classifier
from UK_Garden_Bird_Classifier import bird_classes
from UK_Garden_Bird_Classifier.classifier import classify_bird

test_class_names = bird_classes.class_names

# Generate test cases for each class
test_cases = []
for class_name in test_class_names:
    random_int = random.randint(1, 5)  # Generate a random integer between 1 and 5 (inclusive) for the file names
    current_directory = os.getcwd()
    image_path = os.path.join('/test_images', f'{class_name} ({random_int}).jpg')
    full_image_path = os.path.join(current_directory, image_path)
    test_case = {'image_path': image_path, 'expected_class': class_name}
    test_cases.append(test_case)


# Function to display the test result and prediction on the image
def __display_test_result(img_path: str, base_truth: str, prediction: str, confidence: float):
    """
    Displays the test result and prediction on the image.
    :param img_path: Path to the image file.
    :param base_truth: The expected class (ground truth).
    :param prediction: The predicted class from the classifier.
    :param confidence: The confidence score of the prediction.
    """

    # Load and display the image using matplotlib
    img = plt.imread(img_path)

    # Display the predicted class and test result as a title

    # Check if image paths contain '5' - tests for false positives
    # '5' images do not represent the class of bird for which they have been named.
    if '5' not in img_path:
        plt.text(1, 1124, f"{img_path} is a {base_truth}", fontsize=10)
        if base_truth == prediction:
            title = f"TEST FOR TRUE POSITIVE - PASSED\n  Predicted Class: {prediction}, Confidence: {int(100 * confidence)}%"
        else:
            title = f"TEST FOR TRUE POSITIVE - FAILED\n Predicted Class: {prediction}, Confidence: {int(100 * confidence)}%\n Actual Class: {base_truth}"
    else:
        plt.text(1, 1074, f"{img_path} is not a {base_truth}", fontsize=10)
        if base_truth != prediction:
            title = f"TEST FOR FALSE POSITIVE - PASSED\n Predicted Class: {prediction}, Confidence: {int(100 * confidence)}%"
        else:
            title = f"TEST FOR FALSE POSITIVE - TEST FAILED\n Predicted Class: {prediction}, Confidence: {int(100 * confidence)}%"

    # Create a full-screen figure
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()


# Function to run test cases
def run_test_cases():
    """
    Classifies 1 test cases for each class in test_images and displays the results.
    """
    for test_img in test_cases:
        test_img_path = test_img['image_path']
        base_truth = test_img['expected_class']

        # Call the classify_bird function, which returns the predicted class and confidence score
        predicted_class, predicted_confidence = classify_bird(test_img_path)

        # Pass the predicted class, ground truth, and confidence score to the display function
        __display_test_result(test_img_path, base_truth, predicted_class, predicted_confidence)
