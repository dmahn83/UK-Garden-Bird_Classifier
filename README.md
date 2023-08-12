## UK Garden Bird Classifier <hr> 
 Python library to classify images of the top 20 UK Garden Bird Species </br>


### Disclaimer<br />

The ResNet50 V2 model used by this program has been trained to classify the following species only:<br/><br/>
House_Sparrow<br/>
Bluetit<br/>
Starling<br/>
Wood_Pigeon<br/>
Blackbird<br/>
Robin<br/> 
Goldfinch<br/> 
Great_Tit<br/>
Magpie<br/> 
Long_Tailed_Tit<br/> 
Chaffinch<br/>
Dunnock<br/>
Jackdaw<br/> 
Feral_Pigeon<br/> 
Collared_Dove<br/>
Carrion_Crow<br/>
Coal_Tit<br/>
Greenfinch<br/>
Wren<br/>
Song_Thrush<br/>

### Installation <br />
```sh
!git clone https://github.com/dmahn83/20-UK-Garden-Birds
!cd 20-UK-Garden-Birds
!pip install .
```

### Usage <br />
```python
from UK_Garden_Bird_Classifier import classifier
classifier.classify_bird(img_path)
```


`img_path` : String representing the image path<br />

You can also test the program by runnning `run_test_cases()`
```python
from UK_Garden_Bird_Classifier import test_classifier
test_classifier.run_test_cases()
```




