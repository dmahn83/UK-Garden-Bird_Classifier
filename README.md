![GitHub top language](https://img.shields.io/github/languages/top/gurugaurav/bing_image_downloader)
![GitHub](https://img.shields.io/github/license/gurugaurav/bing_image_downloader)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fgurugaurav%2Fbing_image_downloader&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
## UK Garden Bird Classifier <hr> 
Python library to classify images of UK Garden bird species </br>


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
pip install UK_Garden_Bird_Classifier
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




