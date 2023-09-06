## UK Garden Bird Classifier <hr> 
 Python library to classify images of the top 20 UK Garden Bird Species </br>

### INSTALLATION <hr>
The UK_Garden_Bird_Classifier module is installed directly from this repo.

```python
!pip install git+https://github.com/dmahn83/UK-Garden-Bird-Classifier.git
```

### USAGE <hr>

### TESTING THE INSTALLATION
The model displays a prediction for a single image for each class.  

```python
from UK_Garden_Bird_Classifier import test_classifier
test_classifier.run_test_cases()
```

Each class has 5 possible test cases (one is chosen at random for each class at each execution).<br>
**Images labeled (5)** e.g. test_images/Magpie (5).jpg are not representative of the class for which they are labelled.- **they are a test for false positive results**.  <br><br> 

### CLASSIFYING AN IMAGE
The model predicts the class of bird in a single image:

```python
from UK_Garden_Bird_Classifier import classifier
classifier.classify_bird(image_path)
```
`image_path` : String representing the image path<br />
`returns` : A tuple containing the predicted class and confidence e.g  [Magpie, 0.99]<br />


### DISCLAIMER<hr>

The ResNet50 V2 model used by this program has been trained to classify images containing a **single bird**, and can only identify the following species:<br/><br/>

`class_names=`  [
    "House_Sparrow", "Bluetit", "Starling", "Wood_Pigeon", "Blackbird", "Robin", "Goldfinch", "Great_Tit",
    "Magpie", "Long_Tailed_Tit", "Chaffinch", "Dunnock", "Jackdaw", "Feral_Pigeon", "Collared_Dove",
    "Carrion_Crow", "Coal_Tit", "Greenfinch", "Wren", "Song_Thrush"
]

### RESOURCES<hr>

We provide links to Kaggle notebooks and additional resources detailing the curation of the 20 UK Garden Bird dataset.  We also provide links to experiments and their results detailing the development of the augmented ResNet50V2 model used in this package:

- 20 UK Garden Birds Dataset Curation
  - Image procurement methodology - root/resources/Data_Collection_using_Bing_image_downloader.ipynb
  - Image processing methodology - https://www.kaggle.com/code/davemahony/1-20-uk-garden-bird-ds-prep-with-mask-rcnn  
  - Dataset analysis - .https://www.kaggle.com/code/davemahony/1-20-uk-garden-bird-ds-prep-with-mask-rcnn 

- 20 UK Garden Birds Experiments (Model Development)
  - Experiment 1 - We apply transfer learning to a ResNet50V2 model pretrained on the ImageNet dataset, using this as  the basis for transfer learning https://www.kaggle.com/code/davemahony/3-cnn-resnet-birds-525-species
  - Experiment 2 - We train a base model using the ResNet50V2 architecture to assess performance improvements. https://www.kaggle.com/code/davemahony/1-20-uk-garden-bird-ds-prep-with-mask-rcnn  
  - Experiment 3 - We apply transfer learning techniques to the initial model. https://www.kaggle.com/code/davemahony/5-20-uk-garden-birds-pretrained-resnet50v2 
  - Experiment 4 - We apply both transfer learning and image augmentation techniques to the initial model. https://www.kaggle.com/code/davemahony/6-20-uk-garden-birds-aug-pretrained-resnet5 
  - Experiment 5 - We apply both transfer learning and background removal techniques to the initial model. https://www.kaggle.com/code/davemahony/7-20-uk-garden-birds-nobg-pretrained-resnet5
  - Experiment Metrics per model - root/resources/20 UK Garden Bird Experiments/Model Metrics.xlsx
  - Experiment Predictions per model -root/resources/20 UK Garden Bird Experiments/Model Prediction .xlsx