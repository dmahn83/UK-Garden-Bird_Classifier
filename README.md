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

We provide links to Kaggle notebooks and additional resources detailing the curation of the 20 UK Garden Bird dataset.  We also proveide links to experiments and their results detailing the development of the augmented ResNet50V2 model used in this package:

- 20 UK Garden Birds Dataset
  - Image procurement methodology - root/resources/Data_Collection_using_Bing_image_downloader.ipynb
  - Image processing methodology - https://www.kaggle.com/code/davemahony/1-20-uk-garden-bird-ds-prep-with-mask-rcnn  
  - Dataset analysis - .https://www.kaggle.com/code/davemahony/1-20-uk-garden-bird-ds-prep-with-mask-rcnn 
